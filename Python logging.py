import logging
from this import d
#basicConfig ile ilgili https://docs.python.org/3/library/logging.html
#%(asctime)s = saat ve gün
#%(name)s = isim 
#%(levelname)s = Tür (warning, error vs.)
#%(message)s = karşına çıkacak mesaj
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt = '%m/%d/%Y %H:%M:%S')

#logging helper importladıktan sonra mesajları kaldırabilirsin.
#import Python logging helper
import Pythonlogginghelper
"""logging.debug("This is debug message")
logging.info ("This is info message")
logging.warning("This is warning message")
logging.error("This is error message")
logging.critical("This is critical message")"""


try:
    a=[1,2,3]
    val=a[4]
except IndexError as e:
    logging.error(e, exc_info= True)#IndexError: list index out of range hatası verir.


import traceback
try:
    a=[1,2,3]
    val=a[4]
except:
    logging.error("The error is %s", traceback.format_exc())#Bir üstteki ile aynı hata mesajını verir.
#Ayrıca root: The error is Traceback... şeklinde başlar


#Büyük uygulamardaki çoklu log mesajlarını takip etmek için çoklu dosya tutmak istersek;
#import logging
from logging.handlers import RotatingFileHandler


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

#2 KB'lık dosyalarda log dosyası tutmaya başlar log1, log2, log3 vs.
handler = RotatingFileHandler('app.log', maxBytes=2000, backupCount=5)
logger.addHandler(handler)

for _ in range(10000):
    logger.info('Hello, world!') # çalıştırdığında dosyaları oluşutur ve içerisinde hello world mesajlarını görebilirsin.

import time
from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

#when için s, m, h, d, midnight, w0(gün isimleri w0=pazartesi...)
handler = TimedRotatingFileHandler('timed_test.log', when = 'm', interval=1, backupCount=5)#when='s' ve interval = 5

for _ in range(6):
    logger.info('Hello, world!')
    time.sleep(6)#5 saniyede bir gün saat şeklinde dosya oluşturmaya başlar.

#micro servislerde çalışıyorsan dosyaları json formatında tutmayı öneriyor
#Python'da json formatter var https://pypi.org/project/python-json-logger/
