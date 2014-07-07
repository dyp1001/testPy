'''
Created on Jun 24, 2014

@author: Kusi Family
'''
#!usr/bin/env python
import os

def child():
   print 'A new child ',  os.getpid( )
   os._exit(0)  

#test
def parent():
   while True:
      newpid = os.fork()
      if newpid == 0:
         child()
      else:
         pids = (os.getpid(), newpid)
         print "parent: %d, child: %d" % pids
      if raw_input( ) == 'q': break

parent()