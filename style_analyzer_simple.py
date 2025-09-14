import os
import json
from datetime import datetime
from openai import OpenAI

# Replace 'your-api-key-here' with your actual OpenAI API key
API_KEY = "your-api-key-here"

# Initialize OpenAI client with direct API key
client = OpenAI(api_key=API_KEY)

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
        str: Structured stylometric analysis for style profiling.
    """

    prompt = f"""
    Perform a comprehensive stylometry analysis of the following text for creating a detailed writing style profile. Analyze and provide specific, quantifiable insights on:

    **LINGUISTIC PATTERNS:**
    1. Sentence Structure: Average length, complexity patterns (simple/compound/complex ratios), preferred sentence types
    2. Clause Patterns: Subordinate clause usage, coordination vs subordination preferences
    3. Punctuation Style: Comma usage patterns, semicolon frequency, dash/parentheses preferences

    **LEXICAL CHARACTERISTICS:**
    4. Vocabulary Level: Formal vs informal ratio, technical term usage, abstract vs concrete word preferences
    5. Word Choice Patterns: Synonyms preferences, adjective/adverb density, specific vs general terms
    6. Frequency Patterns: Most used transition words, preferred conjunctions, filler words

    **STYLISTIC MARKERS:**
    7. Tone Indicators: Confidence level, emotional markers, certainty expressions
    8. Narrative Voice: Person preference (1st/2nd/3rd), active vs passive voice ratio
    9. Rhetorical Devices: Metaphor usage, repetition patterns, parallel structure frequency

    **STRUCTURAL PREFERENCES:**
    10. Paragraph Organization: Length preferences, topic transition methods
    11. Flow Patterns: How ideas are connected, logical progression style
    12. Emphasis Techniques: How important points are highlighted

    **PERSONAL MARKERS:**
    13. Idiomatic Expressions: Unique phrases or expressions used
    14. Cultural References: Types of references made
    15. Formality Adaptability: Range between formal and casual registers

    **ADVANCED ANALYSIS:**
    16. Discourse Markers: How transitions and connections are made
    17. Cognitive Style: Abstract vs concrete thinking patterns
    18. Emotional Patterns: How emotions are expressed and managed
    19. Authority Indicators: How expertise and confidence are conveyed
    20. Reader Engagement: How the author connects with the audience

    Provide your analysis as a structured profile with specific examples and percentages where possible. Format as detailed analysis for style profiling:

    Text to analyze:
    {text_to_analyze}
    """

    try:
        if API_KEY == "your-api-key-here":
            return "Error: Please replace 'your-api-key-here' with your actual OpenAI API key in the API_KEY variable."
        
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
    
    print("Creating comprehensive style profile...")
    print("=" * 60)
    
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
            print(f"✗ Error reading {file_path}: {file_content}")
    
    # Comprehensive analysis of all texts combined
    if combined_text:
        print("\n--- Creating Consolidated Style Profile ---")
        comprehensive_analysis = analyze_style(combined_text)
        
        style_profile = {
            'individual_analyses': all_analyses,
            'comprehensive_profile': comprehensive_analysis,
            'total_word_count': len(combined_text.split()),
            'sample_count': len(all_analyses),
            'model_used': 'gpt-4o-mini',
            'analysis_date': str(datetime.now()),
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
    try:
        with open(profile_path, 'w', encoding='utf-8') as file:
            json.dump(style_profile, file, indent=2, ensure_ascii=False)
        print(f"\n✓ Style profile saved to: {profile_path}")
        return True
    except Exception as e:
        print(f"✗ Error saving profile: {e}")
        return False

def load_style_profile(profile_path="user_style_profile.json"):
    """
    Loads a previously saved style profile.
    
    Args:
        profile_path (str): Path to the saved profile
        
    Returns:
        dict: Loaded style profile or None if error
    """
    try:
        with open(profile_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except Exception as e:
        print(f"Error loading profile: {e}")
        return None

def analyze_single_text(text_input):
    """
    Analyzes a single text input for quick style assessment.
    
    Args:
        text_input (str): Text to analyze
        
    Returns:
        str: Style analysis result
    """
    print("Analyzing text style...")
    return analyze_style(text_input)

def compare_styles(profile1_path, profile2_path):
    """
    Compares two style profiles to identify differences and similarities.
    
    Args:
        profile1_path (str): Path to first profile
        profile2_path (str): Path to second profile
        
    Returns:
        str: Comparison analysis
    """
    profile1 = load_style_profile(profile1_path)
    profile2 = load_style_profile(profile2_path)
    
    if not profile1 or not profile2:
        return "Error: Could not load one or both profiles for comparison."
    
    comparison_prompt = f"""
    Compare these two writing style profiles and identify:
    1. Key similarities in writing style
    2. Major differences in approach
    3. Unique characteristics of each style
    4. Overall compatibility assessment
    
    Profile 1: {profile1.get('comprehensive_profile', 'No profile data')}
    
    Profile 2: {profile2.get('comprehensive_profile', 'No profile data')}
    
    Provide a detailed comparison analysis:
    """
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": comparison_prompt}
            ],
            temperature=0.3
        )
        
        return response.choices[0].message.content
    except Exception as e:
        return f"Error in comparison: {e}"


if __name__ == "__main__":
    print("Style Transfer AI - Stylometry Analyzer")
    print("=" * 50)
    
    # Check if API key is set
    if API_KEY == "your-api-key-here":
        print("⚠️  Warning: Please set your OpenAI API key in the API_KEY variable")
        print("   Replace 'your-api-key-here' with your actual API key")
        exit(1)
    
    # Define file paths for analysis
    file_paths = [
        "about_my_pet.txt",
        "about_my _pet_1.txt"
    ]
    
    # Check if files exist in current directory
    existing_files = [f for f in file_paths if os.path.exists(f)]
    
    if not existing_files:
        print("⚠️  No sample text files found in current directory.")
        print("   Please ensure the following files exist:")
        for fp in file_paths:
            print(f"   - {fp}")
        print("\n   Or modify the file_paths list to point to your text samples.")
        exit(1)
    
    print(f"✓ Found {len(existing_files)} text sample(s) to analyze")
    
    # Create comprehensive style profile
    style_profile = create_style_profile(existing_files)
    
    if style_profile['profile_created']:
        # Save the profile for later use in text generation
        save_style_profile(style_profile)
        
        print("\n" + "="*60)
        print("COMPREHENSIVE STYLE PROFILE CREATED")
        print("="*60)
        print(style_profile['comprehensive_profile'])
        print(f"\nProfile Statistics:")
        print(f"- Samples analyzed: {style_profile['sample_count']}")
        print(f"- Total words: {style_profile['total_word_count']}")
        print(f"- Model used: {style_profile['model_used']}")
        print("\n✓ Your style profile is ready for text generation!")
    else:
        print("✗ Failed to create style profile")
        print(f"Error: {style_profile.get('error', 'Unknown error')}")