import logging
import threading
import time
import sys

# handle and run a few sleep threads

#TODO: will need thread function here


def sleep_thread(name):
    logging.info(f"Thread {name}: starting")
    time.sleep(3)
    logging.info(f"Thread{name}: finished")


if __name__ == "__main__":
    logging.basicConfig(format="%(asctime)s: %(message)S", level=logging.INFO,
                        datefmt="%H:%M:%S")
    print(sys.argv)

    for i in sys.argv[1:]:
        logging.info(f"Main: Thread {i} creation started")
        
        slth = threading.Thread(target=sleep_thread, args=(i,))

        logging.info(f"Main: Thread {i} created, preparing to run")
        
        slth.start()

        logging.info(f"Main: Thread {i} launched - will notify when complete")
        logging.info(f"Rest of program running\n")
