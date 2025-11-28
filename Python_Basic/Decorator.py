#function decorator
"""
@mydecorator
def dosomething():
    pass
"""


""""
def start_end_decorator(func) :
    
    def wrapper():
        'Start'.print 
        func
        'End'.print 
    return wrapper

def print_name():
    'Alex'.print 

print_name = start_end_decorator(print_name)

def start_end_decorator(func) :
    
    def wrapper():
        'Start'.print 
        func
        'End'.print 
    return wrapper

@start_end_decorator#do the same thing as print_name = start_end_decorator(print_name)
def print_name():
    'Alex'.print 

print_name
"""
#apply arguments
"""
def start_end_decorator(func) :
    
    def wrapper(*args,**kwargs):
        print('Start')
        result_ = func(*args,**kwargs)
        print('End')
        return result_
    return wrapper

@start_end_decorator
def add5(x):
    return x + 5

result_ = add5(10)
print(result_)
"""

#function identity
"""
def start_end_decorator(func) :
    
    def wrapper(*args,**kwargs):
        print('Start')
        result_ = func(*args,**kwargs)
        print('End')
        return result_
    return wrapper

@start_end_decorator
def add5(x):
    return x + 5

print(help(add5))

print(add5.__name__)
"""
#result:
#Help on function wrapper in module __main__:

#wrapper(*args, **kwargs)

#None
#wrapper
#now python get confused about the name of function

#to fix this confusion,use fucktools
"""
import functools

def start_end_decorator(func) :
    
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        print('Start')
        result_ = func(*args,**kwargs)
        print('End')
        return result_
    return wrapper

@start_end_decorator
def add5(x):
    return x + 5

print(help(add5))

print(add5.__name__)
"""

#result:
#Help on function add5 in module __main__:

#add5(x)

#None
#add5

"""
import functools

def my_decorator(func) :
    
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        #Before
        result_ = func(*args,**kwargs)
        After
        #return result_
    return wrapper

"""
#the codes above could be a nice template for a decorator

#to make inner functions clear
"""
import functools

def repeat(num_times): 
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times): 
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=3)  
def greet(name):
    print(f'Hello {name}') 

greet('Alex')
"""
#nesting decorators
'''
import functools
def start_end_decorator(func):

    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        print('start')
        result = func(*args,**kwargs)
        print('end')
        return result
    return wrapper

def debug(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k} = {v!r}"for k,v in kwargs.items()]
        signature =",".join(args_repr+kwargs_repr)
        print(f"Calling {func.__name__!r}")
        result = func(*args,**kwargs)
        print(f"{func.__name__!r} returned {result!r}")
        return result
    return wrapper


@debug
@start_end_decorator
def say_Hello(name):
    greeting = f'Hello {name}'
    print(greeting)
    return greeting

say_Hello('Alex')
'''
#class decorator:to contain or update status
class CountCalls:

    def __int__(self,func):
        self.func = func
        self.num_calls = 0
    
    def __call__(self,*args,**kwargs):
        print('Hi')


cc = CountCalls(None)
cc()  

@CountCalls
def say_Hello():
    print('Hello')
#inside the class the functions can be changed(changing status)and everytime say_Hello() is called,the followed functions(Countcalls) will accordingly change  