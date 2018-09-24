class Foobar:
    def __init__(self,value = 42):
        self.somevar = value

    def __del__(self):
        print('对象被销毁时调用')

f = Foobar("this is my param")
print(f.somevar)