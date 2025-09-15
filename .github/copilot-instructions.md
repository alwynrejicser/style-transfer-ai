# GitHub Copilot Instructions - Style Transfer AI

## Project Overview
**Style Transfer AI** is an advanced stylometry analysis system that extracts deep linguistic patterns from writing samples to create comprehensive style profiles. The system supports tri-model architecture (local Ollama + OpenAI API) with privacy-first local processing capabilities.

## Architecture & Key Components

### Tri-Model System
- **Local Ollama Models**: `gpt-oss:20b` (advanced) and `gemma3:1b` (fast) via HTTP API
- **OpenAI API**: GPT-3.5-turbo fallback with flexible key management
- **Model Selection**: Interactive CLI choice system with connection validation

### Core Analysis Pipeline
1. **Text Ingestion**: Multi-file processing with UTF-8 encoding fallback to latin-1
2. **Statistical Analysis**: Word frequencies, punctuation patterns, lexical diversity calculations
3. **Readability Metrics**: Flesch scores, Coleman-Liau index, syllable counting algorithms
4. **Deep Stylometry**: 25-point linguistic analysis framework via structured LLM prompts
5. **Dual Output**: JSON (machine-readable) + TXT (human-readable) with timestamps

### Key File: `style_analyzer_enhanced.py`
- **Main entry point**: Interactive model selection and analysis workflow
- **Global state**: `USE_LOCAL_MODEL`, `SELECTED_MODEL`, `USER_CHOSEN_API_KEY`
- **API patterns**: Ollama HTTP requests to `localhost:11434/api/generate` with model-specific parameters

## Critical Development Patterns

### Model Communication
```python
# Ollama payload structure - adjust num_predict by model size
payload = {
    "model": model_name,
    "prompt": prompt,
    "stream": False,
    "options": {
        "temperature": 0.2,  # Lower for consistent analysis
        "num_predict": 3000 if "gpt-oss" in model_name else 2000,
        "timeout": 180  # Extended for deep analysis
    }
}
```

### Error Handling Strategy
- **Connection failures**: Graceful fallback from local to API models
- **Timeout handling**: Model-specific timeout values (180s for deep analysis)
- **File encoding**: UTF-8 with latin-1 fallback for text reading
- **API key validation**: Length checks and interactive replacement

### Output File Naming
- **JSON**: `user_style_profile_enhanced_TIMESTAMP.json`
- **TXT**: `user_style_profile_enhanced_TIMESTAMP.txt`
- **Timestamp format**: `%Y%m%d_%H%M%S` for chronological sorting

## Stylometry Analysis Framework

### 25-Point Analysis Structure
The system uses structured prompts divided into 7 categories:
1. **Linguistic Architecture** (4 points): Sentence structure, clause patterns, punctuation, syntax
2. **Lexical Intelligence** (4 points): Vocabulary sophistication, semantic fields, diversity metrics
3. **Stylistic DNA** (4 points): Tone architecture, voice consistency, rhetorical devices
4. **Cognitive Patterns** (4 points): Logical flow, transitions, emphasis techniques
5. **Psychological Markers** (4 points): Processing style, emotional intelligence, authority positioning
6. **Structural Genius** (4 points): Paragraph architecture, coherence, temporal dynamics
7. **Unique Fingerprint** (1 point): Personal signature elements

### Statistical Metrics Implementation
- **Lexical diversity**: `unique_words / total_words`
- **Readability scores**: Flesch Reading Ease, Flesch-Kincaid Grade Level, Coleman-Liau Index
- **Syllable counting**: Vowel pattern algorithm with silent 'e' handling
- **Punctuation analysis**: Counter-based frequency tracking

## Development Workflow

### Prerequisites Setup
```bash
# Ollama installation and model pulling
ollama pull gpt-oss:20b
ollama pull gemma3:1b
ollama serve

# Python dependencies
pip install requests openai
```

### Testing Workflow
- **Sample files**: `about_my_pet.txt`, `about_my_pet_1.txt` in project root
- **Interactive testing**: Run `python style_analyzer_enhanced.py` for full workflow
- **Model validation**: Check Ollama connection before analysis starts

### Security Considerations
- **API keys**: Use placeholder `"your-openai-api-key-here"` in code
- **Environment variables**: Reference `.env.example` for production setup
- **Local processing**: Default to Ollama models for privacy-sensitive content

## Code Modification Guidelines

### Adding New Models
1. Update `AVAILABLE_MODELS` dictionary with model name and description
2. Adjust `num_predict` parameters based on model capabilities
3. Test connection validation in `check_ollama_connection()`

### Extending Analysis Framework
- **Prompt modification**: Update `create_enhanced_deep_prompt()` with new analysis dimensions
- **Output processing**: Extend `format_human_readable_output()` for new metrics
- **Statistical functions**: Add new metric calculations to `analyze_text_statistics()`

### File Processing Extensions
- **New input formats**: Extend `read_text_file()` with additional encoding support
- **Batch processing**: Modify file path handling in `create_enhanced_style_profile()`

When working on this codebase, prioritize local model usage for privacy, maintain the dual-output format pattern, and ensure all new features support the tri-model architecture.