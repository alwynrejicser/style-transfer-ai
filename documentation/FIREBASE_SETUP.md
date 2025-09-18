# Firebase Firestore Setup Guide

## Step-by-Step Firestore Database Creation

### Step 1: Create a Firebase Project

1. **Go to Firebase Console**
   - Open your web browser and navigate to [https://console.firebase.google.com/](https://console.firebase.google.com/)
   - Sign in with your Google account

2. **Create a New Project**
   - Click the **"Create a project"** button (or **"Add project"** if you have existing projects)
   - Enter a project name (e.g., "style-transfer-ai" or "my-stylometry-app")
   - Click **"Continue"**

3. **Configure Google Analytics (Optional)**
   - Choose whether to enable Google Analytics for your project
   - For this application, you can **disable it** or leave it enabled
   - Click **"Continue"** or **"Create project"**

4. **Wait for Project Creation**
   - Firebase will set up your project (this takes a few moments)
   - Click **"Continue"** when the setup is complete

### Step 2: Enable Firestore Database

1. **Navigate to Firestore Database**
   - In your Firebase project dashboard, look for the left sidebar
   - Click on **"Firestore Database"** (it has a database icon)

2. **Create Database**
   - Click the **"Create database"** button
   - You'll see a modal dialog with two options

3. **Choose Security Rules Mode**
   
   **Option A: Start in test mode (Recommended for development)**
   - Select **"Start in test mode"**
   - This allows read/write access for 30 days (good for development)
   - Click **"Next"**
   
   **Option B: Start in production mode**
   - Select **"Start in production mode"**
   - This denies all reads/writes by default (requires authentication setup)
   - Click **"Next"**

4. **Choose Database Location**
   - Select a location closest to your users (e.g., "us-central1", "europe-west1")
   - **Important**: This cannot be changed later
   - Click **"Done"**

5. **Database Creation Complete**
   - Firestore will create your database
   - You'll see the Firestore console with an empty database

### Step 3: Get Your Project Configuration

1. **Find Your Project ID**
   - In the Firebase console, click the gear icon (⚙️) next to "Project Overview"
   - Select **"Project settings"**
   - Note down your **Project ID** (you'll need this for the code)

2. **Generate Service Account Key**
   - Still in Project Settings, click on the **"Service accounts"** tab
   - Click **"Generate new private key"**
   - A dialog will appear warning about keeping the key secure
   - Click **"Generate key"**
   - A JSON file will download automatically
   - **IMPORTANT**: Save this file securely and never share it publicly

### Step 4: Configure Your Local Environment

1. **Place the Service Account Key**
   
   **Option A: Project Directory (Recommended)**
   ```
   d:\CodeSpace\PROJECT\style-transfer-ai\
   ├── firebase-credentials.json  ← Place your downloaded JSON file here
   ├── style_analyzer_enhanced.py
   └── ...
   ```
   
   **Option B: Custom Location with Environment Variable**
   ```bash
   # Windows PowerShell
   $env:FIREBASE_CREDENTIALS_PATH = "C:\path\to\your\serviceAccountKey.json"
   
   # Windows Command Prompt
   set FIREBASE_CREDENTIALS_PATH=C:\path\to\your\serviceAccountKey.json
   
   # Linux/Mac Terminal
   export FIREBASE_CREDENTIALS_PATH=/path/to/your/serviceAccountKey.json
   ```

2. **Update Project ID in Code**
   - Open `style_analyzer_enhanced.py`
   - Find this line (around line 1253):
   ```python
   'projectId': 'styler-24736',  # User should update this with their project ID
   ```
   - Replace `'styler-24736'` with your actual Project ID from Step 3.1

### Step 5: Install Required Dependencies

```bash
# Install Firebase Admin SDK
pip install firebase-admin

# Or install all dependencies at once
pip install -r requirements.txt
```

### Step 6: Test Your Setup

1. **Run the Test Script**
   ```bash
   python test_firebase.py
   ```

2. **Expected Output (Success)**
   ```
   🔥 Testing Firebase Firestore Integration
   ==================================================
   1. Testing Firebase initialization...
      ✅ Firebase initialized successfully!
   
   2. Testing profile retrieval...
      ✅ Successfully queried Firestore (found 0 profiles)
   
   🎉 Firebase Firestore integration test completed!
   ```

3. **If You See Errors**
   - Check that the JSON key file is in the correct location
   - Verify the Project ID is correct in the code
   - Ensure Firestore is enabled in your Firebase project

### Step 7: Run the Style Analyzer

```bash
python style_analyzer_enhanced.py
```

Now your profiles will be saved both locally AND in your Firestore database!

## Installation

1. **Install Firebase Admin SDK**
   ```bash
   pip install firebase-admin
   ```

2. **Place Your Service Account Key**
   
   Option A: Place the JSON file in your project directory with one of these names:
   - `firebase-credentials.json`
   - `serviceAccountKey.json`
   
   Option B: Set an environment variable:
   ```bash
   # Windows
   set FIREBASE_CREDENTIALS_PATH=C:\path\to\your\serviceAccountKey.json
   
   # Linux/Mac
   export FIREBASE_CREDENTIALS_PATH=/path/to/your/serviceAccountKey.json
   ```

3. **Update Project ID**
   - Open `style_analyzer_enhanced.py`
   - Find the line: `'projectId': 'styler-24736'`
   - Replace `'styler-24736'` with your actual Firebase project ID

## Firestore Database Structure

The analyzer stores data in the `stylometry_reports` collection with this structure:

```json
{
  "user_profile": {
    "name": "John_Doe",
    "native_language": "English",
    "education_level": "Bachelor's"
  },
  "metadata": {
    "analysis_date": "2025-01-15T10:30:00",
    "total_samples": 3,
    "combined_text_length": 1245
  },
  "text_statistics": {
    "word_count": 1245,
    "lexical_diversity": 0.847
  },
  "human_readable_report": "Full text report...",
  "created_at": "2025-01-15T10:30:00Z",
  "timestamp": "20250115_103000"
}
```

## Security Best Practices

1. **Never commit service account keys to version control**
2. **Use environment variables in production**
3. **Set up proper Firestore security rules**
4. **Regularly rotate service account keys**
5. **Monitor usage in Firebase Console**

## Firestore Security Rules (Production)

Replace the default rules with:

```javascript
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /stylometry_reports/{reportId} {
      allow read, write: if request.auth != null;
    }
  }
}
```

## Cost Information

- Firebase Spark plan includes generous free tier
- Firestore free tier: 50K reads, 20K writes, 20K deletes per day
- Storage: 1 GiB free
- Check [Firebase Pricing](https://firebase.google.com/pricing) for current limits

## Troubleshooting Common Issues

### ❌ "Firebase service account key not found"

**Problem**: The analyzer can't find your service account JSON file.

**Solutions**:
1. **Check file location**:
   ```
   # Make sure your file is here:
   d:\CodeSpace\PROJECT\style-transfer-ai\firebase-credentials.json
   ```

2. **Check file name**: Must be exactly one of these:
   - `firebase-credentials.json`
   - `serviceAccountKey.json`

3. **Set environment variable**:
   ```powershell
   # PowerShell
   $env:FIREBASE_CREDENTIALS_PATH = "C:\full\path\to\your\file.json"
   ```

### ❌ "Permission denied" or "7 PERMISSION_DENIED"

**Problem**: Firestore security rules are blocking access.

**Solutions**:
1. **Check security rules in Firebase Console**:
   - Go to Firestore Database → Rules
   - For testing, use:
   ```javascript
   rules_version = '2';
   service cloud.firestore {
     match /databases/{database}/documents {
       match /{document=**} {
         allow read, write: if true;
       }
     }
   }
   ```

2. **Ensure you're in test mode**:
   - If you started in production mode, switch to test mode or set up authentication

### ❌ "Project not found" or "Invalid project ID"

**Problem**: Wrong project ID in the code.

**Solutions**:
1. **Get correct Project ID**:
   - Go to Firebase Console → Project Settings
   - Copy the "Project ID" (not "Project name")

2. **Update the code**:
   ```python
   # In style_analyzer_enhanced.py, find and update:
   'projectId': 'your-actual-project-id-here',
   ```

### ❌ "Module 'firebase_admin' not found"

**Problem**: Firebase Admin SDK not installed.

**Solution**:
```bash
pip install firebase-admin
```

### ❌ "Firestore database does not exist"

**Problem**: Firestore database wasn't created properly.

**Solutions**:
1. **Go back to Firebase Console**
2. **Navigate to Firestore Database**
3. **If you see "Get started", click it and create the database**
4. **Make sure you complete the database creation process**

### ❌ Test script shows "Query executed but returned: error"

**This is normal!** It means:
- ✅ Firebase connection is working
- ✅ Authentication is successful
- ℹ️ No profiles exist yet (which is expected for new setups)

## Quick Verification Checklist

Before running the analyzer, verify:

- [ ] Firebase project created
- [ ] Firestore database enabled
- [ ] Service account key downloaded
- [ ] JSON file placed in correct location
- [ ] Project ID updated in code
- [ ] `firebase-admin` package installed
- [ ] Test script runs without errors

## Firebase Console Navigation Help

1. **Firebase Console URL**: https://console.firebase.google.com/
2. **Project Dashboard**: Shows overview of your project
3. **Firestore Database**: Left sidebar → "Firestore Database"
4. **Project Settings**: Gear icon (⚙️) → "Project settings"
5. **Service Accounts**: Project Settings → "Service accounts" tab

## Security Notes for Production

When you're ready to deploy or share your app:

1. **Update Firestore Rules**:
   ```javascript
   rules_version = '2';
   service cloud.firestore {
     match /databases/{database}/documents {
       match /stylometry_reports/{reportId} {
         allow read, write: if request.auth != null;
       }
     }
   }
   ```

2. **Set up Authentication** (if needed):
   - Go to Authentication in Firebase Console
   - Enable sign-in methods
   - Implement user authentication in your app

3. **Use Environment Variables**:
   ```bash
   # Don't hardcode project ID, use environment variables
   FIREBASE_PROJECT_ID=your-project-id
   FIREBASE_CREDENTIALS_PATH=/path/to/credentials.json
   ```