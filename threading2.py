import sys
import threading
import time

def thread_function(name, sleeptime):

    with open("names.txt", "r+") as namefiles:
        print(namefiles.read())

    with open("names.txt", "r+") as namefiles:
        message = input("Pleaase enter your message: ")
        namefiles.write(f"thread name is {name}\t{message}\t")
    #sleep_function(name,sleeptime)

    
def sleep_function(name,sTime):
    # this makes the wait time the critical path, not responce time like usual
    time.sleep(sTime)
    print(f"Thread {name} is done")


if __name__ == "__main__":
    print("hi")
    s = 1
    for n in sys.argv[1:]:
        print("created thread {n}")
        prth = threading.Thread(target=thread_function, args=(n,s,))
        prth.start()
        prth.join()
        
        slth = threading.Thread(target=sleep_function, args=(n,s,))
        slth.start()
        s += 2