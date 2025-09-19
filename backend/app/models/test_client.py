# test_client.py
import requests

while True:
    user_msg = input("You: ")
    if user_msg.lower() in ["quit", "exit"]:
        break

    res = requests.post(
        "http://127.0.0.1:8000/chat",
        json={"message": user_msg}
    )
    print("Therapist:", res.json()["reply"])
