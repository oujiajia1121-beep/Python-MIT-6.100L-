# print([[e,e**2] for e in range(6) if e%2==0])

######课上代码
# def make_prod(a):
#     def g(b):
#         return a*b
#     return g
# # val=make_prod(2) (3)
# # print(val)
# doubler=make_prod(3)
# val=doubler(3)
# print(val)



#########part.1
#my_list=[]
# for i in range(51):
#     if i%2==0:
#         b=i**2
#         #my_list.append(b)
#         print(b)
#创建列表还是直接打印都是可以的


##########part.2
# mylist=['name',1,2,'family',3,'lover',0,'address',9,'work']
# count=0
# for i in mylist:
#     if type(i)==str and len(i) > 5:#也可以用isinstance(i,str),来替代type(i)==str  而且isinstance(i,str)更好用
#         count+=1
# print(count)



##########part.3
# a=[1,2,3,4,5]
# result=list(map(lambda x: x+10,a))
# print(result)
#lambda x: x + 10,a  是一个匿名函数,意思是把a中的元素+10。map()可以迭代列表中的每一个元素。list()把map返回的迭代器转换成列表



##########part.4
a=[1,2,3,4,5,6,7,8,9]
def is_prime(n):
    if n<2:
        return False
    for i in range(2,int(n*0.5)+1):
        if n%i==0:
            return False
    return True
primes=list(filter(lambda x: is_prime(x),a))
print(primes)

#也可以这样写
a=[1,2,3,4,5,6,7,8,9]
primes=list(filter(lambda x:x>=2 and all(x%i!=0 for i in range(2,int(x*0.5)+1)),a))
print(primes)