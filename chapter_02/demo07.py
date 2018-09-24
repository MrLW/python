print(list('Hello'))
# 修改列表
x = [1,2,3]
x[1] = 4
print(x)
# 删除列表
names = ['Alice', 'Beth', 'Cecil', 'Dee-Dee', 'Earl']
del names[2]
print(names)
# 切片列表,切片赋值.注意:这里是替换.
perl = list('Perl')
perl[2:] = list('ar')
print(perl)
