# -*- coding: utf-8 -*-

from threading import Thread, Lock

lock = Lock()

class Task(Thread):
    def __init__(self, index):
        Thread.__init__(self)
        
        self.index = index;
        
    def run(self):
        lock.acquire()
        print("Hello from thread " + str(self.index))
        lock.release()
            
def main():
    threadCount = 10
    threads = []
    
    for i in range(0, threadCount):
        task = Task(i)
        threads.append(task)
        task.start()
        
    for i in range(0, threadCount):
        threads[i].join()
            
if __name__ == "__main__":
    main()        