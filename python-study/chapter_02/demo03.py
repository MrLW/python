# 切片:访问单个元素
tag = '<a href="http://www.python.org">Python web site</a>'
print(tag[9:30])
# 访问数字列表都某三个元素
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[-3:])
# 复制整个序列
print(numbers[:])
# 指定步长
print(numbers[::2]) 