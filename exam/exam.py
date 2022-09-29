import threading
import time
import random

mutex = [threading.Lock(),threading.Lock(),threading.Lock(),threading.Lock(),threading.Lock(),threading.Lock(),threading.Lock(),threading.Lock(),threading.Lock()]



def usandoPalillos(id):
    izquierdo = mutex[id]
    derecho = mutex[(id+1)%8]
    
    
    izquierdo.acquire() #Ocupa el palillo que le corresponde por defecto
    
    if derecho.acquire(blocking=False):
        return True
    else: 
        izquierdo.release() #puesto que no tiene el derecho, libera
        return False

def dejarPalillos(id):
    izquierdo = mutex[id]
    derecho = mutex[(id+1)%8]
    
    izquierdo.release()
    derecho.release()

def crito(id):
    i = False
    iter = 0
    
    while i == False:
        enUso = usandoPalillos(id)
    
        if enUso:
            print("Persona: "+str(id+1)+" comiendo")
            print("Persona: "+str(id+1)+" uso palillos: "+str(id+1)+" y "+str(((id+1)%8)+1))
            time.sleep(random.randint(2, 5))
            dejarPalillos(id)
            print("Persona: "+str(id+1)+" terminó de comer")
            i==True
            break
        else:
            if iter < 5:
                print("Persona: "+str(id+1)+" esperando")
                iter=iter+1
                
        
        

class Persona(threading.Thread):
     def __init__(self, id):
        threading.Thread.__init__(self)
        self.id=id

     def run(self):
        #mutex.acquire() #Inicializa semáforo , lo adquiere
        crito(self.id)
        #mutex.release() #Libera un semáforo e incrementa la varibale

hilos = [Persona(0), Persona(1), Persona(2), Persona(3), Persona(4), Persona(5), Persona(6), Persona(7)]


for h in hilos:
    h.start()