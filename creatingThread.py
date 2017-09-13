import threading

def do_this():
	# sth thread do
	print 'This is my thread!'

my_thread = threading.Thread(target=do_this)
my_thread.start()

print threading.active_count() # sometimes one thread finish before this, so there would be only one (sometimes two)
print threading.enumerate() # list of threads running
print threading.current_thread() # current thread