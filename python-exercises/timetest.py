def minor(v):
    return min(v)

list = [5,3,0,9]

print minor(list)

exit()

import time

t0 = time.time()
time.sleep(4)
t1 = time.time()

print "It took %.2f seconds to execute." % (t1 - t0)