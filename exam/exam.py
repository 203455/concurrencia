import threading
import time
import random

mutex = threading.Lock()


def crito(id):
    global x;
    x = x-2
    print("Persona "+str(id+1)+" está comiendo")
    print("palillos en espera (mano izquierda de otro comensal): "+str(x))
    time.sleep(random.randint(3,5))
    print("Persona "+str(id+1)+" terminó de comer")
    x = 8
        
        

class Persona(threading.Thread):
     def __init__(self, id):
        threading.Thread.__init__(self)
        self.id=id

     def run(self):
        mutex.acquire() #Inicializa semáforo , lo adquiere
        crito(self.id)
        mutex.release() #Libera un semáforo e incrementa la varibale

hilos = [Persona(0), Persona(1), Persona(2), Persona(3), Persona(4), Persona(5), Persona(6), Persona(7)]

x=8;

for h in hilos:
    h.start()