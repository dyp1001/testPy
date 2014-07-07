'''
Created on Jun 24, 2014

@author: Kusi Family
'''

import thread
import time

def worker_thread(id):
    
    print "Thread id %d now alive"%id
    count =1
    while True:
        print "Thread with id: %d has counter value %d"%(id,count)
        time.sleep(2)
        count +=1
        
for i in range(5):
    thread.start_new_thread(worker_thread, (i,))
    
print "Main thread going for infinite wait loop"
while True:
    pass