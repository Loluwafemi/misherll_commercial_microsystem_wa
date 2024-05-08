import sys
import os
import threading
import contextlib
import yaml
# from loader import PlatformLoader as PLoader
# File finder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from File.operator import putFile
from Request.loader import PlatformLoader



class Request:
    
    def call(self, arg):
        # operation call
        if arg:
            return PlatformLoader(arg)              # self.moderator()
        else: pass
    
    
    # change status using result
    def moderator(self, result):
        result = {
            ... or None
        }
        try:        # assign values
            pass
        except:
            pass
        finally:
            return result
        
            

    # lock before use[avoid dl]
    def saveResult(self, result):
        if browse:
            self.lock = threading.Lock()
            with self.lock:
            # put media to a directory
                ...    
        
        

'''
# takes in a dictionary of report

Steps
Every call 
    1. initiate the loader use the moderator function to listen to the returned result
    2. moderator decides to work on the data passed[update status, trial, history, url and others]
    3. and finally the system exit
'''