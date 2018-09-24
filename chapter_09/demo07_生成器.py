# 生成器,核心:yield关键字
def flatter(nes):
    for bs in nes :
        for b in bs:
            yield b;

nes = [[1,2,3],[4,5],[7,8]]
for x in flatter(nes):
    print('x:',x)

# 对生成器转换为list
l = list(flatter(nes))
print(l) ;

