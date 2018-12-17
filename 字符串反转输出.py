a = 'abcdefg'

def foo(msg):
    arr = list(msg)
    s = ''.join(arr[::-1])
    return s

aa = foo(a)
print(aa)

print('********************************')

aa = list(a)
aaa = ''.join(aa[::-1])
print(aaa)