#encode
import json
person ={"name":"John",
         "age":"30",
         "city":"New York",
         "hasChildren":"False",
         "titles":["engineer","programmer"]
         }

personJson = json.dumps(person,indent=4,sort_keys=True)#conert person to a json object
print(personJson)

with open('person.json','w') as file:
    json.dump(person,file,indent=4)

#decode
#convert person to a file,w means write

person =json.loads(personJson)
print(person)
#convert the json object back to python object
with open('person.json', 'r') as file:
    person = json.load(file)
    print(person)
#convert from a json file

#to encode a custom object to a json obejct

class User:
    def ___init___(self,name,age):
        self.name = name
        self.age = age

user = User('Max',27)

def encode_user(o):
    if isinstance(o,User):
        return{'name':o.name,'age':o.age, o.__class__.__name__: True}
    else:
        raise TypeError('Object of type User is not JSON serializable')


UserJson = json.dumps(user,default=encode_user)
print(UserJson)

#another way to encode custom object to a json object
from json import JSONEncoder

class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o,User):
            return{'name':o.name,'age':o.age, o.__class__.__name__: True}
        return JSONEncoder.default(self,o)

UserJson =UserEncoder().encode(user)

#custom decoding method
def decode_user(dict):
    if User.__name__ in dict:
        return User(name=dict['name'],age=dict['age'])
    return dict



#decode
user =json.loads(UserJson,object_hook=decode_user)
print =(type(user))
print(user.name)

