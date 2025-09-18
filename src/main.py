"""
Main orchestrator for Style Transfer AI.
Integrates all modules and provides the primary application entry point.
"""

import sys
import os
from datetime import datetime

# Add the src directory to the Python path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.menu.main_menu import run_main_menu
from src.menu.model_selection import require_model_selection
from src.config.settings import APPLICATION_NAME, VERSION, AUTHOR
from src.menu.navigation import print_header, clear_screen


def display_startup_banner():
    """Display the application startup banner."""
    clear_screen()
    print_header(f"{APPLICATION_NAME} v{VERSION}", width=70)
    print(f"Author: {AUTHOR}".center(70))
    print(f"Advanced Stylometry Analysis System".center(70))
    print("="*70)
    print()
    print("Features:")
    print("• 25-point deep stylometry analysis")
    print("• Multi-model support (Ollama, OpenAI, Gemini)")
    print("• Statistical readability metrics")
    print("• Cloud storage integration (Firestore)")
    print("• Privacy-first local processing")
    print("• Comprehensive style profiling")
    print()


def check_system_requirements():
    """
    Check system requirements and dependencies.
    
    Returns:
        dict: System check results
    """
    print("Checking system requirements...")
    
    issues = []
    warnings = []
    
    # Check Python version
    if sys.version_info < (3, 7):
        issues.append("Python 3.7 or higher is required")
    
    # Check for optional dependencies
    optional_deps = {
        'requests': 'HTTP requests (required for OpenAI, Gemini)',
        'firebase_admin': 'Firebase/Firestore integration',
        'openai': 'OpenAI API integration',
        'google.generativeai': 'Google Gemini integration'
    }
    
    for dep, description in optional_deps.items():
        try:
            __import__(dep)
        except ImportError:
            warnings.append(f"Optional dependency '{dep}' not installed - {description}")
    
    # Check directory structure
    required_dirs = [
        'src/config',
        'src/utils',
        'src/models',
        'src/analysis',
        'src/storage',
        'src/menu'
    ]
    
    for directory in required_dirs:
        if not os.path.exists(directory):
            issues.append(f"Required directory missing: {directory}")
    
    return {
        'success': len(issues) == 0,
        'issues': issues,
        'warnings': warnings
    }


def initialize_application():
    """
    Initialize the application and perform startup checks.
    
    Returns:
        bool: True if initialization successful, False otherwise
    """
    print("Initializing Style Transfer AI...")
    
    # Check system requirements
    system_check = check_system_requirements()
    
    if not system_check['success']:
        print("\n❌ CRITICAL ISSUES FOUND:")
        for issue in system_check['issues']:
            print(f"  • {issue}")
        print("\nPlease resolve these issues before continuing.")
        return False
    
    if system_check['warnings']:
        print("\n⚠️  WARNINGS:")
        for warning in system_check['warnings']:
            print(f"  • {warning}")
        print("\nSome features may not be available.")
    
    # Initialize model configuration
    print("\nInitializing model configuration...")
    print("⚠️  Model selection will be required before analysis.")
    
    print("\n✓ Application initialized successfully!")
    return True


def show_quick_start_guide():
    """Display a quick start guide for new users."""
    print("\n" + "="*60)
    print("QUICK START GUIDE")
    print("="*60)
    print("1. Select a model (Menu option 7)")
    print("   • Ollama models provide local, private processing")
    print("   • API models (OpenAI/Gemini) require internet and API keys")
    print()
    print("2. Prepare your writing samples")
    print("   • Gather 2-5 text files with your writing")
    print("   • Files should be at least 500 words each")
    print("   • Plain text (.txt) format works best")
    print()
    print("3. Run analysis (Menu option 1)")
    print("   • Choose 'Enhanced' for complete 25-point analysis")
    print("   • Choose 'Statistical' for quick readability metrics")
    print()
    print("4. View and manage results")
    print("   • Results saved locally and optionally to cloud")
    print("   • Use menu options 3-6 to manage profiles")
    print("="*60)


def main():
    """Main application entry point."""
    try:
        # Display startup banner
        display_startup_banner()
        
        # Initialize application
        if not initialize_application():
            print("\nInitialization failed. Exiting...")
            sys.exit(1)
        
        # Show quick start guide for first-time users
        from src.menu.navigation import confirm_action
        if confirm_action("\nShow quick start guide?", default='y'):
            show_quick_start_guide()
        
        from src.menu.navigation import pause_for_user
        pause_for_user()
        
        # Run main menu loop
        run_main_menu()
        
    except KeyboardInterrupt:
        print("\n\nApplication interrupted by user.")
        print("Thank you for using Style Transfer AI!")
        sys.exit(0)
        
    except Exception as e:
        print(f"\n❌ FATAL ERROR: {e}")
        print("\nPlease report this error to the development team.")
        print(f"Error details: {type(e).__name__}: {e}")
        sys.exit(1)


def cli_entry_point():
    """
    Command-line interface entry point.
    This function is called when the module is run as a script.
    """
    main()


if __name__ == "__main__":
    cli_entry_point()