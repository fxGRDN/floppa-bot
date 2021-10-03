import requests
from dotenv import load_dotenv
from os import environ
from random import randint

load_dotenv()
CLIENT_ID = environ.get("CLIENT_ID")


def getAllImgs():
    url = "https://api.imgur.com/3/album/9vusFxT"

    h = {
        'Authorization': 'Client-ID ' + CLIENT_ID
    }

    r = requests.request("GET", url, headers=h)

    imgIDs = []

    rJSON = r.json()

    for link in rJSON['data']['images']:
        imgIDs.append(link['id'])

    return imgIDs


def getRandImg():
    links = getAllImgs()

    rand = links[randint(0, len(links)-1)]

    imglink = 'https://imgur.com/'+rand

    return imglink





