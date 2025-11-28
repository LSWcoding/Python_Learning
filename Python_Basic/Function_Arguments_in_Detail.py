#Parameter:Variables that are defined or used inside parentheses where defining a function
#Argument:Values passed for parameters while calling a function 
"""
def print_name(name):#name:Parameter
    print(name)

print_name('Alex')#'Alex':Argument

def foo(a,b,c,d = 4):#d = 4 is default argument,it should be the last position
    print(a,b,c,d)

foo(1,2,3)#positional arguments
foo(a=1,c=2,b=3)#key word arguments,the order is not important
foo(1,b=2,c=3)#mixed arguments and no positional arguments after key word arguments
"""
#variable length arguments
"""
def foo(a,b,*args,**kwargs):#mark parameter with*,any numbers of positional arguments could be passed to the function,with** pass any numbers of keyword arguments to the function
    print(a,b)
    for arg in args:#args is a tuple
        print(arg)
    for key in kwargs:#kwargs is a dictionary
        print(key,kwargs[key])


foo(1,2,3,4,5,six =6,seven =7)
"""
#force keyword arguments
"""
def foo(a,b,*,c,d):#any parameter after* must be a keyword argument
    print(a,b,c,d)

foo(1,2,c=3,d=4) 

def foo(*args,last):#last should be a keyword argument
"""
#unpack argument
"""
def foo(a,b,c):
    print(a,b,c)

my_list = [0,1,2]
#unpack the list to the arguments the length of both should be match.Tuple is also valid for this
foo(*my_list)
my_dict = {'a' : 1,'b' :2,'c' : 3}
foo(**my_dict)#unpack dictionary
"""

"""
#local and global variable
def foo():
    global  number
    x = number
    number = 3
    print('number inside funtion',x)#0
    
    global  number
    x = number #here x = 0 because number = 0 outside
    number = 3 #here the number is modified so print(number) outside is 3
    

number = 0

foo()
print(number)#3
"""
