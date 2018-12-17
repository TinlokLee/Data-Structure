
import re

num_re = re.compile(r'[0-9]')
zimu_re = re.compile(r'[a-zA-Z]')

def count_num(str_num):
    num_list = num_re.findall(str_num)
    zimu_list = zimu_re.findall(str_num)
    print('数字个数: %d,中英文个数: %d'%(len(num_list),len(zimu_list)))

str = 'aadadada,887,44,nihaoa,你呢,yet'
print(count_num(str))
print('------------------------------------')
''' 正则匹配邮箱 '''
str0 = '1224242@qq.com,jjj@sss.com, 68878@yu.net,13344445@163.com'
str1 = re.match(r'^[a-zA-Z0-9.-]+@[a-zA-Z0-9]+[com,cn,net]{1,3}$',str0)
str2 = re.match(r'^[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*\.[a-zA-Z0-9]{2,6}$',str0)
print(str1)
print(str2)