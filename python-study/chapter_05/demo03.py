num = int(input('Enter a number: '))
if num > 0 :
    print('the number isd positive ')
elif num < 0 :
    print('the number is negative')
else:
    print('the number is zero')
# while
name = ''
while not name or name.isspace():
    name = input('please enter your name :')
    print('Hello,{}'.format(name))
# for
words = ['this','is','an','ex','parrot']
for word in words:
    print(word)
# 范围内置函数,得到的是一个迭代器对象
print(range(0,10))
for i in range(0,10):
    print(i)
# 遍历字典
d = {'x': 1, 'y': 2, 'z': 3}
for key in d:
    print(key, 'corresponds to', d[key])
for key,value in d.items():
    print(key,value)
# 并行迭代
names = ['a','b','c','d','e']
ages = [1,2,3,4,5]
for i in range(len(names)):
    print(names[i] , 'is ' , ages[i] , 'years old')
print(list(zip(names,ages) ))