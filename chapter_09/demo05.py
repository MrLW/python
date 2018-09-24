class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0
    def __setattr__(self, key, value):
        if key == 'size':
            self.width ,self.height = value
        else:
            self.__dict__[key] = value
    def __getattr__(self, key):
        if key == 'size':
            return self.width,self.height
        else:
            raise AttributeError()

