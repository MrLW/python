# try:
#     1/0
# except ZeroDivisionError:
#     raise ValueError from None
# except TypeError:
#     raise
#
# try:
#     1/0
# except (ZeroDivisionError,TypeError):
#     raise ValueError from None

print('----------')
try:
    1/0
except (ZeroDivisionError,TypeError) as e :
    print(e)