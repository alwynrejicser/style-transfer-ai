import openai
import os
from dotenv import load_dotenv

load_dotenv()

# This is a temporary print statement to verify the API key is being loaded.
print(f"API Key found: {bool(os.getenv('OPENAI_API_KEY'))}")

from openai import OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_style(text_to_analyze):
    """
    Analyzes the writing style of a given paragraph using the OpenAI API.
    
    Args:
        text_to_analyze (str): The paragraph of text to be analyzed.
        
    Returns:
        str: The stylistic analysis provided by the model.
    """

    prompt = f"""
    Analyze the writing style of the following paragraph. Focus on the following aspects:
    1. Sentence structure (e.g., simple, complex, long, short).
    2. Vocabulary (e.g., formal, informal, specialized, simple).
    3. Tone (e.g., authoritative, conversational, academic).
    4. Narrative voice (e.g., first person, third person, passive voice).
    5. Use of literary devices (e.g., metaphors, alliteration, figurative language).

    Provide your analysis in a structured, point-by-point format. The paragraph is:
    
    {text_to_analyze}
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.7 # A lower temperature makes the output more focused and less random
        )
        
        # Extract and return the model's response
        return response.choices[0].message.content

    except Exception as e:
        return f"An error occurred: {e}"

def read_text_file(file_path):
    """
    Reads the content of a text file and returns it as a string.
    
    Args:
        file_path (str): The path to the text file.
        
    Returns:
        str: The content of the file, or an error message if the file is not found.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return "Error: File not found."

if __name__ == "__main__":
    # Define a list of file paths you want to analyze.
    # Add your additional text file names here.
    file_paths = [
        r"D:\stylometry_project\about_my_pet.txt",
        r"D:\stylometry_project\about_my _pet_1.txt"
    ]

    for file_path in file_paths:
        file_content = read_text_file(file_path)

        print(f"\n--- Analyzing File: {os.path.basename(file_path)} ---\n")

        if "Error" not in file_content:
            analysis_result = analyze_style(file_content)
            print("Stylistic Analysis:\n")
            print(analysis_result)
        else:
            print(file_content)