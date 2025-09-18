# Firebase Setup Guide

## 🔥 Firebase Admin SDK Configuration

### **Step 1: Get Your Firebase Admin SDK Key**

1. Go to [Firebase Console](https://console.firebase.google.com/)
2. Select your project (`styler-24736`)
3. Navigate to **Project Settings** → **Service Accounts**
4. Click **"Generate New Private Key"**
5. Download the JSON file

### **Step 2: Store the Credentials Securely**

1. **Rename** the downloaded file to `firebase-credentials.json`
2. **Move** it to the `config/` directory:
   ```
   style-transfer-ai/
   └── config/
       └── firebase-credentials.json  ← Place file here
   ```

### **Step 3: Verify Configuration**

The application will automatically detect the credentials at:
```
config/firebase-credentials.json
```

### **🔒 Security Best Practices**

✅ **DO:**
- Store credentials in the `config/` directory
- Use the standard filename `firebase-credentials.json`
- Ensure the file is listed in `.gitignore`
- Set appropriate file permissions (read-only for your user)

❌ **DON'T:**
- Commit credentials to version control
- Share the credentials file publicly
- Hardcode credentials in source code
- Store credentials in the root directory

### **🌍 Environment Variables (Alternative)**

For production deployments, consider using environment variables:

```bash
export GOOGLE_APPLICATION_CREDENTIALS="path/to/firebase-credentials.json"
export FIREBASE_PROJECT_ID="styler-24736"
```

### **🧪 Testing the Setup**

Run the application to test Firebase integration:
```bash
python run.py
# Select menu option 4: "Manage Cloud Data (Firestore)"
```

### **🔧 Troubleshooting**

**Error: "Firebase initialization failed"**
- Verify the JSON file is in `config/firebase-credentials.json`
- Check that the file contains valid JSON
- Ensure your Firebase project ID matches the configuration

**Error: "Permission denied"**
- Verify the service account has Firestore permissions
- Check that the project ID is correct
- Ensure the credentials file hasn't expired

### **📁 Directory Structure**

```
style-transfer-ai/
├── config/
│   ├── firebase-credentials.json      ← Your actual credentials
│   └── firebase-credentials.json.example ← Template file
├── src/
│   └── config/
│       └── settings.py               ← Configuration points here
└── .gitignore                        ← Protects credentials
```