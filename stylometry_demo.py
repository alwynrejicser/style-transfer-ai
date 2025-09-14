"""
Core Stylometry Analysis Functions - Demo Version
================================================
This demonstrates the analysis structure and output format.
"""

import os
import json

def read_text_file(file_path):
    """
    Reads text content from a file.
    
    Args:
        file_path (str): Path to the text file
        
    Returns:
        str: File content or error message
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return f"Error: File '{file_path}' not found"
    except Exception as e:
        return f"Error reading file: {e}"

def analyze_style(text_to_analyze):
    """
    Performs comprehensive stylometry analysis using LLM for style profile creation.
    
    Args:
        text_to_analyze (str): The text to be analyzed.
        
    Returns:
        str: Structured stylometric analysis for style profiling.
    """
    
    # Demo response showing the structure of actual analysis
    demo_analysis = """
    {
      "linguistic_patterns": {
        "sentence_structure": {
          "average_length": 18.5,
          "complexity_ratio": {
            "simple": 0.45,
            "compound": 0.35,
            "complex": 0.20
          },
          "preferred_types": ["declarative", "exclamatory"]
        },
        "clause_patterns": {
          "subordinate_usage": "moderate",
          "coordination_preference": "high",
          "subordination_preference": "low"
        },
        "punctuation_style": {
          "comma_density": 0.12,
          "semicolon_frequency": "rare",
          "dash_parentheses": "moderate dash usage, low parentheses"
        }
      },
      "lexical_characteristics": {
        "vocabulary_level": {
          "formal_informal_ratio": 0.3,
          "technical_terms": "low",
          "abstract_concrete_ratio": 0.4
        },
        "word_choice_patterns": {
          "adjective_density": 0.15,
          "adverb_density": 0.08,
          "specificity": "tends toward general terms"
        },
        "frequency_patterns": {
          "top_transitions": ["and", "but", "so", "then"],
          "preferred_conjunctions": ["and", "but"],
          "filler_words": ["really", "quite", "very"]
        }
      },
      "stylistic_markers": {
        "tone_indicators": {
          "confidence_level": "moderate",
          "emotional_markers": "affectionate, enthusiastic",
          "certainty_expressions": "moderate use of 'definitely', 'always'"
        },
        "narrative_voice": {
          "person_preference": "first_person",
          "active_passive_ratio": 0.85,
          "voice_consistency": "high"
        },
        "rhetorical_devices": {
          "metaphor_usage": "low",
          "repetition_patterns": "moderate",
          "parallel_structure": "occasional"
        }
      },
      "structural_preferences": {
        "paragraph_organization": {
          "length_preference": "medium",
          "transition_methods": "temporal and causal connectors"
        },
        "flow_patterns": {
          "idea_connection": "chronological and descriptive",
          "progression_style": "narrative-based"
        },
        "emphasis_techniques": {
          "highlighting_method": "repetition and exclamation"
        }
      },
      "personal_markers": {
        "idiomatic_expressions": ["love to", "used to", "really enjoys"],
        "cultural_references": "pet care, family activities",
        "formality_range": "casual to slightly formal"
      },
      "quantitative_metrics": {
        "words_analyzed": """ + str(len(text_to_analyze.split())) + """,
        "sentences_counted": """ + str(text_to_analyze.count('.') + text_to_analyze.count('!') + text_to_analyze.count('?')) + """,
        "paragraphs": """ + str(text_to_analyze.count('\\n\\n') + 1) + """
      }
    }
    """
    
    print("✓ Analysis completed successfully!")
    return demo_analysis

def create_style_profile(file_paths):
    """
    Creates a comprehensive style profile from multiple text samples.
    
    Args:
        file_paths (list): List of file paths containing user's writing samples
        
    Returns:
        dict: Consolidated style profile
    """
    
    all_analyses = []
    combined_text = ""
    
    for file_path in file_paths:
        file_content = read_text_file(file_path)
        
        if "Error" not in file_content:
            print(f"\n--- Analyzing File: {os.path.basename(file_path)} ---")
            
            # Individual file analysis
            analysis_result = analyze_style(file_content)
            all_analyses.append({
                'file': os.path.basename(file_path),
                'analysis': analysis_result,
                'word_count': len(file_content.split())
            })
            
            combined_text += file_content + "\n\n"
            print(f"✓ Analysis complete for {os.path.basename(file_path)}")
        else:
            print(f"Error reading {file_path}: {file_content}")
    
    # Comprehensive analysis of all texts combined
    if combined_text:
        print("\n--- Creating Consolidated Style Profile ---")
        comprehensive_analysis = analyze_style(combined_text)
        
        style_profile = {
            'individual_analyses': all_analyses,
            'comprehensive_profile': comprehensive_analysis,
            'total_word_count': len(combined_text.split()),
            'sample_count': len(all_analyses),
            'profile_created': True,
            'analysis_timestamp': '2025-09-15T12:00:00Z',
            'model_used': 'gpt-4o-mini'
        }
        
        return style_profile
    
    return {'profile_created': False, 'error': 'No valid text samples found'}

def save_style_profile(style_profile, profile_path="demo_style_profile.json"):
    """
    Saves the style profile to a JSON file for later use.
    
    Args:
        style_profile (dict): The style profile data
        profile_path (str): Path to save the profile
    """
    
    try:
        with open(profile_path, 'w', encoding='utf-8') as file:
            json.dump(style_profile, file, indent=2, ensure_ascii=False)
        print(f"\n✓ Style profile saved to: {profile_path}")
        return True
    except Exception as e:
        print(f"Error saving profile: {e}")
        return False

if __name__ == "__main__":
    # Define a list of file paths you want to analyze for style profiling
    file_paths = [
        "about_my_pet.txt",
        "about_my _pet_1.txt"
    ]
    
    print("Stylometry Analysis - Demo Output")
    print("=" * 60)
    print("This shows the structure and format of the analysis output")
    print("=" * 60)
    
    # Create comprehensive style profile
    style_profile = create_style_profile(file_paths)
    
    if style_profile['profile_created']:
        # Save the profile for later use in text generation
        save_style_profile(style_profile)
        
        print("\n" + "="*60)
        print("COMPREHENSIVE STYLE PROFILE CREATED")
        print("="*60)
        print("CONSOLIDATED ANALYSIS OUTPUT:")
        print("-" * 30)
        print(style_profile['comprehensive_profile'])
        print("\nProfile Statistics:")
        print(f"- Samples analyzed: {style_profile['sample_count']}")
        print(f"- Total words: {style_profile['total_word_count']}")
        print(f"- Model used: {style_profile['model_used']}")
        print(f"- Timestamp: {style_profile['analysis_timestamp']}")
        
        print("\n" + "="*60)
        print("INDIVIDUAL FILE ANALYSES:")
        print("="*60)
        for i, analysis in enumerate(style_profile['individual_analyses'], 1):
            print(f"\n📄 File {i}: {analysis['file']}")
            print(f"Word count: {analysis['word_count']}")
            print("Analysis structure (truncated):")
            print(analysis['analysis'][:200] + "...")
            
    else:
        print("Failed to create style profile")
        print(f"Error: {style_profile.get('error', 'Unknown error')}")