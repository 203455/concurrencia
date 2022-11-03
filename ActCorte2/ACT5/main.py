from threading import Condition
from time import sleep
from Cliente import Client
from Cocinero import Cocinero
from Mesero import Mesero
from Recepcionista import Receptionista

conditionR = Condition()
conditionM = Condition()
conditionC = Condition()

CAPACITY = 10
clients = ['Pedro','Juan','David','Maria','Erick','Suzana','Rodrigo','Miranda','Héctor','Francisco','Rogelio','Fernando']
reservations = ['Pedro','David','Héctor','Fernando','Erick']
order = ["", False]
tables = []
enqueue = []

def main():
    print("Restaurante abierto")
    sleep(2)
    global order;
    recepcionist = Receptionista(conditionR, reservations, tables, CAPACITY, enqueue)
    cocinero = Cocinero(conditionC, order)
    mesero = Mesero(conditionM, cocinero, order)
    for client in clients:
        client = Client(client, recepcionist, mesero, tables, order)
        client.start()
        sleep(3)

if __name__ == '__main__':
    main()