'''
def mygenerator():
    yield 1
    yield 2
    yield 3

g = mygenerator()#create a generator object

for i in g:
    print(i)

value =next(g)
print(value)#1

value =next(g)
print(value)#2

value =next(g)
print(value)#3

value =next(g)
print(value)#error

print(sum(g))

sorted(g).print#return a sorted list
'''


'''
def countdown(num):
    print('Starting')
    while num > 0:
        yield num
        num-= 1

cd = countdown(4)

value = next(cd)
print(value)#Starting

print(next(cd))#4
print(next(cd))#3
print(next(cd))#2
print(next(cd))#1
'''
import sys
def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num +=1
    return nums

def firstn_generator(n):
    num =0
    while num <= n:
        yield num
        num += 1

print(sum(firstn(10)))#45
print(sum(firstn_generator(10)))#45

print(sys.getsizeof(firstn(1000000)))#860764
print(sys.getsizeof(firstn_generator(1000000)))#120