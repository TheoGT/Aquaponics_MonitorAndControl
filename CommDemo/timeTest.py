import time

t0 = time.time()
t1 = time.time()

print('Start: Time is ' + str(t0))

while (t1 - t0 < 5):
	t1 = time.time()

print('Stop: Time is ' + str(t1))