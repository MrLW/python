# 这个前面已经学习过,列表推导
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [x ** 2 for x in a if x % 2 == 0]
print(b)
# 生成器推导
g = ((i + 2) ** 2 for i in range(2, 27))
next(g) # 16


it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        x = next(it)
        print(x)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break


# 对迭代器进行递归调用,解决多层嵌套列表
nes = [[[1,2,3],4,5],6,7]
def flatter(nes):
    try:
        for bs in nes :
            for b in flatter(bs):
                yield b;
    except TypeError:
        yield nes
for i in flatter(nes):
    print('i:',i)

# 生成器的方法
def repeater(value):
    while True:
        new = (yield value)
        if new == 'e':
            break
        if new is not None: value = new

r = repeater(42)
r.send(None);
r.send('helllo,world')
r.send('e')
