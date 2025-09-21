# 🛠️ **Installation Guide - For Your Friend**

## 📥 **Download & Install (Step-by-Step)**

Hey! Here's how to get Style Transfer AI running on your machine:

### **Prerequisites**
- **Python 3.7+** ([Download here](https://python.org/downloads/))
- **Git** ([Download here](https://git-scm.com/downloads))

---

## 🚀 **Method 1: Quick Install (Recommended)**

### **1. Clone the Repository**
```bash
git clone https://github.com/alwynrejicser/style-transfer-ai.git
cd style-transfer-ai
```

### **2. Run Automated Installation**

**Windows:**
```bash
# Double-click or run in PowerShell
install\quick_install.bat
```

**Linux/Mac:**
```bash
# Make sure you have Python 3.7+
python3 -m pip install -e .
```

### **3. Test Installation**
```bash
style-transfer-ai --version
```

If you see version info, you're ready! 🎉

---

## 🛠️ **Method 2: Manual Installation**

### **1. Clone Repository**
```bash
git clone https://github.com/alwynrejicser/style-transfer-ai.git
cd style-transfer-ai
```

### **2. Create Virtual Environment (Optional but Recommended)**
```bash
python -m venv .venv

# Activate it:
# Windows:
.venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate
```

### **3. Install Dependencies**
```bash
# Core dependencies (required)
pip install requests

# For all features (optional):
pip install -r install/requirements.txt

# Or install as package:
pip install -e .
```

### **4. Test It Works**
```bash
# Method 1: Direct run
python run.py

# Method 2: CLI command (if installed as package)
style-transfer-ai
```

---

## 🤖 **AI Model Setup (Choose One)**

### **Option A: Local Models (Free, Private, Recommended)**

1. **Install Ollama**:
   - Go to [ollama.ai](https://ollama.ai/download)
   - Download and install for your OS

2. **Pull Models**:
   ```bash
   # Fast, lightweight model (recommended for testing)
   ollama pull gemma2:2b
   
   # Better quality model (if you have more RAM)
   ollama pull llama3.1:8b
   ```

3. **Start Ollama Server**:
   ```bash
   ollama serve
   ```

### **Option B: Cloud APIs (Paid)**

1. **Get API Keys**:
   - **OpenAI**: [platform.openai.com/api-keys](https://platform.openai.com/api-keys)
   - **Gemini**: [makersuite.google.com/app/apikey](https://makersuite.google.com/app/apikey)

2. **Configure Environment**:
   ```bash
   # Copy template
   cp .env.example .env
   
   # Edit .env and add your API keys
   ```

---

## 🧪 **Test Your Installation**

### **Quick Test**
```bash
# Run the application
python run.py

# Or if installed as package:
style-transfer-ai
```

You should see a menu like:
```
=====================================================
STYLE TRANSFER AI - ADVANCED STYLOMETRY ANALYSIS
=====================================================
Current Model: None (will be selected before analysis)
-----------------------------------------------------
STYLE ANALYSIS:
1. Analyze Writing Style (Complete Analysis)
2. Quick Style Analysis (Statistical Only)
...
```

### **Test with Sample Files**
The app comes with sample text files in `default text/` folder - perfect for testing!

---

## 🔧 **Troubleshooting**

### **Common Issues & Solutions**

**❌ "Python not found"**
- Install Python from [python.org](https://python.org/downloads/)
- Make sure to check "Add to PATH" during installation

**❌ "pip not found"**
- Python 3.7+ includes pip automatically
- Try: `python -m pip` instead of `pip`

**❌ "Module not found"**
- Make sure you're in the project directory
- Try: `pip install -e .` to install in development mode

**❌ "Ollama connection failed"**
- Install Ollama from [ollama.ai](https://ollama.ai/download)
- Run `ollama serve` in a separate terminal
- Pull a model: `ollama pull gemma2:2b`

**❌ "No text files found"**
- Check `default text/` folder exists
- Or use your own .txt files when prompted

---

## 📁 **Project Structure (What You Downloaded)**

```
style-transfer-ai/
├── src/                     # Main application code
├── install/                 # Installation scripts
├── default text/            # Sample text files for testing
├── documentation/           # Detailed guides
├── config/                  # Configuration templates
├── run.py                   # Quick start script
├── setup.py                 # Package installation
└── README.md               # Project overview
```

---

## 🎯 **You're Ready!**

Once installed, you can:
- ✅ Analyze your writing style with 25-point framework
- ✅ Generate content in your style
- ✅ Transfer writing to different styles
- ✅ Save results locally or in cloud (Firestore)
- ✅ Work with virtually any text file format

**Need help?** Check the `documentation/` folder for detailed guides!

---

## 🔗 **Quick Links**

- **Main Repository**: https://github.com/alwynrejicser/style-transfer-ai
- **Issues/Support**: https://github.com/alwynrejicser/style-transfer-ai/issues
- **Ollama Download**: https://ollama.ai/download
- **OpenAI API**: https://platform.openai.com/api-keys
- **Gemini API**: https://makersuite.google.com/app/apikey

**Enjoy analyzing your writing style!** 🎨📝