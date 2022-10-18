#!/bin/python3

from typing import Dict, Any, Optional, AnyStr, Union
import requests

HOST = "https://catfact.ninja"
JWT = "OLnYWHn1yWqXyvQzEHECzhmpm3XPRznbJWnx4iyM"
URLS = {
    "fact_by_length": f"{HOST}/facts",
}


def get_cat_fact_by_length(
    max_length: int, 
    url: AnyStr = URLS["fact_by_length"],
    jwt: AnyStr = JWT,
    session: requests.Session = None, 
    logger: Optional[Any] = None
) -> Dict:

    if session is None:
        session = requests.Session()

    headers = {
        "accept": "application/json",
        "X-CSRF-TOKEN": f"{jwt}",
    }
    params = {
        'max_length': f'{max_length}',
    }
    response = session.get(url=url, params=params, headers=headers, timeout=5)
    if logger: logger.debug(
        f"Gotten response:\nstatus_code: {response.status_code}\n"
        f"response ok? {response.ok}\n"
        f"response contents: {response.content}\n"
    )
    return response.json()
