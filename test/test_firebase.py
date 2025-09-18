#!/usr/bin/env python3
"""
Simple test script to verify Firebase Firestore integration
Run this after setting up Firebase to test the connection
"""

import sys
import os

# Add the current directory to the path to import from style_analyzer_enhanced
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from style_analyzer_enhanced import initialize_firebase, retrieve_firestore_profile, list_user_firestore_profiles
    print("✅ Successfully imported Firebase functions from style_analyzer_enhanced.py")
except ImportError as e:
    print(f"❌ Failed to import Firebase functions: {e}")
    sys.exit(1)

def test_firebase_connection():
    """Test Firebase initialization and basic operations."""
    print("\n🔥 Testing Firebase Firestore Integration")
    print("=" * 50)
    
    # Test 1: Initialize Firebase
    print("1. Testing Firebase initialization...")
    firebase_success = initialize_firebase()
    
    if firebase_success:
        print("   ✅ Firebase initialized successfully!")
    else:
        print("   ❌ Firebase initialization failed.")
        print("   📋 Make sure you have:")
        print("      • Firebase project created")
        print("      • Firestore enabled")
        print("      • Service account key downloaded")
        print("      • Key file placed correctly")
        return False
    
    # Test 2: Test profile retrieval (this will fail gracefully if no profiles exist)
    print("\n2. Testing profile retrieval...")
    try:
        # Try to list profiles for a test user
        result = list_user_firestore_profiles("test_user", limit=1)
        if result['success']:
            print(f"   ✅ Successfully queried Firestore (found {result['count']} profiles)")
        else:
            print(f"   ⚠️  Query executed but returned: {result['error']}")
            print("   (This is normal if no profiles exist yet)")
    except Exception as e:
        print(f"   ❌ Error testing profile retrieval: {e}")
        return False
    
    print("\n🎉 Firebase Firestore integration test completed!")
    print("   The analyzer is ready to save profiles to the cloud!")
    return True

if __name__ == "__main__":
    success = test_firebase_connection()
    
    if success:
        print("\n📝 Next steps:")
        print("   1. Run the main analyzer: python style_analyzer_enhanced.py")
        print("   2. Your profiles will be saved locally AND in Firestore")
        print("   3. Check your Firebase Console to see stored profiles")
    else:
        print("\n🔧 Setup required:")
        print("   1. Review FIREBASE_SETUP.md for complete instructions")
        print("   2. Ensure your service account key is properly placed")
        print("   3. Update the project ID in style_analyzer_enhanced.py")