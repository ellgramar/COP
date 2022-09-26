# A Simple Thread Adventure
import sys
import threading
import time

def thread_function(name):
    print(f"thread name is {name}")

    with open(f"{name}.txt", 'w+') as namefiles:
        namefiles.write(f"thread name is {name}")


if __name__ == "main":
    print("hi")
    for n in sys.argv[1:]:
        prth = threading.Thread(target=thread_function, args=(n,))
        prth.start()
