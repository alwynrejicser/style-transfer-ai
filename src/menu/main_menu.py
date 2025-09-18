"""
Main menu module for Style Transfer AI.
Handles primary navigation and menu display.
"""

import sys
import subprocess
import os
from ..config.settings import PROCESSING_MODES
from ..analysis.analyzer import create_enhanced_style_profile
from ..storage.local_storage import list_local_profiles, load_local_profile, cleanup_old_reports, save_style_profile_locally
from ..storage.firestore import manage_firestore_data_retention, initialize_firebase, save_to_firestore
from .model_selection import (
    select_model_interactive, 
    reset_model_selection, 
    get_current_model_info
)
from ..models.openai_client import setup_openai_client
from ..models.gemini_client import setup_gemini_client
from ..utils.user_profile import get_file_paths


def display_main_menu():
    """Display the main menu options."""
    
    print("\n" + "="*60)
    print("STYLE TRANSFER AI - ADVANCED STYLOMETRY ANALYSIS")
    print("="*60)
    
    # Show current model status
    model_info = get_current_model_info()
    if model_info['has_model']:
        print(f"Current Model: {model_info['selected_model']} (will be reset before next analysis)")
    else:
        print("Current Model: None (will be selected before analysis)")
    print("-" * 60)
    
    print("1. Analyze Writing Style (Complete Analysis)")
    print("2. Quick Style Analysis (Statistical Only)")
    print("3. View Existing Style Profiles")
    print("4. Manage Cloud Data (Firestore)")
    print("5. Cleanup Old Reports")
    print("6. Switch Analysis Model")
    print("7. Check Configuration")
    print("0. Exit")
    print("="*60)


def handle_analyze_style(processing_mode='enhanced'):
    """Handle style analysis workflow."""
    try:
        print(f"\nStarting {processing_mode} style analysis...")
        
        # Force model selection for each analysis
        print("\nPlease select a model for this analysis:")
        select_model_interactive()
        
        # Get current model info
        model_info = get_current_model_info()
        if not model_info['has_model']:
            print("No model selected. Analysis cancelled.")
            return
        
        # Get file paths from user
        file_paths = get_file_paths()
        
        if not file_paths:
            print("No files selected. Analysis cancelled.")
            return
        
        # Prepare model parameters based on selection
        if model_info['use_local_model']:
            # Local Ollama model
            style_profile = create_enhanced_style_profile(
                file_paths, 
                use_local=True, 
                model_name=model_info['selected_model'], 
                processing_mode=processing_mode
            )
        else:
            # Cloud API model
            model_type = None
            api_client = None
            
            if 'gpt' in model_info['selected_model'].lower():
                model_type = 'openai'
                client, message = setup_openai_client(model_info['user_chosen_api_key'])
                if client:
                    api_client = client
                    print(f"✓ {message}")
                else:
                    print(f"✗ Failed to setup OpenAI client: {message}")
                    return
            elif 'gemini' in model_info['selected_model'].lower():
                model_type = 'gemini'
                client, message = setup_gemini_client()
                if client:
                    api_client = client
                    print(f"✓ {message}")
                else:
                    print(f"✗ Failed to setup Gemini client: {message}")
                    return
            
            if not api_client:
                print("✗ Failed to initialize API client")
                return
            
            style_profile = create_enhanced_style_profile(
                file_paths,
                use_local=False,
                api_type=model_type,
                api_client=api_client,
                processing_mode=processing_mode
            )
        
        # Save the analysis results locally
        if style_profile:
            print("\nSaving analysis results...")
            save_result = save_style_profile_locally(style_profile)
            if save_result['success']:
                print(f"✓ {save_result['message']}")
                
                # Prompt user for cloud storage
                cloud_save = input("\nWould you like to save this analysis to the cloud (Firestore)? (y/n): ").strip().lower()
                if cloud_save == 'y':
                    print("\nInitializing cloud storage...")
                    if initialize_firebase():
                        print("Saving to cloud...")
                        cloud_result = save_to_firestore(style_profile)
                        if cloud_result['success']:
                            print(f"✓ Successfully saved to cloud: {cloud_result.get('document_name', 'Unknown')}")
                        else:
                            print(f"✗ Failed to save to cloud: {cloud_result.get('error', 'Unknown error')}")
                    else:
                        print("✗ Cloud storage not available. See setup instructions for Firebase configuration.")
                else:
                    print("Skipping cloud save.")
            else:
                print(f"✗ Failed to save results: {save_result.get('error', 'Unknown error')}")
        
        print("\nAnalysis completed successfully!")
        
        # Reset model selection to force re-selection next time
        reset_model_selection()
        
        input("\nPress Enter to continue...")
        
    except KeyboardInterrupt:
        print("\n\nAnalysis interrupted by user.")
        # Reset model selection even if interrupted
        reset_model_selection()
    except Exception as e:
        print(f"\nError during analysis: {e}")
        # Reset model selection even if error occurred
        reset_model_selection()


