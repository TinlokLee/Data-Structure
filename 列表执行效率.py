__auth__ = 'Lee'

def foo(n):
    a1 = sorted(n)
    a2 = [i for i in a1 if i < 0.5]
    return [i*i for i in a2]
import cProfile
import random
n = [random.random() for i in range(100000)]
cProfile.run('foo(n)')   



