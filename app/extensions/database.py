from firebase_admin import credentials, firestore, initialize_app

def _initialize_db():
    cred = credentials.Certificate('app/extensions/key.json')
    default_app = initialize_app(cred)
    db = firestore.client()