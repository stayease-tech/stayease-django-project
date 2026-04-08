# test_new_refresh.py
import requests
import os
from dotenv import load_dotenv

load_dotenv()

response = requests.post(
    "https://accounts.zoho.in/oauth/v2/token",
    data={
        "refresh_token": os.getenv("ZOHO_REFRESH_TOKEN"),
        "client_id": os.getenv("ZOHO_CLIENT_ID"),
        "client_secret": os.getenv("ZOHO_CLIENT_SECRET"),
        "grant_type": "refresh_token"
    },
    headers={
        "Content-Type": "application/x-www-form-urlencoded"
    }
)

print(f"Status: {response.status_code}")
print(f"Response: {response.text}")

if response.status_code == 200 and "access_token" in response.text:
    print("\n✅ SUCCESS! Your Zoho integration is ready!")
    print("Restart your Django server and try uploading again.")
else:
    print("\n❌ Still having issues.")