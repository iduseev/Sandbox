#!/bin/python3

import time
import random
import threading
from typing import List, Dict
from concurrent.futures import ThreadPoolExecutor

import requests

import CAT_FACT_API

""" This script is intended to show how multithread request can be sent using queue and via ThreadPoolExecutor """


class MultithreadRequest:
    def __init__(self, tasks: List[Dict]) -> None:
        self.thread_pool_size = 6  # number of maximum executing threads 
        self.results = []  # thread safe data structure
        self.tasks = tasks

    def launch_multithread_process(self) -> None:
        print("Starting launchung multithread process ...")
        # execute multithreading via ThreadPoolExecutor
        with ThreadPoolExecutor(max_workers=self.thread_pool_size) as executor:
            for i in range(self.thread_pool_size):
                print(f"\nRunning thread # {i}\n")
                executor.submit(
                    self.execute_task_thread_local
                )

    def execute_task_thread_local(self) -> None:
        thread_local = threading.local()

        def _get_thread_session() -> requests.Session:
            if not hasattr(thread_local, "session"):
                setattr(thread_local, "session", requests.Session())
            print("Successfully gotten thread session!")
            return thread_local.session

        while self.tasks:  # while queue contains elements
            query_item = self.tasks.pop()
            print(f"\nGetting 1st element from queue!\n{query_item}\n")
            query_item["processing_attempts"] += 1
            resp = CAT_FACT_API.get_cat_fact_by_length(
                max_length=query_item["fact_length"],
                session=_get_thread_session()
            )

            if not resp:
                print("WARNING: Empty response gotten!")
                # check if processing atempts already exceeded
                if query_item["processing_attempts"] > 10:
                    print("Too many attempts to process query! It won't be return back in queue")
                    time.sleep(1)
                else:
                    # put query back to queue
                    self.tasks.insert(0, query_item)
            else:
                data = resp.get("data", {})
                # print(f"cat facts data: {data}")
                self.results.extend([elem.get("fact", "") for elem in data])


# driver code
if __name__ == "__main__":
    cat_facts_tasks = [
        {
        "processing_attempts": 0,
        "fact_length": random.randint(1, 1000)  # generate random integer to pass as length of the fact
        }
        for _ in range(100)
    ]
    try:
        multithread_request = MultithreadRequest(tasks=cat_facts_tasks)  # getting instance of a class
        multithread_request.launch_multithread_process()
        print("\n\nShowing results ...")
        print(f"\n{list(set(multithread_request.results))}\n")  # remaining only unique results
    except Exception as e:
        print("########    GLOBAL ERROR HANDLER    ########")
        print(f"Following exception occured: {e}")
