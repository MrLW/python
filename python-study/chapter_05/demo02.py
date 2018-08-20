name = input('what is your name ?')
if name.endswith('Bob'):
    print("Hello Mr.Bob")
else:
    print("Hello LiWen")
# python的三目运算符
status = 'friend' if name.endswith("Bob") else "liwen"
print(status)

