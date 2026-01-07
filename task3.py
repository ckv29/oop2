import time
import threading

def long_task(name):
    print(f"{name} started")
    time.sleep(3)
    print(f"{name} ended")
  

t1 = threading.Thread(target=long_task,args=("Thread 1",))
t2 = threading.Thread(target=long_task,args=("Thread 2",))

t1.start()
t2.start()

t1.join()
t2.join()

print('All finished')
