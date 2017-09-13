import threading
# if we don't use join, the two x we print could be unexpected
def do_this():
	# sth thread do
	global x
	x = 0
	while x < 300000:
		x += 1
	if x == 300000:
		print x

def do_after():
	global x
	x = 450000  # we might not see 300, thread cut off each other
	while x < 600000:
		x += 1

	print x

global x
x = 0
my_thread = threading.Thread(target=do_this)
my_thread.start()
print my_thread.ident # get thread identification number, exists even thread dead
# my_thread.join() # other thread will wait this finish, actually it joins them to one thread
my_next_thread = threading.Thread(target=do_after)
my_next_thread.start()
print my_next_thread.ident

#print threading.active_count() # sometimes one thread finish before this, so there would be only one (sometimes two)
print threading.enumerate() # list of threads running
# print threading.current_thread() # current thread
