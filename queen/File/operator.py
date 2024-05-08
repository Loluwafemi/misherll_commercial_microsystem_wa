import json
import os
import yaml
import re

''' System '''
import pyzipper

''' Timeout '''
import time
from functools import wraps, partial

root = f'{os.getcwd()}\queen'

data_json = f'{root}\storage\data.json'
request_json = f'{root}\storage\\request.json'
response_json = f'{root}\storage\\response.json'
path = data_json
# path = f'{root}\Dependencies\data.json'
path_config = f'{root}\Dependencies\config.yml'
path_media = f'{root}\Dependencies\paths'



path_name = f'{root}\Dependencies\paths'
public_path = f'{path_name}\public\\'      # save in folder per file
private_path = f'{path_name}\private\\'        # save in a folder in whole [append data]

generated_content_path = f'{root}\Dependencies\environments\generated_content'


# File Manage --start--

def storage_exist():

    if not os.path.exists(path):
        file = open(path, 'w')
        file.write('\n[]')
        file.close()
    else: pass


def storage_exist_new(path):
    
    if not os.path.exists(path):
        file = open(path, 'w')
        file.write('\n[]')
        file.close()
    else: pass


def dedupe(items):
    seen = list()
    for item in items:
        if item not in seen and isinstance(item, dict):
            seen.append(item)
    return seen


def _save(content):
    try:
        with open(path, 'w') as contain:

                new_data = dedupe(content)

                json.dump(dedupe(new_data), contain, indent=4)
            
                # print('success')
    except:
        print('error saving data')



def _save_new(path, content):
    try:
        with open(path, 'w') as contain:

                new_data = dedupe(content)

                json.dump(dedupe(new_data), contain, indent=4)
            
                # print('success')
    except:
        print('error saving data')

# File Manager --end--

# File Operator --start--
# Find Record return a list[multiple result] or dictionary[single result]
def _find(field, value):
    store = list()
    try:
        with open(path, 'r') as rf:
            contents = json.load(rf)
        for item in contents:
            if isinstance(item, dict):
                if item[field] == value:
                    store.append(item)
            
        return store        
                        
    except:
        return "Error Retreiving data"

def _find_new(path, field, value):
    store = list()
    try:
        with open(path, 'r') as rf:
            contents = json.load(rf)
        for item in contents:
            if isinstance(item, dict):
                if item[field] == value:
                    store.append(item)
            
        return store        
                        
    except:
        return "Error Retreiving data"

# Read record
def xlread(field=None, value=None):
    
    if field is None:
        try:
            with open(path, 'r') as rf:
                result = json.load(rf)
            return result
        except:
            print('error retreiving data|Empty')
            
        # else use the keyword to print the data
    return _find(field, value)


def xlread_new(path, field=None, value=None):
    
    if field is None:
        try:
            with open(path, 'r') as rf:
                result = json.load(rf)
            return result
        except:
            print('error retreiving data|Empty')
            
        # else use the keyword to print the data
    return _find_new(path, field, value)


def xlwrite(content):
    storage_exist()
    try:
        storage = []
        olddata = xlread()
        if olddata != None:
            storage = olddata
            newdata = storage.append(content)
            _save(storage)
        else:
            _save(content)
    except:
        print('error appending data')
    storage.clear()
    
    
def xlwrite_new(path, content):
    storage_exist_new(path)
    try:
        storage = []
        olddata = xlread_new(path)
        if olddata != None:
            storage = olddata
            newdata = storage.append(content)
            _save_new(path, storage)
        else:
            _save_new(path, content)
    except:
        print('error appending data')
    storage.clear()
    
var = {
        "recipient": None,
        "task": "read",
        "status": "pending",
        "request": {
            "type": "CUSTOM_API",
            "state": "END"
        },
        "content": {
            "command": None,
            "var_": None
        }

    }

# fetch the whole data, pop[find our data], modify and re-instate 
def xlupdate(field=None, value=None, change=None, newValue=None):
    if field is None and eq is None and change is None:
        return "Complete the query"
    
    try:
        allx = xlread()
        for single in xlread(field=field, value=value):
            key = allx.index(single)
            item = allx.pop(key)
        
        if change == "delete":
            new = None
            print("sucessfully delete")
            
        else:
            item[change] = newValue
            new = item
            print("sucessfully edit")
        
        storage = []
        olddata = allx
        storage = olddata
        newdata = storage.append(new)
        _save(storage)      
    except:
        return "Error Updating the file" 


