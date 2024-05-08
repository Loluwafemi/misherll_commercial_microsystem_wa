import pytest
import time
import sys
import os
import json


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.core.file_manager import FileManager
from webdriver_manager.core.driver_cache import DriverCacheManager
from webdriver_manager.core.os_manager import OperationSystemManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import threading

# compact operation
import yaml
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from File.operator import config, returnFunction, protectFile, private_path, root, generated_content_path
# from Request.loader import translator



class PlatformLoader():
    def __init__(self, data, browser=None):
        self.data = data
        self.time_out = 600
        self.browser = browser if browser else None
        if not self.browser:
            self.result = {}
            self.setup_resource(self.data)
            self.completed()
        else:
            '''
            The essence of this is to JUST setup the whatsapp env
            and that's all
            '''
            self.driver = self.browser
            self.setup_data_resources()
            self._fireup()
            
        
        # self.teardown()

    def setup_data_resources(self):
        path = f'{root}\Dependencies\commands\machine_default.json'
        purpose = 'navigation'
        
        try:
            
            # Resources
            self.config_space = config(path)
            
            data = self.data
            print('working')
            self.resource = self.config_space
            
            # STATES
            state = self.resource[purpose]
            # handle operation
            self.OPERATION = state['operation']
            print(self.OPERATION)
            # handle authentication
            self.AUTHENTICATION = state['authentication']
            print(self.AUTHENTICATION)
            
            # handle error
            self.EXCEPTION = state['exception']   
            print(self.EXCEPTION)
                            
        except:
            print('Error Setting Up Data Resources')
        


    def setup_resource(self, data):
        try:
            # Resources
            self.setup_data_resources()
            
            # # # Driver Setup
            storage = os.path.abspath(private_path) + f'\\{data["userID"]}'
            option = webdriver.ChromeOptions()
            option.add_argument('--ignore-certificate-errors')
            option.add_argument('--ignore-ssl-errors')
            option.add_experimental_option('prefs', {
                "download.default_directory": storage
            })
            
            
            cache_manager = DriverCacheManager(file_manager=FileManager(os_system_manager=OperationSystemManager()))
            manager = ChromeDriverManager(cache_manager=cache_manager)
            os_manager = OperationSystemManager(os_type="win64")
            
            self.driver = webdriver.Chrome(service=ChromeService(manager.install()), options=option)
            
            # or
            
            # self.driver = webdriver.Chrome(option)          # change driver
            self._fireup()

        except:
            print('Error Setting Up All Resources')

    def teardown(self, quit=True):
        if quit:
            self.driver.quit()
        else:
            pass

    # caching function
    global log
    log = {
    "status": None, # "self.AUTHENTICATION" or "self.OPERATION" or "self.EXCEPTION"
    "trial": 0,
    "result": None # True or False or Exception or "Done"
    }


    def _fireup(self):
        try:
            self.__operate()
        except:
            log['status'] = self.EXCEPTION
            self.__operate()


    ''' Automation Functions Start '''

    # modiator == controller
    def __operate(self):
        
        # startup chrome driver or use the modelled driver
        try:
            
            if not self.browser:
                print('Designed for raw request')
                self.wait = WebDriverWait(self.driver, self.time_out)
                
                self.driver.get(self.resource['BASEURL'])
                self.driver.set_window_size(768, 974)
           
            
            self.wait = WebDriverWait(self.driver, self.time_out)
                      
            if log["status"]:
                print('B')
                self.task(log["status"])
            else:
                log['trial'] += 1
                print('A')
                log["status"] = self.AUTHENTICATION
                self.__operate()
        except:
            print('Fail to Operate')

    def completed(self):
        data = self.data  
        try:
            downloadCheck = returnFunction(data['userID'])
            if downloadCheck['isFound']:
                print("Path Found")
                protection = protectFile(data['userID'], passkey=data['pskey'])
            if not protection['isCleared']:
                print('Failed')
                pass
            print('Successfull')
            # data['status'] = 'Processed'
            # data['trial'] = log['trial']
            # data['history']['Error'] = 'False'
            # data['history']['Opsmsg'] = 'File Successfully Saved'
            # data['history']['Result'] = protection['length']
            return data
        except:
            data['status'] = 'Server Error, Try Again'
            data['trial'] = log['trial']
            data['history']['Error'] = 'True'
            data['history']['Opsmsg'] = 'File Not Found'
            data['history']['Result'] = None
            return data


    def operation(self, kw):
        # collect kw and store to a queu
        funcs = _queuFunction(kw)
        if funcs:
            for func in funcs:
                obj = func.split('=') if func.find('=') > 0 else None
                function = obj[0] if obj else func
                kw = obj[1] if obj else None
                call_1 = f'{function}("{kw}")' if kw else None
                call_2 = f'{function}()' if kw is None else None
                trigger = call_1 or call_2
                print("Starting Operation")
                eval(f'self.{trigger}')
        else:
            print('No kW function(s)')
          
          
    # on exception call [edit result and close]
    def close(self):
        print(f"Running Selenium Commands to Close operation: {kw}")
        # self.teardown()

    # function declarator
    def task(self, state):
        drive = state
        if drive is None:
            pass
        for index in drive:
            function = index.split('.') if index.find('.') > 0 else None

            func = function[0] if function else index
            pointer = function[1] if function else None
            kw = None if drive[index] is None else drive[index]

            call_1 = f'{func}({pointer}, {"kw"})' if pointer is not None and kw is not None else None

            call_2 = f'{func}({pointer})' if pointer is not None and kw is None else None

            call_3 = f'{func}()' if not function and kw is None and pointer is None else None

            call_4 = f'{func}("{kw}")' if func and kw and pointer is None else None

            trigger = call_1 or call_2 or call_3 or call_4
            eval(f'self.{trigger}')     # replace with visitor's pattern



