from distutils.log import error
import requests
import time
import concurrent.futures
import threading
import psycopg2

def service(url):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(get_service, url)
    

def get_service(url):
    response = requests.get(url)
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
    url_site = ["https://jsonplaceholder.typicode.com/photos"]
    service(url_site)
    end_time = time.time() - init_time
    print(end_time)