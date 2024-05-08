# from Request.base import Operate
from File.operator import xldelete, xlread, root, config as cfg
from Request.worker import Worker
import os
'''
targets are:
Request : used to pass request to list of data and save result to path
Mega : used to take saved file data and send it to cloud delete after(maintain space)

'''

# for credentials[all data] onPending
class xlRequest:
    def update(self, subject):
        if subject.data['Pending'] > 0:
            # configurations (dy)
            path = f'{root}\Dependencies\config.yml'
            worker_n = cfg(path_configx=path)['Selenium']['worker']
            result = xlread(field="status", value="Pending")
            Worker(worker=worker_n,
                   target='Request',
                   args=result, 
                   status={
                       "status": "Processed",
                       "wait": False
                   })

# for credentials[all data] onComplete
class xlMega:
    def update(self, subject):
        if subject.data['Processed'] > 0:
            # configurations (dy)
            path = f'{root}\Dependencies\config.yml'
            worker_n = cfg(path_configx=path)['Mega']['worker']
            result = xlread(field="status", value="Processed")
            Worker(worker=worker_n,
                   target='Mega',
                   args=result, 
                   status={
                       "status": "Complete",
                       "wait": False
                       
                   })

# onProcessed on 1 thread
# put each[query] result on a queu
class xlWhatkit:
    def update(self, subject):
        if True:            
            # configurations (dy)
            path = f'{root}\Dependencies\config.yml'
            worker_n = cfg(path_configx=path)['Whatsapp']['worker']
            result = xlread(field="platform", value='WHATSAPP_ACCESS')
            filtered_result = [response for response in result 
                      if 'pending' in response['status'].split('.')
                      ]
            Worker(worker=worker_n,
                   target='RequestWhatsapp',
                   args=filtered_result, 
                   status={
                       "status": "Pending",
                       "wait": True
                   })

# xldelete[data], delete any data with status=Done
class xlDone:
    def update(self, subject=None):
        if subject.data['Done'] > 0:
            try:
                result = xlread(field="status", value="Done")
                for item in result:
                    xldelete(item)
            except:
                pass

# dynamically put all to a readable file, using panda
class Notifier:
    def update(self, subject):
        # display records
        # print('##################################################')
        # print(f'Processed : Processed record has {subject.data["Processed"]} data')
        # print(f'Pending : Pending record has {subject.data["Pending"]} data')
        # print(f'Delayed [server error] : server delayed record has {subject.data["Server Error"]} data')
        # print(f'Completed : Completed record has {subject.data["Done"]} data')
        # print(f'Incorrect Credential :  Incorrect record are {subject.data["Credential Error"]} data')
        # print(f'Total Credential :  Total record are {subject.data["Total"]}')
        # print('##################################################')

        ...


