import requests


def download_friends(username):
    host = "https://www.livejournal.com/misc/fdata.bml?user={username}"
    url = host.format(username=username)
    response = requests.get(url)
    return response.text


def clean_data(response):
    response_splitted = response.splitlines()[1:-1]
    response_cleaned = [el[2:] for el in response_splitted]
    return response_cleaned
