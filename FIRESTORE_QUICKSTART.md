# 🔥 Firestore Quick Setup - 5 Minutes

## ⚡ Fast Track Setup

### 1️⃣ Create Firebase Project (2 minutes)
```
1. Go to: https://console.firebase.google.com/
2. Click "Create a project"
3. Enter project name → Continue
4. Disable Google Analytics → Create project
```

### 2️⃣ Enable Firestore (1 minute)
```
1. Left sidebar → "Firestore Database"
2. Click "Create database"
3. Choose "Start in test mode" → Next
4. Select location (us-central1) → Done
```

### 3️⃣ Get Service Key (1 minute)
```
1. Gear icon → Project settings
2. "Service accounts" tab
3. "Generate new private key" → Generate key
4. Save file as "firebase-credentials.json"
```

### 4️⃣ Configure Code (1 minute)
```python
# 1. Copy Project ID from Firebase Console
# 2. In style_analyzer_enhanced.py, update line ~1253:
'projectId': 'your-actual-project-id-here',

# 3. Place firebase-credentials.json in project folder
# 4. Install: pip install firebase-admin
```

## 🎯 File Structure
```
style-transfer-ai/
├── firebase-credentials.json  ← Your downloaded key
├── style_analyzer_enhanced.py ← Update project ID here
└── test_firebase.py          ← Run this to test
```

## ✅ Test Your Setup
```bash
python test_firebase.py
```

**Expected Output**:
```
✅ Firebase initialized successfully!
✅ Successfully queried Firestore
🎉 Firebase Firestore integration test completed!
```

## 🚀 You're Done!
```bash
python style_analyzer_enhanced.py
```

Your profiles will now save locally AND in Firebase Firestore cloud database!

---

**Need help?** Check [FIREBASE_SETUP.md](FIREBASE_SETUP.md) for detailed instructions.