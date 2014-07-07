'''
Created on Jun 24, 2014

@author: Kusi Family
'''

import os

def child_process():
    print "I am child process and my pid is: %d"%os.getpid()
    print "The child is exiting"

def parent_process():
    print "I am the parent process and my pid is: %d"%os.getpid()
    
    childid = os.fork()
    
    if childid == 0:
        #we are inside the child
        child_process()
        
    else:
        # we are inside the parent 
        print "we are inside the parent"
        print "Our child has the PID: %d"%childid
        
    while True:
        pass
    
parent_process()