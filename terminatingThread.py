import threading

def do_this():
	# sth thread do
	global dead
	print 'This is my thread!'
	x = 0
	while not dead:
		x += 1
		pass
	print x

global dead
dead = False

my_thread = threading.Thread(target=do_this)
my_thread.start()

print threading.active_count() # sometimes one thread finish before this, so there would be only one (sometimes two)
print threading.enumerate() # list of threads running
print threading.current_thread() # current thread

raw_input('Hit enter to die.') 
dead = True

