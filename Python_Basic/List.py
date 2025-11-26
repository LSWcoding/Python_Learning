#List:ordered, mutable, allows duplicate elements
my_list =["banana", "cherry", "apple"]

my_list2 = list()#creating a empty list using the list() function

my_list3 = [5, True, "apple", 3.14,"apple"]#list allows different data types,also allows duplicate elements("apple" is repeated)

item = my_list[0]#accessing elements using indexing(0-based index,from left to right),item will be "banana"

item2 = my_list[-1]#accessing elements using negative indexing(from right to left,-1 is the last element),item2 will be "apple"

for i in my_list:#iterating through a list
    print(i)#prints each element in my_list

if "banana" in my_list:#checking for existence of an element
    print("Yes, 'banana' is in the list")
else :
    print("No, 'banana' is not in the list")

print(len(my_list))#getting the length of the list,prints 3

my_list.append("lemon")#adding an element to the end of the list
print(my_list)#prints ['banana', 'cherry', 'apple', 'lemon']

my_list.insert(1,"blueberry")#inserting an element at a specific index(1)
print(my_list)#prints ['banana', 'blueberry', 'cherry', 'apple', 'lemon']

print(my_list.pop())#removes and returns the last element of the list,prints 'lemon',the print result is 'lemon' and ['banana', 'blueberry', 'cherry', 'apple'] is the current state of my_list
print(my_list)#prints ['banana', 'blueberry', 'cherry', 'apple']

my_list.remove("cherry")#removes the first occurrence of the specified element
print(my_list)#prints ['banana', 'blueberry', 'apple']

my_list.clear()#removes all elements from the list
print(my_list)#prints []

my_list =["banana", "cherry", "apple"]#reinitializing my_list
item = my_list.reverse()#reversing the list
print(my_list)#prints ['apple', 'cherry', 'banana']

my_list.sort()#sorting the list in ascending order
print(my_list)#prints ['apple', 'banana', 'cherry']

new_list = sorted(my_list)#creating a new sorted list without modifying the original list

my_list4 = [0]*5#creating a list with 5 elements,all initialized to 0
print(my_list4)#prints [0, 0, 0, 0, 0]

new_list2 = my_list + my_list4#concatenating two lists
print(new_list2)#prints ['apple', 'banana', 'cherry', 0, 0, 0, 0, 0]

toslice = [1,2,3,4,5,6,7,8,9]
a = toslice[2:5]#slicing the list from index 2 to 4 (5 is exclusive)
print(a)#prints [3, 4, 5],toslice[2] is included, toslice[5] is excluded
b = toslice[:4]#slicing from the start to index 3
print(b)#prints [1, 2, 3, 4]
c = toslice[5:]#slicing from index 5 to the end
print(c)#prints [6, 7, 8, 9]
d = toslice[-4:-1]#slicing using negative indices(from index -4 to -2)
print(d)#prints [6, 7, 8],[-4] is included, [-1] is excluded
e = toslice[:]#copying the entire list
print(e)#prints [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(toslice is e)#prints False,because e is a new list,not a reference to toslice
print(toslice == e)#prints True,because both lists have the same elements
f = toslice[::1]#slicing with a step of 1 (default behavior)
print(f)#prints [1, 2, 3, 4, 5, 6, 7, 8, 9]
g = toslice[::2]#slicing with a step of 2 (every second element)
print(g)#prints [1, 3, 5, 7, 9]
h = toslice[::-1]#slicing with a step of -1 (reverses the list)
print(h)#prints [9, 8, 7, 6, 5, 4, 3, 2, 1]

list_org = ["banana", "cherry", "apple "]
list_copy = list_org.copy()#creating a shallow copy of the list
#list_copy = list(list_org) another way to create a copy of the list
#list_copy = list_org[:] another way to create a copy of the list

#list_copy = list_org this would create a reference,modifying list_copy would also modify list_org

list_copy.append("lemon")#modifying the copied list,original list is unaffected
print("Original List:", list_org)#prints Original List: ['banana', 'cherry', 'apple ']
print("Copied List:", list_copy)#prints Copied List: ['banana', 'cherry', 'apple ', 'lemon']

numbers = [1, 2, 3, 4, 5]
squared = [x**2 for x in numbers]#list comprehension to create a new list with squared values,each element in numbers is squared
print(squared)#prints [1, 4, 9, 16, 25]