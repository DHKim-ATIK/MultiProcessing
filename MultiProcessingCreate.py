from concurrent.futures import thread
from multiprocessing import Process,freeze_support
from threading import Thread
from datetime import datetime

def ProcessThreadFunction():
    print("Process or Thread created")

if __name__=="__main__":
    
    freeze_support()

    print(str(datetime.now())+"Create Process start")
    process=Process(target=ProcessThreadFunction)
    process.start()
    process.join()
    print(str(datetime.now())+"Process join done")
    print(str(datetime.now())+"Create Thread start")
    worker=Thread(target=ProcessThreadFunction)
    worker.start()
    worker.join()
    print(str(datetime.now())+"Thread join done")