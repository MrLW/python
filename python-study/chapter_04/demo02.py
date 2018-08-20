# 复制：浅复制
from copy import deepcopy
# fromkeys:创建一个新字典,
print({}.fromkeys(['name','age']))
print(dict.fromkeys(['name','age'],'Unknow')) # 指定默认值

# items
d = {'title': 'Python Web Site', 'url': 'http://www.python.org', 'spam': 0}
print(d.items())
# 将字典项放入list中
print(list(d.items()))