import sys
import os
import time

# Automator and options
from alright import WhatsApp
from webdriver_manager.core.file_manager import FileManager
from webdriver_manager.core.driver_cache import DriverCacheManager
from webdriver_manager.core.os_manager import OperationSystemManager, ChromeType
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver



# compact operation
import yaml
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Request.loader import PlatformLoader
from File.handler import resource_formatter
from Request.processor import MicroProcess


# thread
import continuous_threading
from continuous_threading import CommandProcess, ContinuousThread
import threading

# caching
import weakref



'''
3. the thread called will be deamon and will implement the continuous_thread
4. deamon will be cache with (is_alive) and when called again will execute the alternate function
'''


_cache_box = weakref.WeakValueDictionary()
_thread_box = list()
_state_cache = weakref.WeakValueDictionary()

# Command Class[trigger a continuous thread at first and then check if thread is still alive]
class AutoMediaBot(object):
    def __init__(self, data):
        self.data = data
        if len(_thread_box) > 1:
            print("Setting limit to Thread_cmd")
            ctn_thread = _limiter(_running_thread)
            return self.__init__(data=data)
        else:
            print('Active and alive')

    # setup environmental parameters
    def operate(self):
        '''
        write_messages then read_and_process messages
        '''
        # cache_driver = _thread_box[0]
        machine = self.whatsapp
        micro_process = MicroProcess(drive=machine)
        time.sleep(5)
    
    # defaultly call and login run once
    def setup_environment(self, data):
        '''
        use the with statement to call the automation and on successful setup call the continuous thread which will keep it awake and stopping it to remain and as well ensuring successful closing of the thread
        '''
        print('Setting_up Automation Environment')
        
        option = webdriver.ChromeOptions()
        option.add_argument('--ignore-certificate-errors')
        option.add_argument('--ignore-ssl-errors')
        option.add_experimental_option('detach', True)
        
        driver = webdriver.Chrome(options=option, service=None)
        print(driver)
        
        self.whatsapp = WhatsApp(browser=driver)
        
        micro_system = PlatformLoader(data=data, browser=self.whatsapp.mini_driver())
        
        '''
        Once the sytem environment commence startup,
        the pool thread remain awake making it unable to close
        
        the return status value after login in triggers the 
        continuousprocess, which in turn inherit the
        scanning of the data for available content and sorting
        
        data is collected in chunk and processed in chunk
        
        continuousprocess sleep only when there is no data to process
        and the time to sleep is 2sec
        '''
        
        
        '''
        Always(Continuous thread) read unreadmessages[{}] and store in a textfile and process:
        Process is for every firstline of message, check if any command is found from the command set,
        if found, use handler to construct a request and save to request while message is marked read,
        request(pending) is operated on (threadpool)
        
        Process II: response is constructed by futures using request data and wait on queue to be passed to the Always(Continuous thread) send messages
        
        using the John Von NeuMann BottleNeck request and respond on a single thread.
        
        '''
        try:
            if micro_system:
                print('Starting Loop thread')
                ctn_thread = ContinuousThread(target=self.operate, daemon=True)
                ctn_thread.start()  
        except:
            print('NOT SUCCESSFULLY LOGGED IN')


        print("sleeping after environment setup")



    '''
    Task and Action
    
    Task:
    Internal task -> generated by machine then write to machine[support with handler]
    1. send messages[
        a numbers 
        list of message 
        iterate every number the send an iteration of all message for each
    ]
    
    2. send media[
        list of numbers 
        a single fetched file / list
        iterate every number the send an iteration of all message for each
    ]
    
    3. search by name / unsaved contacts
    
    
    External task -> needed for machine to process[for each result, use regex to process it and generate proper response -> internal task]
    4. get last message received in a given chat [then regex]
    
    5. retrieve all chat names with unread messages [+ regex]
    '''
    
    



# store live thread[CommandThread]
def _caching_system(cmd_thread, data):
    if cmd_thread not in _cache_box:
        target = AutoMediaBot(data=data) 
        new_cache = CommandProcess(target=target, daemon=True)
        _cache_box[cmd_thread] = new_cache
    else:
        new_cache = _cache_box[cmd_thread]
    new_cache.start()
    return new_cache


def _limiter(_list):
    if _list and len(_list) > 1:
        while len(_list) > 1:
            for index in len(_list):
                _list.pop(index)
    return _list





# Start a runner[continuous thread] use for cache
class Operational:
    def __runner__(self, data):
        if _thread_box and len(_thread_box) == 1 and _cache_box:
            # print("using Registered Thread")
            # _thread_box[0].send_cmd('sending_message')
            # if not data:
            #     getattr(_thread_box[0], 'send_cmd')('sending_message')
            print('Waiting for Command')
        elif len(_thread_box) > 1:
            print("Setting limit to Thread")
            ctn_thread = _limiter(_thread_box)
            return self.__runner__(data)
        else:
            cmd_thread = _caching_system(cmd_thread='MainThread', data=data)
            print("Registered a Runner Thread")
            _thread_box.append(cmd_thread)
            cmd_thread.send_cmd('setup_environment', data=data)

            return self.__runner__(data)

# Direct caller from loop
class RequestWhatsapp:

    def call(self, arg):
        
        # t = threading.Thread(target=Operational().__runner__(), args=(arg,), daemon=True)
        # t.start()
        return Operational().__runner__(data=arg)

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
