#!/bin/python3

import time
import requests
import threading
from concurrent.futures import ThreadPoolExecutor



thread_local = threading.local()


def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session


def download_site(url):
    session = get_session()
    with session.get(url) as response:
        print(f"Read {len(response.content)} from {url}")


def download_all_sites(sites):
    with ThreadPoolExecutor(max_workers=10) as executor:  # ThreadPoolExecutor as context manager
        executor.map(download_site, sites)


if __name__ == "__main__":
    sites = [
        "https://en.wikipedia.org/wiki/Python_(programming_language)",
        "https://en.wikipedia.org/wiki/Multithreading_(computer_architecture)",
    ] * 80
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds")