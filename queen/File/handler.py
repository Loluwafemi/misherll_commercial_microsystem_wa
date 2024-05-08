# open file to be used, must be shared by threads and used by both [maintenance and operator]
from faker import Faker
import uuid
import random, sys, os


# file operator
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from File.operator import disintegrate

# For Generator

fake = Faker()
choice = ["Pending", "Processing", "Processed", "Server Error", "Credential Error", "Done"]
platforms = [
    'EXAMPASS_FUNAAB',
    'WHATSAPP_ACCESS',
    'OTHERS'
]
userID = f'user_{uuid.uuid1()}'
number = f'{fake.msisdn()}'
credential = f'{b"Data"}'
url = f'{fake.url()}'
trial = f'{random.randint(1, 5)}'
time_stamp = f'{fake.date_time()}'
platform = random.choice(platforms)
pskey = f'queen_{str(uuid.uuid1())[:8]}'
status = random.choice(choice)



# Original, populate with maintenance

# userID = f'user_{uuid.uuid1()}'
# number = f'{fake.msisdn()}'
# credential = f'{b"Data"}'
# url = f'{fake.url()}'
# trial = f'{random.randint(1, 5)}'
# time_stamp = f'{fake.date_time()}'
# platform = "Funaab.examPass"
# pskey = f'queen_{str(uuid.uuid1())[:8]}'
# status = random.choice(choice)


def resource_formatter(message):
    recipient = 'message'
    content = 'message'
    status = "pending"
    content = disintegrate(content)

    return {
        "recipient": recipient,
        "task": "read",
        "status": status,
        "request": {
            "type": "CUSTOM_API",
            "state": "END"
        },
        "content": content

    }


def composed_resource(message):
    recipient = 'message'
    content = 'message'
    status = "pending"
    response = None         # API
    response_type = None         # API
    priority = 2

    return {        
        "recipient": recipient,
        "task": "write",
        "status": status,
        "response": response,
        "response_type": response_type,
        "priority": priority


    }

def gen_data():
    return {
        "userID": f'user_{uuid.uuid1()}',
        "number": f'{fake.msisdn()}',
        "credential": f'{b"Data"}',
        "url": f'{fake.url()}',
        "trial": f'{random.randint(1, 5)}',
        "time_stamp": f'{fake.date_time()}',
        "platform": platform,
        "pskey": f'queen_{str(uuid.uuid1())[:8]}',
        "status": random.choice(choice),
        "history": {
            "Error": "True",
            "Opsmsg": "ServerError",
            "Result": "blob->remove this before save"
        }
                
    }


# for _ in range(3):
#     print(gen_data())



