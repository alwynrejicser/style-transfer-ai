"""
Firestore cloud storage module for Style Transfer AI.
Handles Firebase initialization and Firestore operations.
"""

from datetime import datetime
from ..config.settings import FIREBASE_PROJECT_ID, FIREBASE_CREDENTIALS_PATH, FIRESTORE_COLLECTION
from ..utils.formatters import format_human_readable_output
from ..utils.text_processing import sanitize_filename

# Global Firebase database client
db = None
FIREBASE_AVAILABLE = False

try:
    import firebase_admin
    from firebase_admin import credentials, firestore
    FIREBASE_AVAILABLE = True
except ImportError:
    print("WARNING: Firebase Admin SDK not installed. Install with: pip install firebase-admin")


def initialize_firebase():
    """Initialize Firebase Admin SDK and Firestore client."""
    global db, FIREBASE_AVAILABLE
    
    if not FIREBASE_AVAILABLE:
        print("📦 Firebase Admin SDK not installed.")
        print("💡 To enable cloud storage: pip install firebase-admin")
        return False
    
    if db is not None:
        return True  # Already initialized
    
    # Check if credentials file exists
    import os
    if not os.path.exists(FIREBASE_CREDENTIALS_PATH):
        print(f"🔥 Firebase credentials not found at: {FIREBASE_CREDENTIALS_PATH}")
        print("💡 To set up cloud storage:")
        print("   1. Copy config/firebase-credentials.json.example to config/firebase-credentials.json")
        print("   2. Replace with your actual Firebase credentials")
        print("   3. See SETUP.md for detailed instructions")
        print("📁 Continuing with local storage only...")
        return False
    
    try:
        # Check if Firebase app is already initialized
        try:
            app = firebase_admin.get_app()
        except ValueError:
            # Initialize Firebase app
            cred = credentials.Certificate(FIREBASE_CREDENTIALS_PATH)
            firebase_admin.initialize_app(cred, {
                'projectId': FIREBASE_PROJECT_ID,
            })
        
        # Initialize Firestore client
        db = firestore.client()
        print("🔥 Firebase Firestore initialized successfully")
        return True
        
    except Exception as e:
        print(f"❌ Firebase initialization failed: {e}")
        print("💡 Check your Firebase configuration:")
        print(f"   - Credentials file: {FIREBASE_CREDENTIALS_PATH}")
        print(f"   - Project ID: {FIREBASE_PROJECT_ID}")
        print("   - See config/README.md for setup help")
        print("📁 Continuing with local storage only...")
        return False


def save_to_firestore(style_profile):
    """
    Save style profile to Firestore cloud database.
    
    Args:
        style_profile (dict): The complete style profile data
        
    Returns:
        dict: Save result with success status and document name
    """
    global db
    
    if not db:
        return {
            'success': False,
            'error': 'Firestore not initialized'
        }
    
    try:
        # Extract user name for document naming
        user_name = "Anonymous_User"
        if 'user_profile' in style_profile and 'name' in style_profile['user_profile']:
            user_name = sanitize_filename(style_profile['user_profile']['name'])
        
        # Prepare data for Firestore
        firestore_document_data = style_profile.copy()
        firestore_document_data['human_readable_report'] = format_human_readable_output(style_profile)
        firestore_document_data['timestamp'] = datetime.now().strftime("%Y%m%d_%H%M%S")
        firestore_document_data['created_at'] = datetime.now()
        
        # Create user-specific document name
        firestore_doc_name = f"{user_name}_profile_{firestore_document_data['timestamp']}"
        
        # Add document to Firestore
        doc_ref = db.collection(FIRESTORE_COLLECTION).document(firestore_doc_name)
        doc_ref.set(firestore_document_data)
        
        return {
            'success': True,
            'firestore_doc_name': firestore_doc_name,
            'message': f"Profile stored in Cloud Firestore with user-specific name: {firestore_doc_name}"
        }
        
    except Exception as e:
        return {
            'success': False,
            'error': f"Error storing profile in Firestore: {e}"
        }


def list_firestore_profiles(user_name=None, limit=50):
    """
    List profiles stored in Firestore.
    
    Args:
        user_name (str): Filter by user name (optional)
        limit (int): Maximum number of profiles to return
        
    Returns:
        list: List of profile documents with metadata
    """
    global db
    
    if not db:
        return []
    
    try:
        query = db.collection(FIRESTORE_COLLECTION)
        
        if user_name:
            sanitized_name = sanitize_filename(user_name)
            query = query.where('user_profile.name', '==', user_name)
        
        query = query.order_by('created_at', direction=firestore.Query.DESCENDING).limit(limit)
        
        docs = query.stream()
        profiles = []
        
        for doc in docs:
            data = doc.to_dict()
            profiles.append({
                'id': doc.id,
                'user_name': data.get('user_profile', {}).get('name', 'Unknown'),
                'created_at': data.get('created_at'),
                'analysis_date': data.get('metadata', {}).get('analysis_date', 'Unknown'),
                'file_count': data.get('metadata', {}).get('total_samples', 0),
                'model_used': data.get('metadata', {}).get('model_used', 'Unknown')
            })
        
        return profiles
        
    except Exception as e:
        print(f"Error listing Firestore profiles: {e}")
        return []


