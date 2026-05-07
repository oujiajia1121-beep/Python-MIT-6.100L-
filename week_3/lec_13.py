########part_1
# try:
#     x=int(input("Enter a number:"))
#     print(f"That is my favorite number:{x}")
# except ValueError:
#     print("It is not a number!!!")


#########part_2
# def safe_divide(a,b):
#     try:
#         return a/b
#     except ZeroDivisionError:
#         return None

#########part_3
def calc_age(x):
    if x<=0:
        raise ValueError#主动抛出ValueError异常
    print(f'请输入合法的年龄{x}')
    return x
# calc_age(-5)
calc_age(18)
