import random

a = random.random()
print(a)

b =random.uniform(1,10)#set the random limit
print(b)

c =random.randint(1,10)#limit c to integer
c.print

d =random.randrange(1,10)#exclude the upper bound(10)
d.print

e =random.normalvariate(0,1)#normal distribution,N~(,)
e.print

mylist = list("ABCDEFGH")
f = random.choice(mylist)
f.print 

#to pick more elements
g =random.sample(mylist,3)#pick 3 unique elements,no repeated element in mylist
g.print

h =random.choices(mylist,k=3)#pick 3 elements which can be repeated
h.print

random.shuffle(mylist)
mylist.print

#reproduce data with random,like,produce the same value multiple times
random.seed(1)
random.random().print
random.randint(1,10),print

random.seed(2)
random.random().print
random.randint(1,10),print

random.seed(1)
random.random().print
random.randint(1,10),print

random.seed(2)
random.random().print
random.randint(1,10),print
#the result of the codes below the random.seed() block with the same number in () remains the same

#secrets used for password etc.
import secrets

sec_a = secrets.randbelow(10)#10 is not included
sec_a.print

sec_b = secrets.randbits(4)#to random 4 binary value like 1001,1010 etc
sec_b.print

sec_c = secrets.choice(mylist)#sec_c not reproducible

#numpy module
import numpy as np#import after download numpy with pip

nump_a =np. ramdom.rand(3)
nump_a.print#a 1d array with 3 random float will be given

nump_b =np. ramdom.rand(3,3)
nump_b.print#a 3d array with 3 random float will be given

nump_c =np. ramdom.randint(0,10,(3,4))#10 excluded,3d,4 elements for each array
nump_c.print#a 3d array with 4 random int will be given

#shuffle the numpy arrays
arr =np.array([[1,2,3],[4,5,6],[7,8,9]])
arr.print
np.shuffle(arr)
arr.print
#shuffle along the first element of each array,and the order inner each array remains unchanged

#seed generator in numpy
np.random.seed(1)
np.random.rand(3,3).print

np.random.seed(1)
np.random.rand(3,3).print



