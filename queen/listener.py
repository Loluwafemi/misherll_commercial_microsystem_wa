# from File.operator import xlread as content
import time
from File.operator import xlread, xlwrite
from File.handler import gen_data
from subscriber import xlRequest, xlWhatkit, xlDone, Notifier, xlMega
from observer import Data


# concurrency
from concurrent.futures import ThreadPoolExecutor, as_completed, wait
import concurrent
import threading



def return_dic(interval, dictionary_func, field=None, value=None):
    while True:
        yield dictionary_func(field, value)
        time.sleep(interval)

# trigger query manager
def get_cdata(field=None, value=None):
    return xlread(field=field, value=value)

# do not touch
# heartbit timer[5 second check]
dictionary_gen = return_dic(2, get_cdata, field="status", value="Pending")

# refreshes digits every seconds
def counter(field=None, value=None):
    for item in return_dic(1, get_cdata, field=field, value=value):
        return len(item)
    
    

def report():
    return {
        "Pending": counter(field="status", value="Pending"),
        "Processing": counter(field="status", value="Processing"),
        "Processed": counter(field="status", value="Processed"),
        "Done": counter(field="status", value="Done"),
        "Server Error": counter(field="status", value="Server Error"),
        "Credential Error": counter(field="status", value="Credential Error"),
        "Complete": counter(field="status", value="Complete"),
        "Total": counter()
        }

def initaitor():
    # subject interface for the subscibers
    observer = Data()
    
    # subscribers
    xlreq = xlRequest()
    xlwhat = xlWhatkit()            # causes blocking
    xldone = xlDone()
    xlmega = xlMega()
    xlnotify = Notifier()
    
    # attach[subscribe] to the observer[using the inherited method]
    
    subscriber = [xlwhat, xlreq, xldone, xlmega, xlnotify]
    
    with ThreadPoolExecutor(len(subscriber)) as executors:
        executors.thread_name_prefix = 'subscriber'
        futures = executors.map(observer.subscribe, subscriber)
        
    
    # use the timer to tiger this
    # while data is the record dictionary information.
    for _ in dictionary_gen:
        # xlwrite(gen_data())
        observer.data = report()
        
   
 
