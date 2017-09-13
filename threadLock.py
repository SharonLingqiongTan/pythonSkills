import threading
# lock doesn't allow one thread change a shared resource when other one is working on it
def do_this():
	# sth thread do
	global x, y, lock1, lock2
	lock1.acquire()

	while x < 300:
		x += 1
	print x
	# lock1.release()


def do_after():
	global x, y, lock1, lock2
	lock2.acquire()
	
	x = 450
	while x < 600:
		x += 1

	print x
	# lock2.release()

def do_later():
	global x, y, lock1, lock2
	# lock2.acquire()
	x = 500
	while x < 700:
		x += 1

	print x
	# lock2.release()

global x, y, lock
x = 0
y = 0
lock1 = threading.Lock()
lock2 = threading.Lock()

my_thread = threading.Thread(target=do_this)

my_thread.start()


my_next_thread = threading.Thread(target=do_after)
my_next_thread.start()

my_last_thread = threading.Thread(target=do_later)
my_last_thread.start()


#print threading.active_count() # sometimes one thread finish before this, so there would be only one (sometimes two)
# print threading.enumerate() # list of threads running
# print threading.current_thread() # current thread