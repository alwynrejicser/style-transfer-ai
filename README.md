# Style Transfer AI - Enhanced Deep Stylometry Analyzer

🎯 **Advanced stylometry analysis system with deep linguistic profiling and dual output formats**

## Features

✅ **Hierarchical Model Selection**:
- **Local Processing**: GPT-OSS 20B (advanced), Gemma 3:1B (fast)
- **Online Processing**: OpenAI GPT-3.5-turbo, Google Gemini-1.5-flash
- **Intuitive navigation**: Main menu → Sub-menus with back navigation
- **User-friendly interface**: Emoji-enhanced menus and clear options

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
The analyzer generates:
- **Individual analyses** for each text file with 25-point deep analysis
- **Consolidated style profile** combining all samples
- **Dual format outputs**:
  - **JSON file** (`user_style_profile_enhanced_TIMESTAMP.json`) - Machine-readable data
  - **TXT file** (`user_style_profile_enhanced_TIMESTAMP.txt`) - Human-readable report
- **Advanced metrics**: Readability scores, lexical diversity, statistical analysis
- **Comprehensive metadata** with timestamps and detailed file information

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
├── style_analyzer_enhanced.py           # Enhanced deep analyzer (25-point framework)
├── IMPLEMENTATION.md                    # Detailed documentation
├── README.md                           # This file
├── .env.example                        # Environment configuration template
├── .gitignore                          # Git ignore for security
├── about_my_pet.txt                    # Sample text file 1
├── about_my_pet_1.txt                  # Sample text file 2
└── user_style_profile_enhanced_*.json  # Generated analysis results (JSON)
└── user_style_profile_enhanced_*.txt   # Generated analysis results (TXT)
```

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
