from threading import Thread
from time import sleep

class Receptionista(Thread):
    def __init__(self, conditionR, reservations, tables, capacity, enqueue):
        Thread.__init__(self)
        self.conditionR = conditionR
        self.reservations = reservations
        self.tables = tables
        self.CAPACITY = capacity
        self.enqueue = enqueue
        
    def atender(self, client, op):
        hasReservation = False
        self.conditionR.acquire()
        if (op == 0): print(f"Recepcionista esta Atendiendo al cliente {client}")
        for reservation in self.reservations:
            if (reservation == client):
                if (op == 0): 
                    print(f"Recepcionista el cliente {client} tiene reservación, pasa directamente")
                else: 
                    print(f"Recepcionista el cliente {client} ya tiene una reservación y pasará a centarse")
                hasReservation = True
                self.tables.append(client)
                self.reservations.remove(client)
                sleep(5)
        if (hasReservation == False):
            if (len(self.tables) < self.CAPACITY and (len(self.reservations) + len(self.tables) < self.CAPACITY)):
                self.reservations.append(client)
                print(f"Recepcionista  se le dará una reservación al cliente {client}")
                self.atender(client,1)
                hasReservation = True
            else:
                print(f"Recepcionista {client} no tiene reservación y no hay mesas disponibles, irá a la cola")
                self.enqueue.append(client)
        self.conditionR.notify()
        self.conditionR.release()
        if (hasReservation == True):
            return True
        return False
    
    def atenderCola(self, client):
        if (len(self.tables) < self.CAPACITY and (len(self.reservations) + len(self.tables) < self.CAPACITY)):
            self.reservations.append(client)
            print(f"Recepcionista  1 lugar disponible y se le dará una reservación al cliente {client}")
            self.atender(client,1)
            self.enqueue.remove(client)
            return True
        else:
            return False