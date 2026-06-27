import requests
from datetime import datetime

URL = "https://tevetvault.netlify.app/"

try:
    response = requests.get(URL, timeout=30)
    print(f"[{datetime.now()}] SUCCESS - Status Code: {response.status_code}")
except Exception as e:
    print(f"[{datetime.now()}] ERROR - {e}")
