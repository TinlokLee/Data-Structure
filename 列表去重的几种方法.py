l1 = ['a','g','a','b','t','f']
ls = {}.fromkeys(l1).keys()
print(ls)

''' 字典去重并保持顺序输出 '''
l1 = ['aa','g','a','b','t','f','a']
l2 = list(set(l1))
l2.sort(key=l1.index)

print(l2)
print('----------------------------------------')
    
a = [1,3,2,4,4,3,5,6,7]
#print(list(set(a)))
#print({}.fromkeys(a).keys())
aa = list(set(a))
aa.sort(key=a.index)   # 保持原顺序输出
print(aa) 

print('****************************************')

a = [1,3,9,2,4,4,3,53,5,6,7]
aa = list(set(a))
#aa.sort(key=a.index)  # 保持原顺序输出
#aa.sort()             # 默认升序输出
aa.sort(reverse=True)  # 降序输出
print(aa)