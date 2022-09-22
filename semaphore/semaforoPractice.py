from threading import Thread, Semaphore
from pytube import YouTube
semaforo = Semaphore(1)

yt_videos = [
    'https://youtube.com/shorts/1UNnitK-02c?feature=share', 
    'https://youtube.com/shorts/aJZ-BeUgMLg?feature=share',
    'https://youtube.com/shorts/tsUEoqa8Frw?feature=share',
    'https://youtube.com/shorts/OvIfchxfvKU?feature=share',
    'https://youtube.com/shorts/qu3GD9lDAHA?feature=share'
]

def critico(id):
    yt = YouTube(yt_videos[id])
    yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
    print(f'{yt_videos[id]} was downloaded...')
    
class Hilo(Thread):
    def __init__(self, id):
        Thread.__init__(self)
        self.id=id
        
    def  run(self):
        semaforo.acquire()
        critico(self.id)
        semaforo.release()

threads_semaphoore = [Hilo(0), Hilo(1), Hilo(2), Hilo(3), Hilo(4)]

for t in threads_semaphoore:
    t.start()