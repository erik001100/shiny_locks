#!/usr/bin/env python

import time
import shiny_locks

def main():
    with shiny_locks.file_lock('/tmp/my_test.lock'):
        job()
    
def job():    
    print("I am here and sleeping for 10 seconds")
    for i in range(10):
        print("Sleeping for {0} seconds...".format(i))
        time.sleep(i)

if __name__ == '__main__':
    main()
