a = [1,2,3,4,5]*2
print(a)
from copy  import copy
a = [1,2,3,4,5]
for i in copy(a):
    a.append(i)
print(a)
'''删除'''
for i in a:
    a.remove(i)
print(a)
for i in a:
    a.remove(i)
print(a)
print('------------------------------')
l = [[1] * 3]*3
print(l)