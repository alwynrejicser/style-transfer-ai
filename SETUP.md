# 🚀 Style Transfer AI - Quick Start Guide

## 📥 **First Time Setup**

Welcome! You've downloaded Style Transfer AI. Follow these steps to get cloud storage working:

### **🔥 Firebase Setup (Optional - for Cloud Storage)**

#### **Option A: Use Your Own Firebase Project (Recommended)**

1. **Create a Firebase Project**:
   - Go to [Firebase Console](https://console.firebase.google.com/)
   - Click "Add Project" or "Create a project"
   - Name it anything you want (e.g., "my-style-transfer")
   - Enable Firestore Database

2. **Get Your Admin SDK Key**:
   - Go to Project Settings → Service Accounts
   - Click "Generate New Private Key"
   - Download the JSON file

3. **Configure the Application**:
   ```bash
   # Copy the template
   cp config/firebase-credentials.json.example config/firebase-credentials.json
   
   # Replace the content with your downloaded JSON file
   # Update src/config/settings.py with your project ID
   ```

#### **Option B: Skip Cloud Storage**
If you don't want cloud storage, the app works perfectly with local storage only!

### **🤖 AI Model Setup**

#### **Local Models (Recommended - Free & Private)**
```bash
# Install Ollama
# Visit: https://ollama.ai/download

# Pull recommended models
ollama pull gemma2:2b      # Fast model
ollama pull llama3.1:8b    # Better quality
```

#### **API Models (Optional)**
- **OpenAI**: Get API key from [OpenAI Platform](https://platform.openai.com/api-keys)
- **Gemini**: Get API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

### **⚙️ Configuration**

1. **Copy Environment Template**:
   ```bash
   cp .env.example .env
   ```

2. **Edit .env with your values**:
   ```bash
   # Firebase (if using cloud storage)
   FIREBASE_PROJECT_ID=your-project-id
   
   # API Keys (if using API models)
   OPENAI_API_KEY=your-openai-key
   GEMINI_API_KEY=your-gemini-key
   ```

### **🎯 Quick Start Commands**

```bash
# Install dependencies
pip install -r install/requirements.txt

# Run the application
python run.py

# Or install as package
pip install -e .
style-transfer-ai
```

### **✅ What Works Without Setup**

- ✅ **Local file storage** (always works)
- ✅ **Statistical analysis** (no AI needed)
- ✅ **Local Ollama models** (if installed)

### **🔧 What Needs Configuration**

- 🔧 **Cloud storage** (requires Firebase setup)
- 🔧 **OpenAI/Gemini models** (requires API keys)
- 🔧 **GitHub uploads** (requires GitHub token)

### **🆘 Need Help?**

Check the documentation in:
- `config/README.md` - Firebase setup details
- `documentation/` - Advanced configuration
- GitHub Issues - Report problems

**The app will guide you through model selection on first run!**