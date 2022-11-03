from threading import Thread
from time import sleep

class Cocinero(Thread):
    def __init__(self, conditionC,order):
        Thread.__init__(self)
        self.conditionC = conditionC
        self.order = order
        
    def cocinar(self, client):
        self.conditionC.acquire()
        print(f"Cocinero esta cocinando el platillo del cliente {client}")
        sleep(10)
        self.order[1] = True
        self.conditionC.notify()
        self.conditionC.release()
        print("Cocinero: Estoy descasando")