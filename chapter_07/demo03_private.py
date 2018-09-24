class Secretive:
    # 在方法前面加两个下划线,则外部不可访问
    def __inaccessible(self):
        print('Bet you can not see me...')
    def accessible(self):
        print('the secret message is :')
        self.__inaccessible()
s = Secretive()
s.accessible()
Secretive._Secretive.__inaccessible