# ''' Automation Functions End '''

# ''' Commands with exeption handling Start '''

    def findByName(self, kw):
        
        try:
            print(f'Finding Element by Name: {kw}')
            # self.element = self.wait.until(
            #     EC.presence_of_element_located(By.NAME, kw)
            # )
            self.element = self.driver.find_element(By.NAME, kw)
            time.sleep(5)
        except:
            pass

    def findByClassName(self, kw):
        
        try:
            
            print(f'Finding Element by ClassName: {kw}')
            self.element = self.wait.until(EC.presence_of_element_located((
                By.CLASS_NAME,
                kw,)))
            
            # time.sleep(8)
            # self.element = self.driver.find_element(By.CLASS_NAME, kw)
            
        except:
            pass

    def findByID(self, kw):
        
        try:
            print(f'Finding Element by ID: {kw}')
            self.element = self.wait.until(
                EC.presence_of_element_located(
                    (
                        By.ID,
                        kw,
                    )
                    )
                )

            # self.element = self.driver.find_element(By.ID, kw)
            
        except:
            pass

    def findByTagName(self, kw):
        

        try:
            print(f'Finding Element by TagName: {kw}')

            self.element = self.wait.until(
                EC.presence_of_element_located((By.TAG_NAME, kw,))
                )
            # self.element = self.driver.find_element(By.TAG_NAME, kw)
            
        except:
            pass

    def findByLinkText(self, kw):
        
        try:
            print(f'Finding Element by 5 LnkText: {kw}')

            self.element = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, kw,)))
            # self.element = self.driver.find_element(By.LINK_TEXT, kw)
            
        except:
            pass

    def findByPartialLinkText(self, kw):
        
        try:
            print(f'Finding Element by LnkTextP: {kw}')

            self.element = self.wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, kw,)))
            # self.element = self.driver.find_element(By.PARTIAL_LINK_TEXT, kw)
            
        except:
            pass

    def findByCss(self, kw):
        
        try:
            print(f'Finding Element by Css: {kw}')

            self.element = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, kw,))
            )
            # self.element = self.driver.find_element(By.CSS_SELECTOR, kw)
            
        except:
            pass

    def findByXpath(self, kw):
        try:
            print(f'Finding Element by Xpath: {kw}')

            self.element = self.wait.until(
                EC.presence_of_element_located((By.XPATH, kw))
            )
            
        except:
            pass   
            print(f'Element is {self.element}')
            
            
    def findByText(self, kw):
        try:
            print(f'Finding Element by Text: {kw}')

            self.element = self.wait.until(
                EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{kw}')]"))
            )
            
        except:
            pass   
            print(f'Element is {self.element}')
    
    def __repr__(self):
        return str(self.success_pass())
    
    def success_pass(self):
        result, completed = self.driver.execute_script("var req = new XMLHttpRequest();req.open('GET', document.location, false);req.send(null);return req.getAllResponseHeaders()"), True
        return {
            "header": result,
            "continue": completed
        }


    
    # Actions

    def click(self):
        try:
            if self.element:
                print(f'Click Element: {self.element.tag_name}')
                
                self.element.click()
            else: 
                print('Nothing to click')
                pass
        except:
            pass

    def click_e(self):
        try:
            if self.element:
                print(f'Click_E Element: {self.element.tag_name}')
                
                self.driver.execute_script('arguments[0].click();', self.element)
            else: 
                print('Nothing to click')
                pass
        except:
            pass

    def input(self, cred):
        self.element.send_keys('000')
        
        self.element.send_keys(Keys.CONTROL + "a")
        self.element.send_keys(Keys.DELETE)
        
        self.element.send_keys(cred)

    def enter(self):
        try:
            print('Click Enter')

            self.element.send_keys(Keys.ENTER)
        except:
            pass

    def goto(self, kw):
        try:
            print(f'Brwoser navigating to: {kw}')
            # self.driver.get(self.resource['BASEURL'])
            self.driver.get(kw)
        except:
            pass

    def capture(self):
        path = generated_content_path
        info = self.driver.current_url         # generate url from driver
        print(path)
        print(info)
        self.element.screenshot(f'{path}\_generated_image.png')
        print('Captured')



''' Commands with exeption handling End '''



'''  Platform disintegration Start'''
def _queuFunction(kw):
    functions = kw.split(',')
    func = functions if kw.find(',') > 0 else [kw]
    store = list()
    for index in func:
        store.append(index)
    return store



# for each state to translate during validation
def key_w(key):
    key = key
    store = []
    for index in key:
        store.append(key[index])
    return store

'''  Platform disintegration End'''


# data = {
#         "userID": "user_4274f107-8e5e-11ee-bcef-f057a6886575",
#         "number": "7495815114036",
#         "credential": "b'Data'",
#         "url": "http://smith-henderson.com/",
#         "trial": "2",
#         "time_stamp": "2019-09-29 08:28:50",
#         "platform": "RESULT_FUNAAB",
#         "pskey": "queen_4274f108",
#         "status": "Pending",
#         "history": {
#             "Error": "True",
#             "Opsmsg": "ServerError",
#             "Result": "blob->remove this before save"
#         }
#     }


# if __name__ == '__main__':
#     p = PlatformLoader(data)

    