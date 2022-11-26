"""
# Que.1 program to Find the size of a Tuple
# Using getsizeof()
t = ('red', 'yellow', 'green', 'pink', 'blue', 'black')
import sys
print('size of tuple', sys.getsizeof(t), 'bytes')

or
# Using __sizeof__() method
t = ('red', 'yellow', 'green', 'pink', 'blue', 'black')
print('size of tuple', t.__sizeof__(), 'bytes')
=========================================================

# Que.2 Maximum and Minimum K elements in Tuple
# Using sorted() + loop
t = (5, 20, 3, 7, 6, 8)
print('The original tuple is:', t)
K = 2
ls = []
t = list(sorted(t))
for i, val in enumerate(t):
    if i < K or i >= len(t) - K:
        ls.append(val)
print('extracted value is:', tuple(ls))

or
# Using slicing + sorted()
t = (5, 20, 3, 7, 6, 8)
print('The original tuple is:', t)
K = 2
t = list(sorted(t))
res = tuple(t[:K] + t[-K:])
print('extracted value is:', tuple(ls))
================================================================

# Que.3 Create a list of tuples from given list having number
and its cube in each tuple
# Using pow() function
l1 = [1, 2, 5, 6]
res = [(num, pow(num, 3)) for num in l1]
print('cute in each tuple:', res)

or
# Using ** operator
l1 = [1, 2, 5, 6]
res = [(num, (num ** 3)) for num in l1]
print('cute in each tuple:', res)
======================================================================

# Que.4 Adding Tuple to List and vice – versa
# Using += operator
ls = [1, 2, 3, 4]
t = (5, 6, 7)
ls += t
print('adding tuple to list is:', ls)

or
# Using tuple(), data type conversion
t = (5, 6, 7)
ls = [1, 2, 3, 4]
res = tuple(list(t) + ls)
print('adding tuple to list is:', res)
==========================================================

# Que.5 Sum of tuple elements
# Using list() + sum()
t = (7, 8, 9, 1, 10, 7)
print('The original tuple is:', t)
print('sum is:', sum(list(t)))

or
t = (7, 8, 9, 1, 10, 7)
res = 0
for i in t:
    res += i
print('sum is:', res)
==============================================================

# Que.6 Modulo of tuple elements
# using zip()
t1 = (10, 4, 5, 6)
t2 = (5, 6, 7, 5)
res = tuple(x % y for x, y in zip(t1, t2))
print('Tuple modulo is:', res)

or
# using map() + mod
from operator import mod
t1 = (10, 4, 5, 6)
t2 = (5, 6, 7, 5)
res = tuple(map(mod, t1, t2))
print('Tuple modulo is:', res)
=====================================================

# Que.7 All pair combinations of 2 tuples
# Using list comprehension
t1 = (4, 5)
t2 = (7, 8)
print('The original tuple 1:', t1)
print('The original tuple 2:', t2)
res = [(a, b) for a in t1 for b in t2]
res = res + [(a, b) for a in t2 for b in t1]
print('The filtered tuple:', res)
=======================================================================

# Que.8 Update each element in tuple list
# Using list comprehension
tl = [(1, 3, 4), (2, 4, 6), (3, 8, 1)]
print('The original list:', tl)
add_ele = 4
res = [tuple(j + add_ele for j in sub) for sub in tl]
print('List after bulk update:', res)

or
# Using list comprehension + map() + lambda
tl = [(1, 3, 4), (2, 4, 6), (3, 8, 1)]
print('The original list:', tl)
add_ele = 5
res = [tuple(map(lambda ele: ele + add_ele, sub)) for sub in tl]
print('List after bulk update:', res)
=========================================================================

# Que.9 Multiply Adjacent elements
# using zip() + tuple
t = (1, 5, 7, 8, 10)
print('The original tuple:', t)
res = tuple(i * j for i, j in zip(t, t[1:]))
print('Resultant tuple after multiplication:', res)

or
# using map() + lambda + tuple
t = (1, 5, 7, 9, 10)
print('The original tuple:', t)
res = tuple(map(lambda i, j: i * j, t[1:], t[:-1]))
print('Resultant tuple after multiplication:', res)
===================================================================

# Que.10 Join Tuples if similar initial element
# Using loop
t = [(5, 6), (5, 7), (6, 8), (6, 10), (7, 13)]
print('The original list is:', t)
res = []
for i in t:
    if res and res[-1][0] == i[0]:
        res[-1].extend(i[1:])
    else:
        res.append([ele for ele in i])
res = list(map(tuple, res))
print('The extracted elements:', res)
=================================================================

# Que.11 Remove Tuples of Length K
# Using list comprehension
t = [(4, 5), (4,), (8, 6, 7), (1,), (3, 4, 6, 7)]
print('The original list:', t)
K = 1
res = [ele for ele in t if len(ele) != K]
print('Filtered list:', res)

or
# Using filter() + lambda + len()
t = [(4, 5), (4,), (8, 6, 7), (1,), (3, 4, 6, 7)]
print('The original list:', t)
K = 1
res = list(filter(lambda x: len(x) != K, t))
print('Filtered list:', res)
================================================================

# Que.12 Remove Tuples from the List having every element as None
# Using all() + list comprehension
lt = [(None, 2), (None, None), (3, 4), (12, 3), (None,)]
print('The original list is:', lt)
res = [sub for sub in lt if not all(ele == None for ele in sub)]
print('Removed None Tuples:', res)

or
# Using all() +  filter() + lambda
lt = [(None, 2), (None, None), (3, 4), (12, 3), (None,)]
print('The original list is:', lt)
res = list(filter(lambda sub: not all(ele == None for ele in sub), lt))
print('Removed None Tuples:', res)

or
# Using count()
lt = [(None, 2), (None, None), (3, 4), (12, 3), (None,)]
print('The original list is:', lt)
res = []
for i in lt:
    if not(i.count(None) == len(i)):
        res.append(i)
print('Removed None Tuples:', res)
====================================================================

# Que.13 Sort a list of tuples by second Item
# Using Bubble Sort
t = [('for', 24), ('is', 10), ('best', 28),
       ('better', 5), ('portal', 20), ('a', 15)]
lst = len(t)
for i in range(0, lst):
    for j in range(0, lst - i - 1):
        if t[j][1] > t[j + 1][1]:
            temp = t[j]
            t[j] = t[j + 1]
            t[j + 1] = temp
print('sort a list of tuples by second Item:', t)

or
# Using sorted()
tup = [('rishabh', 10), ('akash', 5), ('ram', 20), ('gauri', 15)]
res = sorted(tup, key=lambda x: x[1])
print('sort a list of tuples by second Item:', res)
==================================================================

# Que.14 Sort Tuples by Total digits
# Using sorted() + len() + sum() + lambda
tl = [(3, 4, 6, 723), (1, 2), (12345,), (134, 234, 34)]
print('The original list is:', tl)
res = sorted(tl, key=lambda tup: sum([len(str(ele)) for ele in tup ]))
print('Sorted tuples:', res)
================================================================

# Que.15 Elements frequency in Tuple
# Using defaultdict()
from collections import defaultdict
t = (4, 5, 4, 5, 6, 6, 5, 5, 4)
print('The original tuple is:', t)
res = defaultdict(int)
for ele in t:
    res[ele] += 1
print('Tuple elements frequency is:', dict(res))

or
# Using counter()
from collections import Counter
t = (4, 5, 4, 5, 6, 6, 5, 5, 4)
print('The original tuple is:', t)
res = Counter(t)
print('Tuple elements frequency is:', dict(res))

or
# Using count()
t = (4, 5, 4, 5, 6, 6, 5, 5, 4)
print('The original tuple is:', t)
res = dict()
x = list(t)
y = []
for i in x:
    if i not in y:
        y.append(i)
for i in y:
    res[i] = x.count(i)
    print('Tuple elements frequency is:',  res)
===================================================================

# Que.16 Filter Range Length Tuples
# Using list comprehension + len()
tt = [(4,), (5, 6), (2, 3, 5), (5, 6, 8, 2), (5, 9)]
print('The original list is:', tt)
i, j = 2, 3
res = [sub for sub in tt if (len(sub)) >= i and len(sub) <= j]
print('The tuple list after filtering range records:', res)

or
# Using filter() + lambda + len()
tt = [(4,), (5, 6), (2, 3, 5), (5, 6, 8, 2), (5, 9)]
print('The original list is:', tt)
i, j = 2, 3
res = list(filter(lambda ele: (len(ele)) >= i and len(ele) <= j, tt))
print('The tuple list after filtering range records:', res)
==============================================================

# Que.17 Assign Frequency to Tuples
# Using Counter() + items() + * operator + list comprehension
from collections import Counter
st = [(6, 5, 8), (2, 7), (6, 5, 8), (6, 5, 8), (9,), (2, 7)]
print('The original list is:', st)
res = [(*key, val) for key, val in Counter(st).items()]
print('Frequency Tuple list:', res)

or
# Using Counter() + most_common() + * operator + list comprehension
from collections import Counter
st = [(6, 5, 8), (2, 7), (6, 5, 8), (6, 5, 8), (9,), (2, 7)]
print('The original list is:', st)
res = [(*key, val) for key, val in Counter(st).most_common()]
print('Frequency Tuple list:', res)

or
# Using count(),list(),tuple()
st = [(6, 5, 8), (2, 7), (6, 5, 8), (6, 5, 8), (9,), (2, 7)]
print('The original list is:', st)
res = []
for i in st:
    if i not in res:
        res.append(i)
res1 = []
for i in res:
    x = list(i)
    x.append(st.count(i))
    p = tuple(x)
    res1.append(p)
print('Frequency Tuple list:', res1)
=================================================================

# Que.18 Records with Value at K index
# Using loop
tl = [(3, 1, 5), (1, 3, 6), (2, 5, 7), (5, 2, 8), (6, 3, 0)]
print('The original list is:', tl)
ele = 3
K = 1
res = []
for x, y, z in tl:
    if y == ele:
        res.append((x, y, z))
print('The tuples of element at Kth position:', res)

or
# Using enumerate() + list comprehension
tl = [(3, 1, 5), (1, 3, 6), (2, 5, 7), (5, 2, 8), (6, 3, 0)]
print('The original list is:', tl)
ele = 3
K = 1
res = [b for a, b in enumerate(tl) if b[K] == ele]
print('The tuples of element at Kth position:', res)
=======================================================================

# Que.19 Test if tuple is distinct
# Using loop
t = (1, 4, 5, 6, 1, 4)
print('The original tuple is:', t)
res = True
temp = set()
for ele in t:
    if ele in temp:
        res = False
        break
    temp.add(ele)
print('Is tuple distinct ?:', res)

or
# Using set() + len()
t = (1, 4, 5, 6, 1, 4)
print('The original tuple is:', t)
res = len(set(t)) == len(t)
print('Is tuple distinct ?:', res)
=====================================================================

# Que.20 Row-wise element Addition in Tuple Matrix
# Using enumerate() + list comprehension
ls = [[('Shiv', 3), ('is', 3)], [('best', 1)], [('for', 5), ('study', 1)]]
print('The original list is:', ls)
ele = [6, 7, 8]
res = [[sub + (ele[idx],) for sub in val] for idx, val in enumerate(ls)]
print('The matrix after row elements addition:', res)

or
# Using enumerate() + list comprehension
ls = [[('Shiv', 3), ('is', 3)], [('best', 1)], [('for', 5), ('study', 1)]]
print('The original list is:', ls)
ele = [6, 7, 8]
res = [[(idx, val) for idx in key] for key,  val in zip(ls, ele)]
print('The matrix after row elements addition:', res)
===================================================================
"""
