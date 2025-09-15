# Style Transfer AI - Enhanced Deep Stylometry Analyzer v4.5

🎯 **Advanced stylometry analysis system with personalized linguistic fingerprinting and dual output formats**

## Features

✅ **Personalized Stylometric Fingerprints**:
- **Name-based file organization**: Files saved as `{name}_stylometric_profile_{timestamp}`
- **Personal identity integration**: Your name prominently displayed in analysis
- **Stylometric fingerprint concept**: Treats writing analysis as unique personal identifiers
- **Safe filename handling**: Automatic sanitization for filesystem compatibility

✅ **Performance Optimization**:
- **GPT-OSS Dual Modes**: Turbo (faster, 2000 tokens) vs Normal (thorough, 3000 tokens)
- **Intelligent timeout management**: Mode-specific processing times
- **Resource-aware processing**: Optimized for different analysis depths

✅ **Hierarchical Model Selection**:
- **Local Processing**: GPT-OSS 20B (advanced), Gemma 3:1B (fast)
- **Online Processing**: OpenAI GPT-3.5-turbo, Google Gemini-1.5-flash
- **Intuitive navigation**: Main menu → Sub-menus with back navigation
- **Professional interface**: Clean, emoji-free design for serious analysis

✅ **Enhanced Deep Analysis**:
- **25-point stylometric framework** (upgraded from 15-point)
- **Dual output formats**: JSON (machine-readable) + TXT (human-readable)
- **Advanced metrics**: Readability scores, lexical diversity, psychological profiling
- **Statistical analysis**: Word frequencies, punctuation patterns, complexity indices
- Individual file analysis + consolidated profiling

✅ **Privacy & Flexibility**:
- Local processing for confidential content
- Multiple cloud API options (OpenAI, Gemini)
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

