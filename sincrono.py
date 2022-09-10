from distutils.log import error
from mimetypes import init
from urllib import response
import psycopg2
import requests
import time

def service():
    print("Hola Service")
    get_service()
    

def get_service():
    response = requests.get("https://jsonplaceholder.typicode.com/photos")
    if response.status_code == 200 :
        data = response.json()
        for dataout in data:
            print(dataout["title"])
        write_db(data)
    else:
        pass


def connect_db():
    try:
        conexion = psycopg2.connect(host="localhost", database="DatosJson", user="postgres", password="203455_SQLDesktop")
        print("Conexion exitosa")
        return conexion
    except psycopg2.Error as e:
        print("Ocurrió un error al conectar a PostgreSQL: ", e)
        return error
    

def write_db(data):
    conect = connect_db()
    cur = conect.cursor()
    for dataout in data:
        cur.execute("INSERT INTO datos (title) VALUES ('"+dataout['title']+"')")
    conect.commit()
    pass


if __name__ == "__main__":
    init_time = time.time()
    service()
    end_time = time.time() - init_time
    print(end_time)