from datetime import datetime
import requests

PIXELA_URL = "https://pixe.la/v1/users"
TOKEN = "asdfjkl836vbnm"
USERNAME = "shreyasjain"
NAME = "Shreyas Jain"
PIXELA_GRAPH_URL = f"{PIXELA_URL}/{USERNAME}/graphs"

graph_headers = {
    "X-USER-TOKEN": TOKEN
}


def create_user():
    create_params = {
        "token": TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": 'yes',
        "notMinor": 'yes',
    }

    response = requests.post(url=PIXELA_URL, json=create_params)
    response.raise_for_status()


def create_graph():
    graph_params = {
        "id": USERNAME,
        "name": NAME,
        "unit": "minute",
        "type": "int",
        "color": "shibafu",
    }

    response = requests.post(url=PIXELA_GRAPH_URL, headers=graph_headers, json=graph_params)
    response.raise_for_status()
    print(response.text)


def update_graph():
    requests.put(f"{PIXELA_GRAPH_URL}/{USERNAME}", headers=graph_headers, json={"name": "Study Time"})


def create_pixel():
    date = datetime.now().strftime(format('%Y%m%d'))

    pixel_params = {
        "date": str(date),
        "quantity": "15"
    }

    response = requests.post(f"{PIXELA_GRAPH_URL}/{USERNAME}", headers=graph_headers, json=pixel_params)
    response.raise_for_status()


def update_pixel():
    date = str(datetime(2026, 9, 9).strftime(format('%Y%m%d')))
    print(date)
    update_params = {
        "quantity": '60'
    }

    response = requests.put(f"{PIXELA_GRAPH_URL}/{USERNAME}/{date}", headers=graph_headers, json=update_params)
    response.raise_for_status()

def delete_pixel():
    date = str(datetime(2026, 9, 10).strftime(format('%Y%m%d')))
    response = requests.delete(f"{PIXELA_GRAPH_URL}/{USERNAME}/{date}", headers=graph_headers)
    response.raise_for_status()

# create_user()
# create_graph()
# update_graph()
# create_pixel()
# update_pixel()
delete_pixel()