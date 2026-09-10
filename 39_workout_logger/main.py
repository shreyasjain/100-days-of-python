from datetime import datetime

import requests

API_KEY = "nix_live_Yjs6KDdSnhPfq1PyAD5J7Lh7sW8FdKn1"
APP_ID = "app_83238a871adb43ad96c7a2f5"
BASE_URL = "https://app.100daysofpython.dev"
SHEET_URL = "https://api.sheety.co/8ab15ae450c2cce61400248e3537dcea/myWorkoutsApp/sheet1"
SHEET_AUTH = "c2hyZXlhczpzaHJleWFz"

api_headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
    'Content-Type': 'application/json'
}

sheet_headers = {
    "Authorization": f"Basic {SHEET_AUTH}"
}


def add_row(body):
    print(body)
    response = requests.post(SHEET_URL, headers=sheet_headers, json=body)
    response.raise_for_status()
    print(response.text)


def log_activity(activity):
    body = {
        'query': activity
    }
    response = requests.post(f"{BASE_URL}/v1/nutrition/natural/exercise", headers=api_headers, json=body)
    response.raise_for_status()
    data = response.json()['exercises']
    for d in data:
        body = {
            "sheet1": {
                "date": str(datetime.now().date()),
                'time': str(datetime.now().time()),
                "exercise": d["name"],
                "duration": d["duration_min"],
                "calories": d["nf_calories"]
            }}
        add_row(body)


activity = input("Tell me which exercise you did?")
log_activity(activity)
