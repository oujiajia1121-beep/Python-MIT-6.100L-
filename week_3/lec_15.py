#####递归
 ########例子
# def power_recur(n,p):
#     if p==0:
#         return 1
#     elif p==1:
#         return n
#     else:
#         return n*(power_recur(n,p-1))

# print(power_recur(3,4))


##########part_1 用递归实现竭诚函数
# def factorial_rec(n):
#     if n==1:
#         return 1
#     else:
#         return n*factorial_rec(n-1)

# print(factorial_rec(4))


##########part_2 用递归实现斐波那契数列函数
# def fib_rec(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fib_rec(n-1)+fib_rec(n-2)
    
# print(fib_rec(6))



########part_3 对比循环和递归的性能差异
# import timeit#引入用来测试用时的
# def fib_loop(n):
#     a,b=0,1
#     for n in range(2,n+1):
#         a,b=b,a+b
#     return b
# t_rec=timeit.timeit(lambda:fib_rec(20),number=100)#测试递归
# t_loop=timeit.timeit(lambda:fib_loop(20),number=100)#测试循环

# print(f"测试循环算斐波那契函数循环100次用时{t_loop:.2f}秒")
# print(f"测试递归算斐波那契函数循环100次用时{t_rec:.2f}秒")


#######part_4 用递归实现：计算列表中所有元素的和
def total_rec(my_list):
    if len(my_list)==0:
        #另一种写法 if not my_list: 也表示为空集的时候
        return 0
    else:
        #return my_list[-1]+total_rec(my_list[:-1])#最后一个子集加剩余子集的和
        return my_list[0]+total_rec(my_list[1:])

my_list=[1,2,3,4,5,6,7,8]
print(total_rec(my_list))


######part_5 用递归实现：反转字符串
# def reverse_rec(s):
#     if len(s)<=1:
#         return s
#     #return s[-1]+reverse_rec(s[:-1])
#     #另一种写法
#     return reverse_rec(s[1:])+s[0]


# s="hello world"
# print(reverse_rec(s))