def hello_01(greeting,name):
    print('{},{}'.format(greeting,name))
hello_01(greeting='Hello',name='Bob')

# 收集参数,返回元组
def print_params(*params):
    print(params)
print_params('test')
# 收集关键字参数,使用2个*,返回的是字典
def print_params_3(**params):
    print(params)
print_params_3(x=1,y=2,z=3)