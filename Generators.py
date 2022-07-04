#Generators her seferinde 1 kere verilen komutu döndürür ve bunu tembel bir biçimde yapar :).
#Biz bir kere daha çalıştırmadığımız sürece devam etmez.
#Generators büyük verilerle çalışırken hafızada büyük tasarrufa yol açar.

def mygenerator():
    yield 1 #Yield'ın getiri anlamı var. Return gibi bir işlevde.
    yield 2
    yield 3

g = mygenerator()
print(g)#Sadece objeyi verir

for i in g:
    print(i)

value = next(g) #1 yazdırır ve durur.
print(value)

#2'yi de yazdırmak için...
value = next(g) #2 yazdırır ve durur.
print(value)

#4. defa çalışmaz StopIteration hatası alırız.

print(sum(g))
print(sorted(g))


def countdown(num): #Num başlama sayısı.
    print('Starting')
    while num > 0:
        yield num
        num -= 1

cd= countdown(4) #output vermez.

value = next(cd)#4 yazdırır.
print(value)

print(next(cd))#3 yazdırır.



def firstn(n):#Burada bütün sayıları saklamak için bellekte büyük bir liste oluşturduk.
    nums =  []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums

def firstn_generator(n):#Burada da listeye gerek kalmadan bellekten tasarruf edip aynı sonucu aldık.
    num = 0
    while num < n:
        yield num
        num +=1



mylist = firstn(10)
print(mylist)
print(sum(mylist))#i
print(sum(firstn_generator(10)))#ii
#i ve ii aynı sonucu verir.

import sys
#Byte cinsinden kapladıkları alan 1 milyon değeri verirsek daha net anlaşılır.
print(sys.getsizeof(firstn(10)))
print(sys.getsizeof(firstn_generator(10)))

#Generatorsun avantajlarından biri de istediğimiz değere kadar olan tüm sayıları,
#hesaplamak zorunda kalmıyoruz.


def fibonacci(limit):#Fibonacci dizisi örneği.
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b


fib = fibonacci(30)
for i in fib:
    print(i)

mygenerator1 = (i for i in range(10) if i % 2 == 0)
mylist1 = [i for i in range(10) if i % 2 == 0]

#sys.getsizeof() kullanarak ikisi arasındaki farkı görebilirsin.



