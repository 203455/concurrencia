from concurrent.futures import thread
from distutils.log import error
import requests
import threading
import psycopg2
from pytube import YouTube
import concurrent.futures


yt_videos = [
    'https://youtube.com/shorts/1UNnitK-02c?feature=share', 
    'https://youtube.com/shorts/aJZ-BeUgMLg?feature=share',
    'https://youtube.com/shorts/tsUEoqa8Frw?feature=share',
    'https://youtube.com/shorts/OvIfchxfvKU?feature=share',
    'https://youtube.com/shorts/qu3GD9lDAHA?feature=share'
]

def downland_video(url):
    yt = YouTube(yt_videos[url])
    yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
    print(f'{yt_videos[url]} was downloaded...')

def get_video():
    for yt_video in range(0,5):
        thr_iter = threading.Thread(target=downland_video, args=[yt_video])
        thr_iter.start()


 
def get_services(dato=0):
    print(f'dato={dato}')
    response = requests.get('https://randomuser.me/api/')
    if response.status_code == 200:
        results = response.json().get('results')
        name = results[0].get('name').get('first')
        print(name)
        
def get_data():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
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
        print(f"Dato: {dataout['title']}")
    conect.commit()
    pass



 
if __name__ == '__main__':
    thr_vid = threading.Thread(target=get_video)
    thr_bd = threading.Thread(target=get_data)
    thr_vid.start()
    thr_bd.start()
    for x in range(0,50):
        thr_iter = threading.Thread(target=get_services, args=[x])
        thr_iter.start()
        #get_services()