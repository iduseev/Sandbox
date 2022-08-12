#!/bin/python3

from typing import Dict

import requests

HOST = "https://catfact.ninja"
JWT = "OLnYWHn1yWqXyvQzEHECzhmpm3XPRznbJWnx4iyM"
URLS = {
    "fact_by_length": f"{HOST}/facts",
}


def get_cat_fact_by_length(max_length: int, session: requests.Session = None) -> Dict:

    if session is None:
        session = requests.Session()

    headers = {
        "accept": "application/json",
        "X-CSRF-TOKEN": f"{JWT}",
    }

    params = {
        'max_length': f'{max_length}',
    }
    response = session.get(url=URLS["fact_by_length"], params=params, headers=headers, timeout=5)
    return response.json()