def get_firestore_profile(document_id):
    """
    Retrieve a specific profile from Firestore.
    
    Args:
        document_id (str): Firestore document ID
        
    Returns:
        dict: Profile data or error information
    """
    global db
    
    if not db:
        return {
            'success': False,
            'error': 'Firestore not initialized'
        }
    
    try:
        doc_ref = db.collection(FIRESTORE_COLLECTION).document(document_id)
        doc = doc_ref.get()
        
        if doc.exists:
            return {
                'success': True,
                'profile': doc.to_dict(),
                'message': f"Profile retrieved: {document_id}"
            }
        else:
            return {
                'success': False,
                'error': f"Profile not found: {document_id}"
            }
            
    except Exception as e:
        return {
            'success': False,
            'error': f"Error retrieving profile {document_id}: {e}"
        }


def delete_firestore_profile(document_id):
    """
    Delete a profile from Firestore.
    
    Args:
        document_id (str): Firestore document ID
        
    Returns:
        dict: Delete result with success status
    """
    global db
    
    if not db:
        return {
            'success': False,
            'error': 'Firestore not initialized'
        }
    
    try:
        doc_ref = db.collection(FIRESTORE_COLLECTION).document(document_id)
        doc_ref.delete()
        
        return {
            'success': True,
            'message': f"Profile deleted: {document_id}"
        }
        
    except Exception as e:
        return {
            'success': False,
            'error': f"Error deleting profile {document_id}: {e}"
        }


def manage_firestore_data_retention():
    """Interactive Firestore data retention management."""
    global db
    
    if not db:
        print("Firestore not available. Please check your Firebase configuration.")
        return
    
    while True:
        print("\n" + "="*50)
        print("FIRESTORE DATA RETENTION MANAGEMENT")
        print("="*50)
        print("1. List all stored profiles")
        print("2. View specific profile")
        print("3. Delete specific profile")
        print("4. Delete profiles by user name")
        print("0. Return to main menu")
        print("="*50)
        
        try:
            choice = input("\nEnter your choice (0-4): ").strip()
            
            if choice == "0":
                break
            elif choice == "1":
                profiles = list_firestore_profiles()
                if profiles:
                    print(f"\nFound {len(profiles)} profiles:")
                    print("-" * 70)
                    for i, profile in enumerate(profiles, 1):
                        print(f"{i:2d}. {profile['user_name']} | {profile['analysis_date']} | {profile['model_used']} | ID: {profile['id']}")
                else:
                    print("\nNo profiles found in Firestore.")
                    
            elif choice == "2":
                doc_id = input("Enter profile document ID: ").strip()
                if doc_id:
                    result = get_firestore_profile(doc_id)
                    if result['success']:
                        profile = result['profile']
                        print(f"\nProfile: {profile.get('user_profile', {}).get('name', 'Unknown')}")
                        print(f"Analysis Date: {profile.get('metadata', {}).get('analysis_date', 'Unknown')}")
                        print(f"Model Used: {profile.get('metadata', {}).get('model_used', 'Unknown')}")
                        print(f"Files Analyzed: {profile.get('metadata', {}).get('total_samples', 0)}")
                    else:
                        print(f"Error: {result['error']}")
                        
            elif choice == "3":
                doc_id = input("Enter profile document ID to delete: ").strip()
                if doc_id:
                    confirm = input(f"Are you sure you want to delete profile '{doc_id}'? (y/n): ").strip().lower()
                    if confirm == 'y':
                        result = delete_firestore_profile(doc_id)
                        if result['success']:
                            print(f"SUCCESS: {result['message']}")
                        else:
                            print(f"ERROR: {result['error']}")
                            
            elif choice == "4":
                user_name = input("Enter user name to delete profiles for: ").strip()
                if user_name:
                    profiles = list_firestore_profiles(user_name)
                    if profiles:
                        print(f"\nFound {len(profiles)} profiles for user '{user_name}':")
                        for profile in profiles:
                            print(f"- {profile['id']} | {profile['analysis_date']}")
                        
                        confirm = input(f"Delete all {len(profiles)} profiles for '{user_name}'? (y/n): ").strip().lower()
                        if confirm == 'y':
                            deleted_count = 0
                            for profile in profiles:
                                result = delete_firestore_profile(profile['id'])
                                if result['success']:
                                    deleted_count += 1
                            print(f"SUCCESS: Deleted {deleted_count} profiles for '{user_name}'")
                    else:
                        print(f"No profiles found for user '{user_name}'")
                        
            else:
                print("Invalid choice. Please enter 0-4.")
                
        except KeyboardInterrupt:
            print("\n\nReturning to main menu...")
            break
        except Exception as e:
            print(f"Error: {e}")