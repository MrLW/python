# for break else 语句:在for循环中,如果没有执行break,则执行else

from math import sqrt
for n in range(99,81,-1) :
    root = sqrt(n)
    if root == int(root):
        print(n)
        break ;
else:
    print('do not find it')