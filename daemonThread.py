import threading

def do_this():
	# sth thread do
	global x
	x = 0
	while x < 300000:
		x += 1
	if x == 300000:
		# print x

def do_after():
	global x
	x = 450000  
	while x < 600000:
		x += 1

	# print x

# all main thread is not daemon
# entire python process will close if all non-daemon threads finished
global x
x = 0
main_thread = threading.enumerate()[0]
print main_thread.isDaemon()
my_thread = threading.Thread(target=do_this)
my_thread.setDaemon(True)
my_thread.start()
my_thread.ident 
# my_thread.join() 
my_next_thread = threading.Thread(target=do_after)
my_next_thread.start()
print my_next_thread.ident

#print threading.active_count() # sometimes one thread finish before this, so there would be only one (sometimes two)
print threading.enumerate() # list of threads running
# print threading.current_thread() # current thread