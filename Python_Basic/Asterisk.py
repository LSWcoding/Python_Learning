#******
#multiplication
result = 2*4
#power operation
result = 2**4
zeros = [0]*10#repeat elements,also valid for string,tuple
def foo(*args,**kwargs):#multiple arguments
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key,kwargs[key])
foo(1,2,3,4,5,six =6,seven=7)

def foo2(a,b,*,c):#to limit the arguments after * to only keyword argument
    print(a,b,c)

foo2(1,2,c = 3)
#to unpack,also valid for dictionary and tuple.for dictionary the name of the key should be the same as the parameter and the result is only the value
def foo3 (a,b,c):
    print(a,b,c)

my_list =[ 0,1,2]
foo3(*my_list)

#used for unpacking container
numbers = [1,2,3,4,5,6]
*beginning,last = numbers
print(beginning)#[1,2,3,4,5]
print(last)#6
#the result will alwaysbe list no matter numbers is list or tuple
numbers2 =[1,2,3,4,5,6]
beginning2,*last2 = numbers2
print(beginning2)#1
print(last2)#[2,3,4,5,6]

numbers3 =[1,2,3,4,5,6]
beginning3,*middle3,last3 =numbers3
print (beginning3)#1
print(middle3)#[2,3,4,5]
print(last3)#6
 
numbers4 =[1,2,3,4,5,6]
beginning4,middle4,secondlast4,last4 = numbers4
print(beginning4,middle4,secondlast4,last4)#1,[2,3,4],5,6

#unpack multiple element in to a list
my_tuple2 = (1,2,3)
my_list2 = [5,6,7]
my_set2 = {8,9}
new_list =[*my_tuple2,*my_list2,*my_set2]
print(new_list)#[1,2,3,4,5,6,7,8,9]

dict_a = {'a':1,'b':2}
dict_b ={'c':3,'d':4}
my_dict = {**dict_a,**dict_b}
print(my_dict)#merging dict_a and dict_b

