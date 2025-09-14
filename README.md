<<<<<<< HEAD
# Style Transfer AI - Perfect Stylometry Analyzer

🎯 **Ultimate stylometry analysis system with tri-model support for comprehensive writing style profiling**

## Features

✅ **Tri-Model Architecture**:
- **Local Ollama - GPT-OSS 20B**: Advanced, comprehensive analysis
- **Local Ollama - Gemma 3:1B**: Fast, efficient analysis  
- **OpenAI API - GPT-3.5-turbo**: Cloud-based analysis

✅ **Advanced Analysis**:
- 15-point stylometric framework
- Individual file analysis + consolidated profiling
- JSON-structured output with metadata
- Professional error handling and fallback mechanisms

✅ **Privacy & Flexibility**:
- Local processing for confidential content
- Flexible API key management
- No data sharing with local models
- Production-ready architecture

## Quick Start

### 1. Setup Requirements

#### For Local Models (Recommended)
```bash
# Install Ollama
# Visit: https://ollama.ai/download

# Pull the models
ollama pull gpt-oss:20b      # Advanced model
ollama pull gemma3:1b        # Fast model

# Start Ollama server
ollama serve
```

#### For OpenAI API (Optional)
1. Get your API key from [OpenAI Platform](https://platform.openai.com/api-keys)
2. Replace placeholder in the code files:
   ```python
   OPENAI_API_KEY = "your-openai-api-key-here"  # Replace with your actual key
   ```

### 2. Install Dependencies
```bash
pip install requests openai
```

### 3. Prepare Your Text Samples
Place your writing samples in the project directory:
- `about_my_pet.txt`
- `about_my _pet_1.txt`
- Or modify file paths in the code

### 4. Run Analysis
```bash
python style_analyzer_simple.py
```

## Usage

### Model Selection
When you run the analyzer, choose your preferred model:

```
Choose your analysis method:
1. Local Ollama - GPT-OSS 20B (Advanced, Comprehensive)
2. Local Ollama - Gemma 3:1B (Fast, Efficient)
3. OpenAI API - GPT-3.5-turbo (Cloud, Requires API key)
```

### Output
The analyzer generates:
- **Individual analyses** for each text file
- **Consolidated style profile** combining all samples
- **Comprehensive metadata** (word counts, timestamps, model info)
- **JSON file** (`user_style_profile.json`) for further processing

## API Key Configuration

### Method 1: Direct Code Modification
Replace the placeholder in any of these files:
- `style_analyzer_simple.py`
- `style_analyzer_perfect.py` 
- `stylometry_analysis_core.py`

```python
OPENAI_API_KEY = "your-actual-openai-api-key-here"
```

### Method 2: Interactive Setup (Recommended)
The analyzer will automatically:
1. Detect existing API keys
2. Prompt for new keys if needed
3. Validate key format
4. Handle setup cancellation gracefully

## Project Structure

```
style-transfer-ai/
├── style_analyzer_simple.py     # Main tri-model analyzer
├── style_analyzer_perfect.py    # Enhanced version
├── stylometry_analysis_core.py  # Core analysis functions
├── stylometry_demo.py           # Demo with sample output
├── IMPLEMENTATION.md            # Detailed documentation
├── README.md                    # This file
├── user_style_profile.json     # Generated analysis results
└── demo_style_profile.json     # Example output structure
```

## Stylometric Analysis Framework

The analyzer evaluates **15 comprehensive dimensions**:

### Linguistic Patterns
1. **Sentence Structure**: Length, complexity, preferred types
2. **Clause Patterns**: Subordination vs coordination preferences
3. **Punctuation Style**: Comma density, semicolon usage, dash patterns

### Lexical Characteristics  
4. **Vocabulary Level**: Formal/informal ratio, technical terms
5. **Word Choice**: Adjective density, synonym preferences
6. **Frequency Patterns**: Transition words, conjunctions, fillers

### Stylistic Markers
7. **Tone Indicators**: Confidence, emotional markers, certainty
8. **Narrative Voice**: Person preference, active/passive ratio
9. **Rhetorical Devices**: Metaphors, repetition, parallel structure

### Structural Preferences
10. **Paragraph Organization**: Length, transition methods
11. **Flow Patterns**: Idea connection, progression style
12. **Emphasis Techniques**: Highlighting methods

### Personal Markers
13. **Idiomatic Expressions**: Unique phrases, expressions
14. **Cultural References**: Reference types and patterns
15. **Formality Range**: Casual to formal adaptability

## Security & Best Practices

🔐 **API Key Security**:
- Never commit real API keys to version control
- Use environment variables for production
- Rotate keys regularly
- Monitor usage and costs

🛡️ **Privacy**:
- Use local models for sensitive content
- Local processing keeps data on your machine
- No internet connection required for Ollama models

## Troubleshooting

### Common Issues

**Ollama Connection Failed**:
```bash
# Make sure Ollama is running
ollama serve

# Check if models are installed
ollama list

# Pull missing models
ollama pull gpt-oss:20b
ollama pull gemma3:1b
```

**OpenAI API Errors**:
- Check API key validity
- Verify account has sufficient credits
- Ensure proper key format (starts with 'sk-')

**File Not Found**:
- Verify text files exist in project directory
- Check file names match exactly
- Ensure proper file encoding (UTF-8)

## Contributing

Contributions welcome! Please ensure:
- No real API keys in commits
- Update documentation for new features
- Test with all three model types
- Follow existing code style

## License

MIT License - See LICENSE file for details

---

**Made with ❤️ for the AI community**