def xldelete(credential):
    field = 'status'
    value = credential['status']
    changeto = "delete"
    xlupdate(field=field, value=value, change=changeto)

# File Operator --end--

def config(path_configx):
    with open(path_configx, 'r') as atr:
        data = json.load(atr)
    if data:
        return data
    else:
        print("Error Getting Config")
        return

def config(path_configx):
    with open(path_configx, 'r') as atr:
        data = yaml.safe_load(atr)
    if data:
        return data
    else:
        print("Error Getting Config")
        return



def putFile(media):
    with open(path_media, 'w'):
        ...

# Core Operation
def protectFile(filename, passkey):
    content = showFile(private_path, filename)
    storage = public_path + f'{filename}.zip'
    zipped_item = 0
    data_length = len(content)
    with pyzipper.AESZipFile(storage, 'w', compression=pyzipper.ZIP_LZMA) as zipp:
      zipp.setencryption(pyzipper.WZ_AES)
      zipp.setpassword(b'{passkey}')
      space = private_path + filename
      os.chdir(space)
      if content:
        for index in content:
          temp_path = index['content']
          try:
            zipp.write(index['content'])
            print('Zipped')
          except:
              return f'Error Writing to Encrypted File: {zipp.filename}'
      else:
          return f'Content(s) found: {content}'
      zipped_item = len(zipp.filelist)

    if zipped_item == len(content):
      isCleared = deleteFile(temp_path)
    return {
      "pskey": passkey,
      "isCleared": isCleared,
      "length": data_length
    }

def deleteFile(path):
    abs_path = os.path.dirname(os.path.abspath(path))
    try:
      if abs_path:
            for item in os.listdir(abs_path):
                  os.remove(item)
            return True
      return False
    except:
      print('Unable to delete Raw File(s)')


# open path and store all file to a list
def showFile(path, name):
    store = list()
    space = f'{path}\\{name}'
    sf = os.listdir(space)
    for index in sf:
            store.append({
              "path": find(index),
              "name": os.path.basename(index),
              "content": index,
              "abspath": path,
            })
    if store:
        return store
    else: return None
    
    
def __iterx(inc):
    if isinstance(inc, list):
        __iterx(inc)
    return inc


def find(target):
    for roots, dirs, files in os.walk(path_name):
        if target in files:
            p = '{}\{}'.format(roots, __iterx(target))
            return p
          
def timeout(period=0):
    def decorator(func):
          @wraps(func)
          def wrapper(*args):
              nonlocal period
              while period > 0:
                  result = func(*args)
                  if result:
                      result['duration'] = period
                      return result
                      break
                  time.sleep(1)
                  period -= 1
          return wrapper
    return decorator

@timeout(period=20)
def returnFunction(name):
    if name in os.listdir(private_path):
        return {
                'isFound': True,
                'name': f'Found: {name}',
                "duration": None
                }
    return f'Looking for: {name} in {private_path}.'

# put a timeout(20s) decorator[switch from True to False, using fromDecorator] 




# # read and join all
@property
def resources():
    paths = [request_json, response_json]
    store = []
    for path in paths:
        store += read_content(path)
    return store

def read_content(path):
    if path:
        with open(path, 'r') as rf:
            result = json.load(rf)
    return result

def disintegrate(data):
    template = dict()
    if data:
        instructions = re.split('\s', data) if data else None 
        length = len(instructions)
    if instructions:
            for index in range(length):
                if instructions[index].startswith('>'):
                    template['cmd'] = instructions[index]
                        
                elif instructions[index].startswith('-'):
                    template[f'-var_{index}'] = instructions[index]
                    
                elif re.search('\w', instructions[index]):
                    template['str'] = instructions[index]          
    return template






# show all registered commands
path_command = f'{root}\Dependencies\commands'
@property
def _readAll():
    bulk = []
    files = os.listdir(path_command)
    for file in files:
        dir = os.path.dirname(f"{path_command}\\{file}")
        bulk.append(readJson(f'{dir}\\{file}'))
    return bulk

    # read each and append to a list

def readJson(file):
    with open(file, 'r') as file:
        return json.load(file)
    
readAll = _readAll.fget()
    


@property
def _commands():
    cmd = set()
    bulk = [] if readAll is None else readAll
    for ops in bulk:
        if ops:
            cmd.add(ops["command_name"])
    return cmd
        
commands = _commands.fget()


# find operation with command index

def getOperation(command):
    operation = readAll
    for ops in operation:
        if command == ops['command_name']:
            return ops
