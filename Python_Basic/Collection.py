#collections: counter, namedtuple, OrderedDict, defaultdict, deque
from collections import Counter, namedtuple, OrderedDict, defaultdict, deque
# Counter
a = "aaaaabbbbcccdde"
my_counter = Counter(a)
print(my_counter)#Counter({'a': 5, 'b': 4, 'c': 3, 'd': 2, 'e': 1})
print(my_counter.items())#dict_items([('a', 5), ('b', 4), ('c', 3), ('d', 2), ('e', 1)])
print(my_counter.keys())#dict_keys(['a', 'b', 'c', 'd', 'e'])
print(my_counter.values())#dict_values([5, 4, 3, 2, 1])
print(my_counter.most_common(2))#[('a', 5), ('b', 4)]
print(my_counter.most_common(1)[0])#('a', 5) returns a tuple
print(my_counter.most_common(1)[0][0])#'a' returns the element

# namedtuple
Point = namedtuple('Point', 'x,y')
pt = Point(1, -4)
print(pt)#Point(x=1, y=-4)
print(pt.x, pt.y)#1 -4

# OrderedDict
ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
print(ordered_dict)#OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4)])

# defaultdict
d = defaultdict(int)#default type is int
d['a'] = 1
d['b'] = 2
print(d['a'])#1
print(d['c'])#0, default value for int is 0

# deque
d = deque()

d.append(1)
d.append(2)

d.appendleft(3)
print(d) #deque([3, 1, 2])

d.pop()
print(d) #deque([3, 1])

d.extend([4, 5, 6])
print(d) #deque([3, 1, 4, 5, 6])
d.extendleft([7, 8, 9])
print(d) #deque([9, 8, 7, 3, 1, 4, 5, 6])
d.rotate(2)
print(d) #deque([5, 6, 9, 8, 7, 3, 1, 4])
d.rotate(-3)
print(d) #deque([8, 7, 3, 1, 4, 5, 6, 9])