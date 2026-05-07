# def apply_to_list(lst,func):
#     result=[]
#     for s in lst:
#         if s%2==0:
#             result.append(func(s))
#         else:
#             result.append(func(s))
#     return result
# def is_even(x):
#     return x%2==0
# a=[2,3,4,5,6,7,8,9,5]
# print(apply_to_list(a,is_even))

###################part.2
# def make_multipiler(n):
#     return lambda x:n*x
# a=make_multipiler(4)
# print(a)


##############part.3
# def compose(f,g):
#     return lambda x: f(g(x))
# b=make_multipiler(4)
# a=compose(is_even,b)
# print(a(9))#因为有个匿名返回值x,所以必须在这里再加上一个数字


############part.4
def filter_list(lst,predicate):
    result=[]
    count=0
    for s in lst:
        if predicate(s):
            result.append(s)
            count += 1
    return result,count
def is_prime(x):
    if x<2:
        return False
    if x==2:
        return True
    if x%2==0:
        return False
    for i in range(3,int(x*0.5)+1,2):
        if x%i==0:
            return False
    return True
lst=list(range(1,101))
print(filter_list(lst,is_prime))
        
