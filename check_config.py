"""
Configuration checker for Style Transfer AI.
Helps new users identify what needs to be set up.
"""

import os
import sys
from src.config.settings import *

def check_firebase_setup():
    """Check Firebase configuration status."""
    print("🔥 Firebase Configuration:")
    
    # Check credentials file
    if os.path.exists(FIREBASE_CREDENTIALS_PATH):
        print(f"   ✅ Credentials file found: {FIREBASE_CREDENTIALS_PATH}")
        
        # Check if it's the example file
        try:
            with open(FIREBASE_CREDENTIALS_PATH, 'r') as f:
                content = f.read()
                if "your-project-id" in content:
                    print("   ⚠️  Using example template - needs real credentials")
                    return False
                else:
                    print(f"   ✅ Project ID configured: {FIREBASE_PROJECT_ID}")
                    return True
        except Exception as e:
            print(f"   ❌ Error reading credentials: {e}")
            return False
    else:
        print(f"   ❌ Credentials file missing: {FIREBASE_CREDENTIALS_PATH}")
        print("   💡 Copy config/firebase-credentials.json.example and configure it")
        return False

def check_api_keys():
    """Check API key configuration."""
    print("\n🤖 AI Model Configuration:")
    
    keys_configured = 0
    
    # OpenAI
    if OPENAI_API_KEY and OPENAI_API_KEY != "your-openai-api-key-here":
        print("   ✅ OpenAI API key configured")
        keys_configured += 1
    else:
        print("   ⚠️  OpenAI API key not configured")
    
    # Gemini
    if GEMINI_API_KEY and GEMINI_API_KEY != "your-gemini-api-key-here":
        print("   ✅ Gemini API key configured")
        keys_configured += 1
    else:
        print("   ⚠️  Gemini API key not configured")
    
    # Ollama check
    try:
        import requests
        response = requests.get(f"{OLLAMA_BASE_URL}/api/tags", timeout=2)
        if response.status_code == 200:
            models = response.json().get('models', [])
            print(f"   ✅ Ollama running with {len(models)} models")
            keys_configured += 1
        else:
            print("   ⚠️  Ollama not responding")
    except:
        print("   ⚠️  Ollama not available")
    
    return keys_configured > 0

def check_dependencies():
    """Check optional dependencies."""
    print("\n📦 Dependencies:")
    
    deps = {
        'requests': 'Basic HTTP requests',
        'firebase_admin': 'Firebase/Firestore integration', 
        'openai': 'OpenAI API integration',
        'google.generativeai': 'Google Gemini integration'
    }
    
    available = 0
    for dep, description in deps.items():
        try:
            __import__(dep)
            print(f"   ✅ {dep}: {description}")
            available += 1
        except ImportError:
            print(f"   ⚠️  {dep}: {description} (optional)")
    
    return available

def main():
    """Run configuration check."""
    print("=" * 60)
    print("🔧 STYLE TRANSFER AI - CONFIGURATION CHECKER")
    print("=" * 60)
    
    firebase_ok = check_firebase_setup()
    models_ok = check_api_keys()
    deps_available = check_dependencies()
    
    print("\n" + "=" * 60)
    print("📊 SUMMARY:")
    print("=" * 60)
    
    if firebase_ok:
        print("✅ Cloud storage (Firebase): Ready")
    else:
        print("⚠️  Cloud storage (Firebase): Not configured (local storage only)")
    
    if models_ok:
        print("✅ AI models: At least one available")
    else:
        print("❌ AI models: None configured - setup required")
    
    print(f"📦 Dependencies: {deps_available}/4 optional packages available")
    
    print("\n💡 RECOMMENDATIONS:")
    
    if not models_ok:
        print("🚨 CRITICAL: Set up at least one AI model:")
        print("   • Install Ollama: https://ollama.ai/download")
        print("   • Or get OpenAI API key: https://platform.openai.com/api-keys")
        print("   • Or get Gemini API key: https://makersuite.google.com/app/apikey")
    
    if not firebase_ok:
        print("🔥 For cloud storage:")
        print("   • See SETUP.md for Firebase configuration")
        print("   • Or continue with local storage only")
    
    if deps_available < 2:
        print("📦 Install optional dependencies:")
        print("   pip install firebase-admin openai google-generativeai")
    
    print(f"\n🚀 Ready to run: python run.py")
    
    return firebase_ok and models_ok

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)