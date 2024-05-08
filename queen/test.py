# read all file 
import os, sys, json

path = "Dependencies\commands"
bulk = []
def readAll(path):
    files = os.listdir(path)
    for file in files:
        dir = os.path.dirname(f"{path}\\{file}")
        bulk.append(readJson(f'{dir}\\{file}'))
    return bulk

    # read each and append to a list

def readJson(file):
    with open(file, 'r') as file:
        return json.load(file)

if __name__ == '__main__':
    print(readAll(path))
    
# original
/html/body/div[1]/div/div[2]/div[4]/div/div[3]/div/div[2]/div[3]/div[last()]/div/div/div[1]/div[1]/div[1]/div/div[1]/div/span[1]

#expired 
/html/body/div[1]/div/div/div[4]/div/div[1]/div/div/div[2]/div/div[1]/p


#xxjs
/html/body/div[1]/div/div[2]/div[3]/div/div[2]/div[1]/div/div/div[1]/div/div/div/div[2]/div[1]/div[1]/div/span


/html/body/div[1]/div/div[2]/div[4]/div/div[3]/div/div[2]/div[2]/div[last()]/div/div/div[1]/div[1]/div[1]/div/div[1]/div/span[1]/span