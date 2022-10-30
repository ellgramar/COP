# Elliot Marshall

import concurrent.futures
import logging
import threading
import time
from time import sleep


def threadingFunction(thread):
    # get filepath
    filePath = input("Enter file path: ")
    if filePath == "q":
        return
    else:
        file = open(filePath, "r")
        Lines = file.readlines()
        for line in Lines:
            print(line)
        return


if __name__ == "__main__":
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(threadingFunction, range(3))
