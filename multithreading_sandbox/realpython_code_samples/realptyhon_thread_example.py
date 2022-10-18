import logging
import threading
import time
from concurrent.futures import ThreadPoolExecutor

def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)


# driver code
if __name__ == "__main__":

    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    logging.info("Main    : before creating thread")

    # example w/ only one thread executed
    # x = threading.Thread(target=thread_function, args=(1,))
    # logging.info("Main    : before running thread")
    # x.start()
    # logging.info("Main    : wait for the thread to finish")
    # x.join()  # .join method makes one thread wait for other to finish execution
    # logging.info("Main    : all done")

# example w/ multiple threads executed
    # threads = list()
    # for index in range(10):
    #     logging.info("Main    : create and start thread %d.", index)
    #     x = threading.Thread(target=thread_function, args=(index,))
    #     threads.append(x)
    #     x.start()

    # for index, thread in enumerate(threads):
    #     logging.info("Main    : before joining thread %d.", index)
    #     thread.join()  # .join method makes one thread wait for other to finish execution
    #     logging.info("Main    : thread %d done", index)

# the same functionality w/ ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(thread_function, range(10))