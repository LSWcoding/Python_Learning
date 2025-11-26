#itertool:product,permutations,combinations,accumulate,groupby and infinite iterators
from itertools import product, permutations, combinations, accumulate, groupby, count, cycle, repeat
a = [1, 2]
b = [3, 4]
prod = product(a, b)
print(prod)  # Output: <itertools.product object at ...>
print(list(prod))  # Output: [(1, 3), (1, 4), (2, 3), (2, 4)]

#with repeat
repeat_a = [1, 2]
repeat_b = [3]
repeat_prod = product(repeat_a, repeat_b, repeat=2)
print(list(repeat_prod))  # Output: [(1, 3, 1, 3), (1, 3, 2, 3), (2, 3, 1, 3), (2, 3, 2, 3)]

#permutations
perm_a = [1, 2, 3]
perm = permutations(perm_a)
print(list(perm))  # Output: [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
perm_2 = permutations(perm_a, 2)#specifying length of each permutation
print(list(perm_2))  # Output: [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

#combinations
comb_a = [1, 2, 3, 4]
comb = combinations(comb_a, 2) #no repeated number in (n r)
print(list(comb))  # Output: [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]

#combinations with replacement
comb_wr = combinations_with_replacement(comb_a, 2)
print(list(comb_wr))  # Output: [(1, 1), (1, 2), (1, 3), (1, 4), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4)]
#there are repeated numbers in (n r)

#accumulate
acc_a = [1, 2, 3, 4]
acc = accumulate(acc_a)
print(list(acc))  # Output: [1, 3, 6, 10]

#with operator
import operator
acc_mul = accumulate(acc_a, func=operator.mul)
print(list(acc_mul))  # Output: [1, 2, 6, 24]
#max function
acc_max = [1, 5, 2, 8, 3]
accum_max = accumulate(acc_max, func=max)
print(list(accum_max))  # Output: [1, 5, 5, 8, 8]

#groupby
group_a = [1,2,3,4,5]

def smaller_than_3(x)
    return x<3

group_obj = groupby(group_a, key = smaller_than_3)
print(group_obj)
# do the same thing with lambda function
group_obj = groupby(group_a,key = lambda x: x < 3)

person ={'name'}

person =[{'name':'Tim','age':25},{'name':'Dan','age':25},{'name':'Lisa','age':27},{'name':'Klare','age':28}]

person_group_obj = groupby(person, key = lambda x:['age'])
for key, value in person_group_obj:
    print(key,list(value))
    
#count

for i in count(10)
    print[i]
    if i == 15:
        break
#count from 10 and end when 15

#cycle
cycle_a = [1,2,3]
for i in cycle(cycle_a)
    print i 

#repeat
for i in repeat(1,4):#repeat 1 in 4 times
    print(i)
