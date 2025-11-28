#shallow copy:one level deep,only references of nested child obejects
#deep copy: full independent copy

#false way
"""
org = 5
cpy = org
cpy =6
print(org)#5
print(cpy)#6
org and cpy refer to the same adress
"""

import copy

"""org =[0,1,2,3,4]
#shallow copy
#cpy = copy.copy(org)
#or
#cpy =org.copy
#or
#cpy =list(org)
#or
cpy = org[:]
cpy[0] = -10
print(org)#[-10,1,2,3,4]
print(cpy)#[0,1,2,3,4]
"""
org = [[0,1,2,3,4],[5,6,7,8,9]]
cpy =copy.copy(org)
#cpy =copy.deepcopy(org),to solve the problem with deepcopy
cpy[0][1] = 10
print(cpy)#[[0,-10,2,3,4],[5,6,7,8,9]]
print(org)#[[0,-10,2,3,4],[5,6,7,8,9]]
#shallow copy is one level deep 
