from random import randint
from time import sleep
from threading import Condition, Thread

class Client(Thread):
    def __init__(self, name, recepcionista, mesero, tables, order):
        Thread.__init__(self)
        self.condition = Condition()
        self.name = name
        self.sentado = False
        self.recepcionista = recepcionista
        self.mesero = mesero
        self.tables = tables
        self.comer = False
        self.order = order
        
        
    def requestServiceToRecepcionist(self):
        self.sentado = self.recepcionista.atender(self.name, 0)
        
    def recibirComida(self):
        print(f"Mesero: llevando la comida al cliente {self.name}")
        self.comer = self.mesero.llevarComida
    
    def comiendo(self):
        print(f"{self.name} esta comiendo")
        sleep(randint(1, 10))
        print(f"{self.name} he terminado de comer y me voy")
        self.tables.remove(self.name)
            
    def run(self):
        print(f"{self.name} he llegado al restaurante")
        self.requestServiceToRecepcionist()
        while self.sentado == False:
                self.sentado = self.recepcionista.atenderCola(self.name)
        if (self.sentado == True):
            print(f"Yo {self.name} sentado y esperando a un mesero")
            self.mesero.attend(self.name)
            while(self.comer == False):
                if self.order[1] == True:
                    self.recibirComida()
                self.condition.acquire()
                if (self.comer == True):
                    self.condition.notify()
                self.condition.release()
            if self.comer:
                self.comiendo()