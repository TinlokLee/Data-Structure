class A(object):
    state = {}
    def __new__(cls):
        #ob = super(A,cls).__new__(cls)
        ob = super().__new__(cls)
        ob.__dict__ = cls.state
        #print(ob)
        return ob

class Myfoo(A):
    a = 1
m = Myfoo()
print(m)

class My_Singleton(object):
    def foo(self):
        pass
m = My_Singleton()
print(m)

print('--------------------------------------------------')
class B(object):
    sta = {}
    def foo(cls):
        aa = super().__new__(cls)
        aa.__dict__ = cls.sta
        print(aa)
        return aa
class M(B):
    pass
ss = M()
print(ss)