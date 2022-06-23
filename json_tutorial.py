#Python dict oluşturup json formatına çevirmek
#Ayrıca serialization veya encoding olarak da geçiyor.

import json

person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}

personJSON = json.dumps(person, indent=4, seperators=('; ','= '),
            sort_keys= True)
print(personJSON) # bize False'u false olarak döndürdüğünü göreceksin
#indent bize girintili şekilde gösteriyor.
#seperatorsları görüldüğü şekilde değiştirebilirsin fakat önerilmiyor!
#sort_keys = True keyleri alfabetik olarak sıralıyor.


with open('person.json', 'w') as file: #bize person.json şeklinde bir json dosyası oluşturuyor.
    json.dump(person, file, indent=4)#json.dumps stringler içinmiş :D o yüzden burda bu şekilde kullanıyoruz.


#Json dosyasını Python objesine çevirmek
#Ayrıca deserialization veya decoding olarak da geçiyor.


person = json.loads(personJSON) #json.loads string olarak okumak içinmiş :D :D :D
print(person)

with open('person.json', 'r') as file:#yukarıdaki metodla aynı şey aslında
    person = json.load(file)#burda load kullandık
    print(person)

#Burdan önce normal bir dict ile çalıştık custom bir obje ile çalışmak istersek;

class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User('Max',27)

#Bu fonksiyon bizim custom olarak encoding yaptığımız bir fonksiyon.
def encode_user(o): #eger bu fonksiyonu tanımlamasaydık TypeError hatası verecekti
    if isinstance(o, User): #bir nesnenin bir sınıfın mı yoksa bir alt sınıfının mı örneği olduğunu döndürür. 
        return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
    else:
        raise TypeError('Object of type User is not JSON serializable')

userJSON = json.dumps(user, default = encode_user)#dump veya dumps kullanılabilir çünkü encode_user metodunu tanımladık.
print(userJSON)       

#Custom class için ikinci metod olarak

from json import JSONEncoder
class UserEncoder(JSONEncoder):

    def default(self, o):
        if isinstance(o, User): #bir nesnenin bir sınıfın mı yoksa bir alt sınıfının mı örneği olduğunu döndürür. 
            return {'name': o.name, 'age': o.age, o.__class__.__name__: True}
        return JSONEncoder.default(self, o)

userJSON = json.dumps(user, cls = UserEncoder) #cls => class
print(userJSON)       

#Son olarak bu encoder'ı da kullanabiliriz
userJSON = UserEncoder().encode(user)
print(userJSON)

#Decoding custom objects

def decode_user(dct): #dict olarak objeyi alıyor
    if User.__name__ in  dct:#encoding_user fonksiyonunda user class name'i key olarak tanımladık burda da key'in dict içinde olup olmadaığını kontrol ediyoruz 
        return User(name=dct['name'], age=dct['age'])
    return dct

user = json.loads(userJSON, object_hook=decode_user)
print(user.name) #yukarıdaki custom decoding fonksiyonu olmasaydı dict olarak döndüreceği için hata mesajı alırdık.