#### For Cloud APIs (Optional)
**OpenAI API:**
1. Get your API key from [OpenAI Platform](https://platform.openai.com/api-keys)
2. Replace placeholder in the code:
   ```python
   OPENAI_API_KEY = "your-openai-api-key-here"  # Replace with your actual key
   ```

**Google Gemini API:**
1. Get your API key from [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Replace placeholder in the code:
   ```python
   GEMINI_API_KEY = "your-gemini-api-key-here"  # Replace with your actual key
   ```

### 2. Install Dependencies
```bash
pip install requests openai google-generativeai
```

### 3. Prepare Your Text Samples
Place your writing samples in the project directory:
- `about_my_pet.txt`
- `about_my _pet_1.txt`
- Or modify file paths in the code

### 4. Run Analysis
```bash
python style_analyzer_enhanced.py
```

## Key Workflow

### Personal Profile Setup
1. **Name Collection**: Your name is collected first as stylometric profiles are personal fingerprints
2. **Cultural Context**: Language background, nationality, education details
3. **Writing Experience**: Frequency and background information
4. **Streamlined Process**: Only essential information collected for meaningful analysis

### Processing Modes (GPT-OSS)
When using GPT-OSS models, choose your processing mode:
- **Turbo Mode**: Faster analysis (2000 tokens, 120s timeout) for quick insights
- **Normal Mode**: Thorough analysis (3000 tokens, 180s timeout) for comprehensive profiling

## Usage

### Model Selection
The analyzer features a **hierarchical menu system** for intuitive model selection:

**Main Menu:**
1. **Local Processing** (Privacy-focused)
2. **Online Processing** (Cloud-based)

**Local Models Sub-menu:**
- **GPT-OSS 20B** - Advanced comprehensive analysis
- **Gemma 3:1B** - Fast efficient processing

**Online Models Sub-menu:**
- **OpenAI GPT-3.5-turbo** - Cloud-based analysis
- **Google Gemini-1.5-flash** - Google's latest language model

**Navigation:** Use '0' to go back to the previous menu or exit the application.

### Enhanced Output
The analyzer generates **personalized stylometric fingerprints**:
- **Individual analyses** for each text file with 25-point deep analysis
- **Consolidated style profile** combining all samples
- **Personalized file naming**: `{your_name}_stylometric_profile_{timestamp}`
  - Example: `John_Doe_stylometric_profile_20250915_123456.json`
- **Dual format outputs**:
  - **JSON file** - Machine-readable data for further processing
  - **TXT file** - Human-readable report with your name prominently displayed
- **Writer Identity Section**: Your name featured prominently in analysis header
- **Advanced metrics**: Readability scores, lexical diversity, statistical analysis
- **Comprehensive metadata** with timestamps and detailed file information
- **Automatic cleanup**: Option to remove old reports with both naming patterns

## API Key Configuration

### Method 1: Direct Code Modification
Replace the placeholders in `style_analyzer_enhanced.py`:

```python
OPENAI_API_KEY = "your-actual-openai-api-key-here"
GEMINI_API_KEY = "your-actual-gemini-api-key-here"
```

### Method 2: Interactive Setup (Recommended)
The analyzer will automatically:
1. Detect existing API keys for both OpenAI and Gemini
2. Prompt for new keys if needed based on your model choice
3. Validate key format and provide helpful URLs
4. Handle setup cancellation gracefully
5. Support switching between different API providers

## Project Structure

```
style-transfer-ai/
├── style_analyzer_enhanced.py           # Enhanced deep analyzer v4.5 (25-point framework)
├── .github/
│   └── copilot-instructions.md         # Development guidelines for GitHub Copilot
├── IMPLEMENTATION.md                    # Detailed technical documentation
├── README.md                           # This file
├── futureimprov.md                     # Future improvement plans
├── .env.example                        # Environment configuration template
├── .gitignore                          # Git ignore for security
├── about_my_pet.txt                    # Sample text file 1
├── about_my_pet_1.txt                  # Sample text file 2
└── {name}_stylometric_profile_*.json   # Your personalized analysis (JSON)
└── {name}_stylometric_profile_*.txt    # Your personalized analysis (TXT)
```

## What's New in v4.5

🆕 **Personalized Stylometric Fingerprints**:
- Your name is now collected and used for file naming
- Files saved as `{Name}_stylometric_profile_{timestamp}`
- Writer identity prominently displayed in analysis
- Automatic filename sanitization for safe storage

⚡ **GPT-OSS Performance Modes**:
- **Turbo Mode**: Quick analysis with optimized parameters
- **Normal Mode**: Comprehensive deep analysis
- User choice for processing speed vs thoroughness

🏗️ **Enhanced Architecture**:
- Streamlined user profile collection (8 essential fields)
- Professional interface without emoji clutter
- Improved error handling and connection validation
- Updated cleanup functionality for all naming patterns

## Enhanced Stylometric Analysis Framework

The analyzer evaluates **25 comprehensive dimensions** across 7 categories:

### Part 1: Linguistic Architecture
1. **Sentence Structure Mastery**: Exact averages, complexity ratios with percentages
2. **Clause Choreography**: Subordinate clause frequency, coordination patterns
3. **Punctuation Symphony**: Complete punctuation analysis with frequencies
4. **Syntactic Sophistication**: Sentence variety index, grammatical complexity scoring

### Part 2: Lexical Intelligence  
5. **Vocabulary Sophistication**: Word complexity levels, formal/informal ratios
6. **Semantic Field Preferences**: Domain categorization (abstract/concrete, emotional/logical)
7. **Lexical Diversity Metrics**: Type-token ratio, vocabulary richness index
8. **Register Flexibility**: Formality spectrum analysis, colloquialism detection

### Part 3: Stylistic DNA
9. **Tone Architecture**: Confidence indicators, emotional markers with examples
10. **Voice Consistency**: Person preference analysis, active/passive voice ratios
11. **Rhetorical Weaponry**: Metaphor counting, parallel structures, repetition patterns
12. **Narrative Technique**: Point of view consistency, storytelling vs explanatory modes

### Part 4: Cognitive Patterns
13. **Logical Flow Design**: Argument structure, cause-effect pattern analysis
14. **Transition Mastery**: Transition word categorization, coherence mechanisms
15. **Emphasis Engineering**: Key point highlighting strategies, linguistic intensity
16. **Information Density**: Concept-to-word ratios, information packaging efficiency

### Part 5: Psychological Markers
17. **Cognitive Processing Style**: Linear vs circular thinking, analytical patterns
18. **Emotional Intelligence**: Empathy markers, emotional vocabulary richness
19. **Authority Positioning**: Hedging language, assertiveness markers, expertise indicators
20. **Risk Tolerance**: Certainty language analysis, qualification usage patterns

### Part 6: Structural Genius
21. **Paragraph Architecture**: Length variance, topic development patterns
22. **Coherence Engineering**: Text cohesion measurement, referential chains
23. **Temporal Dynamics**: Tense usage patterns, time reference preferences
24. **Modal Expression**: Modal verb counting, probability vs obligation language

### Part 7: Unique Fingerprint
25. **Personal Signature Elements**: Unique phrases, idiosyncratic expressions, personal habits

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

**GPT-OSS Performance Issues**:
- Try **Turbo Mode** for faster processing
- Switch to **Normal Mode** for detailed analysis
- Check system resources during processing
- Verify model is fully loaded in Ollama

**OpenAI API Errors**:
- Check API key validity
- Verify account has sufficient credits
- Ensure proper key format (starts with 'sk-')

**File Naming Issues**:
- Special characters in names are automatically sanitized
- Long names are truncated to 50 characters
- Empty names default to "Anonymous_User"
- Files are timestamped for unique identification

**File Not Found**:
- Verify text files exist in project directory
- Check file names match exactly
- Ensure proper file encoding (UTF-8)

## Contributing

Contributions welcome! Please ensure:
- No real API keys in commits
- Update documentation for new features
- Test with all model types and processing modes
- Follow existing code style and naming conventions
- Include personalization features in new developments

## Version History

- **v4.5** (Current): Personalized stylometric fingerprints, GPT-OSS performance modes
- **v4.0**: Enhanced deep analysis framework (25-point system)
- **v3.0**: Hierarchical model selection with local/online options
- **v2.0**: Dual output formats (JSON + TXT)
- **v1.0**: Basic stylometry analysis

## License

MIT License - See LICENSE file for details

---

**Made with ❤️ for the AI community - Your Writing, Your Fingerprint, Your Identity**
