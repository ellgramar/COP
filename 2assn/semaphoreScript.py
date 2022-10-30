# By Elliot Marshall, 815277391

import concurrent.futures   #   for ThreadPoolExecutor
import threading            #   for threading
from threading import Lock, Thread, Semaphore  #   also for threading
import time                 #   for wait
from time import sleep      #   also for wait
from datetime import date   #   for finding age
import sys                  #   for command line args handling


def bad_function(screen_lock):
    screen_lock.acquire()


def bad_function2(file_semaphore):
    file_semaphore.acquire(timeout=5)


def find_age(birthday):
    # set year to int again just incase
    mmddyy = birthday.split("/")
    mm = int(mmddyy[0])
    dd = int(mmddyy[1])
    yy = int(mmddyy[2])
    dob = date(yy,mm,dd)
    return (date.today()-dob).days // 365


def get_user_input(first_name):
    print("Hello ", first_name)
    last_name = input("Enter your last name: ")
    birthday = input("lease enter your date of birth (mm/dd/yyyy): ")
    age = find_age(birthday)
    user_string = first_name+" "+last_name+": "+str(age)+" years old, "+"born "+birthday+"\n"
    print(user_string)
    return user_string


def threading_function(file_semaphore, screen_lock, first_name):
    screen_lock.acquire()
    user_string = get_user_input(first_name)
    screen_lock.release()
    # file_semaphore
    file_semaphore.acquire(timeout=5)
    fp = open("semaphorerocks.txt", "a",1)
    fp.write(user_string)
    fp.close()
    file_semaphore.release()


# reset semaphorerocks.txt at each run
fp = open("semaphorerocks.txt", "w",1)
fp.write("")
fp.close()

# create two locks, one for file i/o and one for user (screen) i/o
file_semaphore = Semaphore(3)
screen_lock = Lock()
length = len(sys.argv)
#   bad functions for demonstraiting how to create deadlock in current paradigm
#   uncomment if you want to break something
#bad_function(screen_lock)
bad_function2(file_semaphore)

# create threads
for i in range(1,length):
    t = Thread(target=threading_function, args=(file_semaphore, screen_lock, (sys.argv[i])))
    t.start()