#Sets:unorderd,mutable,no duplicate elements
#Creating a set
my_set = {1, 2, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}
my_setwith_constructor = set([1, 2, 3, 4, 5])#use function/constructor set() to create a set
print(my_setwith_constructor)  # Output: {1, 2, 3, 4, 5}

my_set_no_duplicates = {1, 2, 2, 3, 4, 4, 5}
print(my_set_no_duplicates)  # Output: {1, 2, 3, 4, 5}

set_from_string = set("hello")
print(set_from_string)  # Output: {'h', 'e', 'l', 'o'},in arbitrary order,not certainly {'h', 'e', 'l', 'o'}

empty_set = {}
print(type(empty_set)) # Output: <class 'dict'>,because {} creates an empty dictionary
empty_set_correct = set()
print(type(empty_set_correct)) # Output: <class 'set'>

#Adding elements
empty_set_to_add = set()
empty_set_to_add.add(1)
empty_set_to_add.add(2)
empty_set_to_add.add(3)
print(empty_set_to_add)  # Output: {1, 2, 3}

#Removing elements
set_to_remove = {1, 2, 3, 4, 5}
set_to_remove.remove(3)  # Raises KeyError if 3 is not found
print(set_to_remove)  # Output: {1, 2, 4, 5}
set_to_remove.discard(4)  # Does not raise an error if 4 is not found
print(set_to_remove)  # Output: {1, 2, 5}
set_to_remove.pop()  # Removes and returns an arbitrary element
print(set_to_remove)  # Output: Remaining elements after pop

#Set iteration
set_to_iterate = {1, 2, 3, 4, 5}
for i in set_to_iterate:
    print(i)  # Output: 1 2 3 4 5 in arbitrary order

#Checking membership
set_to_check = {1, 2, 3, 4, 5}
if 3 in set_to_check:
    print("3 is in the set")  # Output: 3 is in the set
else:
    print("3 is not in the set")

#Union
odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8} 
primes = {2, 3, 5, 7}

u = odds.union(evens)
print(u)  # Output: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

i = odds.intersection(evens)
print(i)  # Output: set() because there are no common elements between odds and evens
i2 = odds.intersection(primes)
print(i2)  # Output: {3, 5, 7} because these are common elements between odds and primes

#Difference
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
diff = set_a.difference(set_b)
print(diff)  # Output: {1, 2, 3} because these elements are in set_a but not in set_b,collection a minus collection b
diff2 = set_b.symmetric_difference(set_a)
print(diff2)  # Output: {1, 2, 3, 6, 7, 8} because these elements are in either set_a or set_b but not in both
#note:diff1 and diff2 are new sets,original sets set_a and set_b have not been modified

set_a.intersection_update(set_b)
print(set_a)  # Output: {4, 5},set_a is modified to keep only elements also in set_b
#Syntax: setname.xxx_update(other_set),to modify the original set,xxx: union,intersection,difference,symmetric_difference

#Subset and Superset
set_x = {1, 2, 3}
set_y = {1, 2, 3, 4, 5}
print(set_x.issubset(set_y))  # Output: True,because all elements of set_x are in set_y
print(set_y.issuperset(set_x))  # Output: True,because set_y contains all elements of set_x
print(set_x.isdisjoint(set_y))  # Output: False,because set_x and set_y have common elements
set_z = {6, 7, 8}
print(set_x.isdisjoint(set_z))  # Output: True,because set_x and set_z have no common elements

#Set copy
original_set = {1, 2, 3, 4, 5}
copied_set = original_set.copy()
#not copied_set=original_set,because this way both variables point to the same set in memory,modifying one will affect the other
print(copied_set)  # Output: {1, 2, 3, 4, 5}

copied_set2 = set(original_set)#another way to copy a set
print(copied_set2)  # Output: {1, 2, 3, 4, 5}

#fronzenset:immutable set
frozen = frozenset([1, 2, 3, 4, 5])
print(frozen)  # Output: frozenset({1, 2, 3, 4, 5})
#frozen.add(6)  # Raises AttributeError because frozenset is immutable

