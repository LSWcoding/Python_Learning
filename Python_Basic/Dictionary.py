#Dictionary: Key-Value Pairs, Unordered, Mutable
my_dict = {"name":"Max", "age":28, "city":"New York"}
print(my_dict)  # Output: {'name': 'Max', 'age': 28, 'city': 'New York'}

# creating a dictionary using the dict() function
my_dict2 = dict(name="Anna", age=22, city="London")#no need to use quotes for keys
print(my_dict2)  # Output: {'name': 'Anna', 'age': 22, 'city': 'London'}

# Accessing values
print(my_dict["name"])  # Output: Max

# Adding a new key-value pair
my_dict["job"] = "Engineer"#following  the last key-value pair
print(my_dict)  # Output: {'name': 'Max', 'age': 28, 'city': 'New York', 'job': 'Engineer'}
# Modifying an existing value
my_dict["age"] = 29
print(my_dict)  # Output: {'name': 'Max', 'age': 29, 'city': 'New York', 'job': 'Engineer'}

# Removing a key-value pair
del my_dict["city"]
print(my_dict)  # Output: {'name': 'Max', 'age': 29, 'job': 'Engineer'}

#Pop method
age = my_dict.pop("age")
print(age)  # Output: 29

# popitem method (removes and returns the last inserted key-value pair)
item = my_dict.popitem()
print(item)  # Output: ('job', 'Engineer')

#Checking existence of a key
if "name" in my_dict:
    print("Name exists in the dictionary")  # Output: Name exists in the dictionary
else:
    print("Name does not exist in the dictionary")
# try-except block to handle unexpected elements
try:    
    print(my_dict["lastname"])
except KeyError:
    print("Key 'lastname' does not exist in the dictionary")  # Output: Key 'lastname' does not exist in the dictionary

for key, value in my_dict.items():
    print(f"{key}: {value}")  # Output: name: Max, since other items were removed

for key in my_dict.keys():
    print(key)  # Output: name: Max

my_dict_copy = my_dict.copy()
#my_dict_copy = my_dict is wrong as both will point to same memory location,modifications in one will reflect in other    
print(my_dict_copy)  # Output: {'name': 'Max'}
my_dict_copy2 = dict(my_dict)#another way to copy
print(my_dict_copy2)  # Output: {'name': 'Max'}

#merging two dictionaries
Info1 = {"name":"John", "age":30}
Info2 = {"city":"Boston", "job":"Developer","name":"Doe"}
Info1.update(Info2)#if same key is present in both, value from second dict will be taken
print(Info1)  # Output: {'name': 'Doe', 'age': 30, 'city': 'Boston', 'job': 'Developer'}

#tuple as key
mytuple = (8, 7)
sum_dict = {mytuple: 15}
print(sum_dict)  # Output: {(8, 7): 15}
#list as key will give error because lists are mutable