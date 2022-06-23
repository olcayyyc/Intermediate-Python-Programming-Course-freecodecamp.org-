import random

a = random.random()#0 ve 1 arasında random float döndürür.
a = random.uniform(1, 10)#1 ve 10 arasında random float döndürür.
a = random.randint(1, 10)#1 ve 10 arasında random integer döndürür.
a = random.randrange(1, 10)# 1 ve 10 arasında random integer döndürür ama 10 dahil değil.
a = random.normalvariate(0, 1)#Normal dağılımdan rastgele bir değer döndürür. ilk arg mü ikinci arg sigma.

mylist = list("ABCDEFGH")
a = random.choice(mylist)#listten rastgele bir eleman seçer.
a = random.sample(mylist, 3)#listten rastgele 3 tane eleman seçer. Aynı elemanı 2 kere seçmez.
a = random.choices(mylist, k=3)#listten rastgelece 3 tane eleman seçer. Aynı elemanı birden fazla daha seçebilir.
a = random.shuffle(mylist)#listedeki elemanların yerlerini karıştırır.

random.seed(1)

import secrets

a = secrets.randbelow(10)#1 ve 10 arasında random integer döndürür. 10 dahil değil
a = secrets.randbits(4)#4 bitlik sayıları döndürür(binary).4 değeri için 0'dan 15'e kadar.

mylist = list("ABCDEFGH")
a = secrets.choice(mylist)#listten rastgele bir eleman döndürür.

import numpy as np

a = np.random.ran(3)#3 elemanlı rastgele bir float listesi döndürür.
a = np.random.ran(3, 3)#3x3 şeklinde bir rastgele float matrisi döndürür.
a = np.random.randint(0, 10, 3)#0'dan 10'a kadar 3 elemanlı bir dizi döndürür
a = np.random.randint(0, 10, (3,3))#3x3 şeklinde 0'dan 10'a kadar rastgele sayı içeren bir matris döndürür.

arr = np.array([[1,2,3], [4,5,6], [7,8,9]])#3x3 matris şekline dönüştürür.
np.random.shuffle(arr)#sadece satır olarak yerlerini karıştırır. listeler arası elemanlar değişmez. [4,1,3] olamaz.
np.random.seed(1)#Rastgele matrisler oluştururken numpy seed modülünü kullanman gerekiyor.