def handle_view_profiles():
    """Handle viewing existing style profiles."""
    profiles = list_local_profiles()
    
    if not profiles:
        print("\nNo style profiles found.")
        return
    
    print(f"\nFound {len(profiles)} style profiles:")
    print("-" * 80)
    
    for i, profile in enumerate(profiles, 1):
        print(f"{i:2d}. {profile['filename']} | {profile['user_name']} | {profile['analysis_date']} | {profile['size_mb']:.2f} MB")
    
    print("-" * 80)
    
    try:
        while True:
            choice = input("\nEnter profile number to view (0 to return): ").strip()
            
            if choice == "0":
                break
            
            try:
                profile_num = int(choice)
                if 1 <= profile_num <= len(profiles):
                    selected_profile = profiles[profile_num - 1]
                    result = load_local_profile(selected_profile['filepath'])
                    
                    if result['success']:
                        profile_data = result['profile']
                        display_profile_summary(profile_data)
                        
                        # Ask if user wants to see full report
                        view_full = input("\nView full human-readable report? (y/n): ").strip().lower()
                        if view_full == 'y':
                            if 'human_readable_report' in profile_data:
                                print("\n" + "="*80)
                                print("FULL STYLE ANALYSIS REPORT")
                                print("="*80)
                                print(profile_data['human_readable_report'])
                            else:
                                print("Human-readable report not available in this profile.")
                    else:
                        print(f"Error loading profile: {result['error']}")
                else:
                    print("Invalid profile number.")
            except ValueError:
                print("Invalid input. Please enter a number.")
                
    except KeyboardInterrupt:
        print("\n\nReturning to main menu...")


def display_profile_summary(profile_data):
    """Display a summary of a style profile."""
    print("\n" + "="*80)
    print("STYLE PROFILE SUMMARY")
    print("="*80)
    
    # User information
    user_profile = profile_data.get('user_profile', {})
    print(f"User: {user_profile.get('name', 'Unknown')}")
    print(f"Background: {user_profile.get('background', 'Not specified')}")
    print(f"Writing Goals: {user_profile.get('writing_goals', 'Not specified')}")
    
    # Analysis metadata
    metadata = profile_data.get('metadata', {})
    print(f"\nAnalysis Date: {metadata.get('analysis_date', 'Unknown')}")
    print(f"Model Used: {metadata.get('model_used', 'Unknown')}")
    print(f"Processing Mode: {metadata.get('processing_mode', 'Unknown')}")
    print(f"Files Analyzed: {metadata.get('total_samples', 0)}")
    print(f"Total Words: {metadata.get('total_words', 0):,}")
    
    # Statistical summary
    statistics = profile_data.get('statistical_analysis', {})
    if statistics:
        print(f"\nReadability Scores:")
        print(f"  Flesch Reading Ease: {statistics.get('flesch_reading_ease', 'N/A')}")
        print(f"  Flesch-Kincaid Grade: {statistics.get('flesch_kincaid_grade', 'N/A')}")
        print(f"  Coleman-Liau Index: {statistics.get('coleman_liau_index', 'N/A')}")
        print(f"  Lexical Diversity: {statistics.get('lexical_diversity', 'N/A')}")
    
    # Deep analysis summary (if available)
    deep_analysis = profile_data.get('deep_stylometry_analysis', {})
    if deep_analysis and 'analysis_summary' in deep_analysis:
        print(f"\nDeep Analysis Summary:")
        summary = deep_analysis['analysis_summary']
        # Show first 200 characters of summary
        print(f"  {summary[:200]}...")
    
    print("="*80)


