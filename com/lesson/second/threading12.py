'''
Created on Jun 24, 2014

@author: Kusi Family
'''

import threading
import Queue
import time

class WorkerThread( threading.Thread ):
    
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue
        
    def run(self):
        print "In WorkerThread"
        while True:
            counter = self.queue.get()
            print "Ordered to sleep for %d seconds!"%counter
            time.sleep(counter)
            print "Finish sleeping for %d seconds "%counter
            self.queue.task_done()
            
queue = Queue.Queue()
            
for i in range(10):
    print "Creating workerThread: %d"%i
    worker = WorkerThread(queue)
    worker.setDaemon(True)
    worker.start()
    print "WorkerThread %d Created!"%i
    
for j in range(10):
    queue.put(j)
    
queue.join()

print "All task over"
    