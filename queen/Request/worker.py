import sys
import os
from concurrent.futures import ThreadPoolExecutor, as_completed, wait
import concurrent
import threading

# File finder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from File.operator import xlupdate
from Request.automator import Request
from Request.storage import Mega
from Request.autoWhat import RequestWhatsapp



''' --- start worker's / thread pool ---  '''
class Worker:
    def __init__(self, worker=None, target=None, args=None, status=None):
        self.worker_n = worker
        self._target = target
        self.args = args
        self.status = status
        self.lock = threading.Lock()
        self.__threadops()
        

    # method must be cached, to avoid multple calling/call once and maintain subsequent call
    
        
        
    def __threadops(self):
        
        with ThreadPoolExecutor(self.worker_n) as executors:
                executors.thread_name_prefix = self._target
                
                futures = [executors.submit(self.__target, arg) for arg in self.args]
                
                
                for future in as_completed(futures):
                    try:
                        
                        # t = threading.Thread(target=future.add_done_callback, args=((self.__ttarget),), daemon=True)
                        # t.start()
                        
                        future.add_done_callback(self.__ttarget)  
                    except:
                        pass
                    
    def __target(self, args=None):
        target = self._target      # class()
        try: 
            return eval(f'{target}().call({args})')   
            # target().call(args) e.g Request().call(args)
        except:
            pass
    
    def __ttarget(self, future):
        result = future.result()            # block
        try:
            with self.lock:
                # status is generated from result
                return xlupdate(field="userID", value=result["userID"], change="status", newValue=self.status['status'])
        except:
            pass
        

    
''' --- end worker's / thread pool ---  '''

