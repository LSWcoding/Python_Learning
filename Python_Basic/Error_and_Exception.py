#error could be either a syntax error or an exception

#syntax error

#false:
#syntax error can occur

#a = 5 print(a)

#a = 5
#print(a))

#correct:
#a = 5
#print(a)

#exception:error occurs when code is excuted even if the code syntax is correct

#type error
# a = 5 + '10' int+string

#import error
#import somemodule somemodule dose not exist

#name error
#a = 5
#b = c  c has not been defined

#FileNotFound error
#f = open('somefile.txt),somefile.txt does not exist

#Value error
#a = [1,2,3]
#a.remove(4),4 is not in a
#print(a)
#Index error
#a[4]
#print(a)

#key error
#my_dict = {'name':'Max'}
#my_dict['age']

#Raise Exception
x = -5
if x < 0:
    raise Exception('x should be posive')

#assert statement for Exceptions raising
assert_x = -5
assert(x>=0),'x is not positive'#syntax: assert(conditions),'phrases'


#handle exceptions
try:
    try_a = 5/0# this leads to ZeroDevisionError
except:
    print('an error occurs')#the program will not stop at try block and will continue in except block

#to catch the type of the exceptions
try:
    try_a = 5/0
except Exception as e:
    print(e)#e represent the error type,which is 'division by zero'here
# Exception as e:
# print(e)
#is used when the error type is not clear and should be catched

#when the error type is clear:
try:
    clear_a = 5/0
    clear_b = clear_a + '10'
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print('everything is fine')
finally:#this block always runs no matter the error occurs or not
    print('cleaning up...')

#define Exception
class ValueTooHighError(Exception):
    pass
#this Error is always valid

class ValueTooSmallError(Exception):
    def ___int___(self,message,value):
        self.message = message
        self.value = value 


def test_value(x):
    if x > 100:
        raise ValueTooHighError('value is too high')
    if x < 5:
        raise  ValueTooSmallError('Value is too small',x)

test_value(200)

try:
    test_value()
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message ,e.value)


