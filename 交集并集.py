a = set([1,2,3])
b = set([2,3,4])
print(a & b)
print(a | b)
''' 交集和并集，返回值是字典类型 '''
def foo(n, lt=[]):
    for i in range(n):
        lt.append(i*i)
    print(lt)

print(foo(2))
print(foo(3,[3,2,1]))
print(foo(3))