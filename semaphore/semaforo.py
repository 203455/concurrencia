from threading import Thread, Semaphore
semaforo = Semaphore(1)

def critico(id):
    global x;
    x=x+id
    print("hilo = "+str(id)+" =="+str(x))
    x=1
    
class Hilo(Thread):
    def __init__(self, id):
        Thread.__init__(self)
        self.id=id
        
    def  run(self):
        semaforo.acquire()
        critico(self.id)
        semaforo.release()

threads_semaphoore = [Hilo(1), Hilo(2), Hilo(3)]
x=1;
for t in threads_semaphoore:
    t.start()