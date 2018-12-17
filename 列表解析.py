a0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
a1 = range(10)
a2 = [i for i in a1 if i in a0]
a3 = [a0[s] for s in a0]
a4 = [i for i in a1 if i in a3]
a5 = {i:i*i for i in a1}
a6 = [[i, i*i] for i in a1]
print(a0) #{'a':1,'b':2,'c':3,'d':4,'d':5}
print(a1) # 0,1,2,3,4,5,6,7,8,9
print(a2) # []
print(a3) # [1,2,3,4,5]
print(a4) # [1,2,3,4,5]
print(a5) # {0:0,1:1,2:4,3:9,4:16,5:25...}
print(a6) # [[0,0],[1,1],[2,4]...]
''' 列表解析十分节约时间 '''

def f(x, l=[]):
    for i in range(x):
        l.append(i*i)
    print(l)
a = f(2)
print(a)  # [0,1]
b = f(3,[1,2,3])
print(b) # [1,2,3,0,1,4]
c = f(3)
print(c) # [0,1,0,1,4]
# 使用之前内存地址中存储的旧列表，所有前两位是 0,1

l1 = ['a','a','b','f']
ls = {}.fromkeys(l1).keys()
print(ls)