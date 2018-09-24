class MyException(Exception) : pass

# 异常捕获
class MuffledCallculator :
    muffed = False
    def call(self,expr):
        try:
            return eval(expr)
        except ZeroDivisionError:
            if self.muffed:
                print('Division by zero is illegal')
            else:
                raise


calculator = MuffledCallculator()
print(calculator.call('10/5'))
print(calculator.call('10/0'))
