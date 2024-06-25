import firebase_admin
from firebase_admin import credentials, firestore

# Chatbot Collection Schema Important Fields

#   username: String
#   telegramId: number
#   credits: number

def check_user_auth(user_id, username):
    db = firestore.client()
    users_ref = db.collection("chatbot")
    users = users_ref.stream()
    if not users:
        print("No users found in the database.")
        return False, None

    for user in users:
        user_data = user.to_dict()
        if user_data["telegramId"] == user_id or user_data["username"] == username:
            return True, user_data
    return False, None


def decrement_credits(user_data):
    db = firestore.client()
    doc_ref = db.collection("chatbot").get()
    for doc in doc_ref:
        if (
            doc.to_dict()["username"] == user_data["username"]
            or doc.to_dict()["telegram_id"] == user_data["telegramId"]
        ) and doc.to_dict()["credits"] > 0:
            key = doc.id
            db.collection("chatbot").document(key).update(
                {"credits": firestore.Increment(-1)}
            )
            return True
    return False
