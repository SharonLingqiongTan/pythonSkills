#!/usr/bin/env python
import threading

def main():
	# The program shows 1 thread is running, which is this test program!
    print threading.active_count() # see how many threads running
    print threading.enumerate() # list of threads running
    print threading.current_thread() # current thread

if __name__ == '__main__':
    main()
