"""
Most os thease code was taken from https://thispointer.com/python-check-if-a-process-is-running-by-name-and-find-its-process-id-pid/
"""

import psutil
import time

def checkIfProcessRunning(processName):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;

def findProcessIdByName(processName):
    '''
    Get a list of all the PIDs of a all the running process whose name contains
    the given string processName
    '''

    listOfProcessObjects = []

    #Iterate over the all the running process
    for proc in psutil.process_iter():
       try:
           pinfo = proc.as_dict(attrs=['pid', 'name', 'create_time'])
           # Check if process name contains the given name string.
           if processName.lower() in pinfo['name'].lower() :
               listOfProcessObjects.append(pinfo)
       except (psutil.NoSuchProcess, psutil.AccessDenied , psutil.ZombieProcess) :
           pass

    return listOfProcessObjects;

def main(processNameS):

    print("*** Check if a process is running or not ***")

    # Check if any chrome process was running or not.
    if checkIfProcessRunning(processNameS):
        print('Yes a {} process was running'.format(processNameS))
    else:
        print('No {} process was running'.format(processNameS))



    print("*** Find PIDs of a running process by Name ***")

    # Find PIDs od all the running instances of process that contains 'chrome' in it's name
    listOfProcessIds = findProcessIdByName(processNameS)

    if len(listOfProcessIds) > 0:
       print('Process Exists | PID and other details are')
       for elem in listOfProcessIds:
           processID = elem['pid']
           processName = elem['name']
           processCreationTime =  time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(elem['create_time']))
           print((processID ,processName,processCreationTime ))
    else :
       print('No Running Process found with given text')


    print('** Find running process by name using List comprehension **')

    # Find PIDs od all the running instances of process that contains 'chrome' in it's name
    procObjList = [procObj for procObj in psutil.process_iter() if processNameS in procObj.name().lower() ]

    for elem in procObjList:
       print (elem)


if __name__ == '__main__':
   main('firefox')
