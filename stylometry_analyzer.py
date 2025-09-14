import openai
import os
from dotenv import load_dotenv

load_dotenv()

# This is a temporary print statement to verify the API key is being loaded.

print(f"API Key found: {bool(os.getenv('OPENAI_API_KEY'))}")

from openai import OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def read_text_file(file_path):
    """
    Reads the content of a text file.
    Returns the content or an error message.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return f"Error reading file: {e}"

def analyze_style(text_to_analyze):
    """
    Performs comprehensive stylometry analysis using LLM for style profile creation.
    
    Args:
        text_to_analyze (str): The text to be analyzed.
        
    Returns:
        dict: Structured stylometric analysis for style profiling.
    """

    prompt = f"""
    Perform a comprehensive stylometry analysis of the following text for creating a detailed writing style profile. Analyze and provide specific, quantifiable insights on:

    *LINGUISTIC PATTERNS:*
    1. Sentence Structure: Average length, complexity patterns (simple/compound/complex ratios), preferred sentence types
    2. Clause Patterns: Subordinate clause usage, coordination vs subordination preferences
    3. Punctuation Style: Comma usage patterns, semicolon frequency, dash/parentheses preferences

    *LEXICAL CHARACTERISTICS:*
    4. Vocabulary Level: Formal vs informal ratio, technical term usage, abstract vs concrete word preferences
    5. Word Choice Patterns: Synonyms preferences, adjective/adverb density, specific vs general terms
    6. Frequency Patterns: Most used transition words, preferred conjunctions, filler words

    *STYLISTIC MARKERS:*
    7. Tone Indicators: Confidence level, emotional markers, certainty expressions
    8. Narrative Voice: Person preference (1st/2nd/3rd), active vs passive voice ratio
    9. Rhetorical Devices: Metaphor usage, repetition patterns, parallel structure frequency

    *STRUCTURAL PREFERENCES:*
    10. Paragraph Organization: Length preferences, topic transition methods
    11. Flow Patterns: How ideas are connected, logical progression style
    12. Emphasis Techniques: How important points are highlighted

    *PERSONAL MARKERS:*
    13. Idiomatic Expressions: Unique phrases or expressions used
    14. Cultural References: Types of references made
    15. Formality Adaptability: Range between formal and casual registers

    Provide your analysis as a structured profile with specific examples and percentages where possible. Format as JSON-like structure for easy parsing:

    Text to analyze:
    {text_to_analyze}
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.3  # Lower temperature for more consistent analysis
        )
        
        return response.choices[0].message.content

    except Exception as e:
        return f"An error occurred: {e}"

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
            print("Individual Analysis Complete")
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
            'profile_created': True
        }
        
        return style_profile
    
    return {'profile_created': False, 'error': 'No valid text samples found'}

def save_style_profile(style_profile, profile_path="user_style_profile.json"):
    """
    Saves the style profile to a JSON file for later use.
    
    Args:
        style_profile (dict): The style profile data
        profile_path (str): Path to save the profile
    """
    import json
    
    try:
        with open(profile_path, 'w', encoding='utf-8') as file:
            json.dump(style_profile, file, indent=2, ensure_ascii=False)
        print(f"\nStyle profile saved to: {profile_path}")
        return True
    except Exception as e:
        print(f"Error saving profile: {e}")
        return False


if __name__ == "__main__":
    # Define a list of file paths you want to analyze for style profiling
    file_paths = [
        r"D:\stylometry_project\about_my_pet.txt",
        r"D:\stylometry_project\about_my _pet_1.txt"
    ]
    
    # Create comprehensive style profile
    style_profile = create_style_profile(file_paths)
    
    if style_profile['profile_created']:
        # Save the profile for later use in text generation
        save_style_profile(style_profile)
        
        print("\n" + "="*50)
        print("COMPREHENSIVE STYLE PROFILE CREATED")
        print("="*50)
        print(style_profile['comprehensive_profile'])
        print(f"\nProfile based on {style_profile['sample_count']} samples")
        print(f"Total words analyzed: {style_profile['total_word_count']}")
    else:
        print("Failed to create style profile")
