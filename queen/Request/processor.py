
'''
will take in machine object
A class tha deals with write, read and process both
Resource > request, data(external->output) and response(output)

the continuousthread read the three if any is found, it maps the result->read and write(change status) with micro_processor: map([read, write], micro_processor)
pool_number = 2

micro_processor: which on the other hand checks if data is read or write and the proceed to use the one that best suite:
if data.task == read:
    // make sure you read data to avoid repetition of operation
    disintegrate data and put to list[command and var,]
elif data.task == write:
    disintegrate data and send


'''

# concurrency
from concurrent.futures import ThreadPoolExecutor, as_completed, wait
import concurrent
import threading, sys, os

# file operator
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from File.operator import request_json, response_json, disintegrate, resources, xlwrite_new, commands

'''
On using this medium to process drive(read and send)
##READ
1. Store unRead Messages(all) in a txt file
2. Scan unread messages(filter the ones starting with '>')
3. for each of the valid message create a pool of thread to create a request
4. kill thread on completion

##SEND
1. from the respond file, scan for pending response data
2. line the data to a queue and set response? flag to true
3. for each response send message to the recipient and write to file
4. if queue is empty, set response? flag to false.


'''

class MicroProcess(object):
    
    def __init__(self, drive):
        self.whatsapp = drive
        # setup the pipe to store all event: read and send
        # and check if response file contain data and change flag
        self.isresponse = False
        self._bottleneck()
        
        
        
        
    
    def __send__(self):
        print("Sending Messages")
    
    def __read__(self):
        print("Reading unread Messages")
        # get list of all chat with unread messages
        _unread = self.whatsapp.fetch_all_unread_chats()
        print(f'Unread messages are: {_unread}')
        # for msg in _unread:
        #     _last_message = self.whatsapp.get_last_message_received(query=self.whatsapp.find_by_username(msg))
        #     print(f'Last Message: {_last_message}')
            
    # start a continuous thread to check flag, start reading and sleep
    def _bottleneck(self):
        
        if self.isresponse:
            self.__send__()
            
        self.__read__()
    
    '''def __init__(self, machine, incoming):
        self.machine = machine
        self.unread = self.put_to_resource(incoming) if incoming else 0
        self.operate()
        
        
    def __repr__(self):
        return f'Processing \n \
                reading: {len(self.unread)} messages \n \
                sending: {len(write)} messages'
    
    # only unread messages
    def put_to_resource(self, incoming):
        try:
            xlwrite_new(request_json, incoming)
        except:
            pass            
    
    
    def operate(self):
        data = resources.fget()
        tp = ThreadPoolExecutor()
        futures = [tp.submit(self.__process, task) for task in data]
        
        for future in as_completed(futures):
            pass
        # do something with the lists of data
    
    
    def __process(self, data):
        if data:
            for item in data:
                operation = item['task']
                if operation == 'read':
                    task, result = 'read', disintegrate(operation)
                    
                elif operation == 'write':
                    self.__write(item)
                    
        else: return task, result
        
    
    def __write(self, data):
        try:
            self.machine.sending_message(data['recipient'], data['message'])
        except:
            pass
            # send default message to machine
    

    
'''



