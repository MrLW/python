# 抽象基类
from abc import ABC,abstractmethod
class Talker(ABC):
    # 使用@abstractmethod装饰talk,表明是一个抽象方法
    @abstractmethod
    def talk(selfs):
        pass

# 派生子类
class Knigget(Talker):
    def talk(selfs):
        print('Hi')
class Herring :
    pass ;


