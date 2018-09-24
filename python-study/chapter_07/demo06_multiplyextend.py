# 多继承
class Calculator:
    def calculate(self, expression):
        self.value = eval(expression)
class Talker:
    def talk(self):
        print('Hi, my value is', self.value)

class TalkingCalculator(Calculator,Talker):
    pass
tc = TalkingCalculator()
tc.calculate('1 + 2 * 3')
tc.talk() #Hi, my value is 7
print(callable(getattr(tc,'talk',None)))
print(tc.__doc__)