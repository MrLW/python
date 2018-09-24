# // 使用dict方法将元组转换字典
items = [('name', 'Gumby'), ('age', 42)]
d = dict(items)
print(d)
x = [] ;
# x[42] = 'li'i ; 没有43好元素
x = {} ;
x[42] = 1 ;
# format_map()方法
phonebook = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'} ;
print("Cecil's phone number is {Cecil}.".format_map(phonebook)) ;
# 字典的清空 clear()
x = {} ;
y = x ;
x['key'] = 'value' ;
print(y)
x = {};
print(y) ;