def handle_cleanup_reports():
    """Handle cleanup of old reports."""
    print("\nCleaning up old reports...")
    
    # Get cleanup preferences
    try:
        days = input("Keep reports from last how many days? (default: 30): ").strip()
        if not days:
            days = 30
        else:
            days = int(days)
        
        result = cleanup_old_reports(days_to_keep=days)
        
        if result['success']:
            print(f"SUCCESS: {result['message']}")
            if result['deleted_files']:
                print("Deleted files:")
                for file in result['deleted_files']:
                    print(f"  - {file}")
        else:
            print(f"ERROR: {result['error']}")
            
    except ValueError:
        print("Invalid input. Using default 30 days.")
        result = cleanup_old_reports(days_to_keep=30)
        if result['success']:
            print(f"SUCCESS: {result['message']}")
    except Exception as e:
        print(f"Error during cleanup: {e}")
    
    input("\nPress Enter to continue...")


def handle_cloud_data_management():
    """Handle cloud data management (Firestore)."""
    print("\nInitializing Firestore...")
    
    if initialize_firebase():
        manage_firestore_data_retention()
    else:
        print("Firestore not available. Please check your Firebase configuration.")


def handle_check_configuration():
    """Handle configuration checking."""
    try:
        print("\nRunning configuration check...")
        
        # Get the path to the project root (where check_config.py is located)
        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.dirname(os.path.dirname(current_dir))
        check_config_path = os.path.join(project_root, "check_config.py")
        
        if os.path.exists(check_config_path):
            # Run the check_config.py script
            result = subprocess.run([sys.executable, check_config_path], 
                                 capture_output=False, text=True, cwd=project_root)
            
            print(f"\nConfiguration check completed with exit code: {result.returncode}")
        else:
            print(f"\nError: Configuration checker not found at {check_config_path}")
        
        input("\nPress Enter to continue...")
        
    except KeyboardInterrupt:
        print("\n\nReturning to main menu...")
    except Exception as e:
        print(f"\nError running configuration check: {e}")


def run_main_menu():
    """Run the main menu loop."""
    while True:
        try:
            display_main_menu()
            choice = input("\nEnter your choice (0-7): ").strip()
            
            if choice == "0":
                print("\nThank you for using Style Transfer AI!")
                sys.exit(0)
                
            elif choice == "1":
                handle_analyze_style(processing_mode='enhanced')
                
            elif choice == "2":
                handle_analyze_style(processing_mode='statistical')
                
            elif choice == "3":
                handle_view_profiles()
                
            elif choice == "4":
                handle_cloud_data_management()
                
            elif choice == "5":
                handle_cleanup_reports()
                
            elif choice == "6":
                reset_model_selection()
                print("\nModel selection reset. Please choose a new model:")
                select_model_interactive()
                
            elif choice == "7":
                handle_check_configuration()
                
            else:
                print("Invalid choice. Please enter 0-7.")
                
        except KeyboardInterrupt:
            print("\n\nExiting Style Transfer AI...")
            sys.exit(0)
        except Exception as e:
            print(f"Unexpected error: {e}")


if __name__ == "__main__":
    run_main_menu()