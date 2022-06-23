import logging


logger = logging.getLogger(__name__)
logger.propagate = False
logger.info('Hello from helper')


#Yeni bir logger oluşturuyoruz(üsttekinin aynısı :))
logger1 = logging.getLogger(__name__)

#create handler
#File_h sadece file.log'u kontrol eder, stream_h hepsini
stream_h = logging.StreamHandler()
file_h = logging.FileHandler('file.log')

#level and the format
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

#file.log'da sadece error mesajı gözükür. Çünkü file_h.setLevel'da error olarak atandı.
formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger1.addHandler(stream_h)
logger1.addHandler(file_h)

#Hata mesajları
logger1.warning('This is a warning')
logger1.error('This is an error')

#Ayrıca https://www.youtube.com/watch?v=HGOBQPFzWKo&t=8410s 2:30:50'den itibaren,
#bir config dosyası üzerinde de anlatımı var.



