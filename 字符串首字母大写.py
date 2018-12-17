'''
    自定义函数实现字符串首字母大写
    
    1  使用装饰器
    2  upper()方法
'''

def deco(func):
    def wrapper(*args, **kwargs):
        msg = func(*args, **kwargs)
        ret = msg[0].upper() + msg[1:]
        print(ret)
        # print('Hello')
        return ret
    return wrapper

@deco
def getTxt(word='hello python'):
    # print('你好')
    return word
    # return word.lower()  不用lower（）方法输出结果一样

# 装饰器的调用方法
getTxt()
getTxt(word='idadada') # 可传参数，修改默认值



