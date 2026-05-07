#######例子，用字典递归的方式计算斐波那契函数
# def fib_efficient(n,d):
#     if n in d:
#         return d[n]
#     else:
#         ans=fib_efficient(n-1,d)+fib_efficient(n-2,d)
#         d[n]=ans
#         return ans

# d={1:1,2:1}
# print(fib_efficient(6,d))


########示例———2
# def score_count(x):
#     """通过+1，+2，+3得到的能够达到x分的所有组合，顺序无关紧要
#     """
#     if x==1:
#         return 1
#     elif x==2:
#         return 2
#     elif x==3:
#         return 3
#     else:
#         return score_count(x-1)+score_count(x-2)+score_count(x-3)

# if __name__=="__main__":
#     print(score_count(6))

# def score_efficient(x,d): #用字典递归得分
#     if x in d:
#         return d[x]
#     else:
#         ans=score_efficient(x-1,d)+score_efficient(x-2,d)+score_efficient(x-3,d)
#         d[x]=ans #是把重复的元素都储存在字典中
#         return ans
    
# if __name__=="__main__":
#     d={1:1,2:2,3:3}
#     print(score_efficient(3 ,d))


###########示例————3
# def my_rev(lst):
#     if not lst:
#         return lst
#     return my_rev(lst[1:])+[lst[0]]#[lst[0]]在外面加上方括号是为了使返回值是一个列表，如果没有的话，列表是不能加上整数的
# #函数内的返回值必须是同一种类型
# my_list=[1,['d'],['e',['f','g']]]#只能反转顶层列表中的元素，不能返转深层列表
# print(my_rev(my_list))#[['e',['f','g']],['d'],1]


# def deep_rev(lst):
#     if len(lst)==1:
#         if type(lst[0])!=list:
#             return lst
#         else:
#             return [deep_rev(lst[0])]
#     else:
#         if type(lst[0])!=list:
#             return deep_rev(lst[1:])+[lst[0]]
#         else:
#             return deep_rev(lst[1:])+[deep_rev(lst[0])]
#    #在返转lst[0]时都要在外面加上方括号，不然就会改变元素组成     
# f_list=[1,[2,3],[4,5,6],[7,8,9]]
# s_list=[[1,2],[3,4],5,[6,7,8],9]
# print(deep_rev(f_list))
# print(deep_rev(s_list))


###########part_1 判断一个字符串是否为回文
# def palindrome_rec(w):
#     try:
#         type(w)==str
#         if len(w)==1:
#             return w
#         else:
#             return w[-1]+palindrome_rec(w[:-1])
        
#     except TypeError:
#         print(f"{w}这不是字符串")

# def is_palindrome(w):
#     if w==palindrome_rec(w):
#         print(f"{w}是回文")
#         return True
#     return False

# word="上海自来水来自海上"
# word_2=1234321
# print(is_palindrome(word))
# print(is_palindrome(word_2))


#########part_2 用递归实现：找出嵌套列表中的最大值
# def flatten(lst):
#     if not lst:
#         return lst
#     else:
#         #如果第一个元素是列表，就递归展开：否则直接保留，再处理剩下的部分
#         if isinstance(lst[0],list):#isinstance(对象，类型/类型元组) 判断一个对象是不是某个数据类型的实例，它的返回值是布尔值
#             return flatten(lst[0])+flatten(lst[1:])
#         else:
#             return [lst[0]]+flatten(lst[1:])

# #求列表中最大值的办法，但其实可以不用直接 max() 就好了
# def max_list(lst):
#     my_list=flatten(lst)
#     if not lst:
#         return None
#     max_value=my_list[0]
#     for i in my_list:
#         if type(i)==int:
#             if i>max_value:
#                 max_value=i
#     return max_value
            

# if __name__=="__main__":
#     lst=[1,[2,3],[4,[5,6]]]
#     # print(max_list(lst))
#     #最简洁的办法
#     print(max(flatten(lst)))


############part_3 用递归实现汉诺塔：打印移动步骤
# def hanoi_rec(n,a,b,c):
#     if n==1:
#         print(f"盘子1：{a}👉{c}")
#     else:
#         #把上面n-1个先移到b,借c
#         hanoi_rec(n-1,a,c,b)
#         #移动底下的大盘
#         print(f"盘子{n}:{a}👉{c}")
#         #把n-1个从b移到c，借a
#         hanoi_rec(n-1,b,a,c)

# print(hanoi_rec(3,'A','B','C'))


#########part_4 用递归实现归并排序
#合并两个有序列表
def merge(left,right):
    res=[]
    i=j=0
    #两边逐个对比，小的先放进结果
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i+=1
        else:
            res.append(right[j])
            j+=1
        #补上剩下的元素
    res.extend(left[i:])
    res.extend(right[j:])
    return res

#并归排序主函数
def merge_sort(arr):
    #递归终止：长度<=1 不用排
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=merge_sort(arr[:mid])
    right=merge_sort(arr[mid:])
    #合并
    return merge(left,right)
#测试
nums=[8,3,5,4,7,6,1,2]
print(merge_sort(nums))


# 合并两个有序列表
def merge(left, right):
    res = []
    i = j = 0
    # 两边逐个对比，小的先放进结果
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    # 补上剩下的元素
    res.extend(left[i:])
    res.extend(right[j:])
    return res

# 归并排序主函数
def merge_sort(arr):
    # 递归终止：长度<=1 不用排
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    # 关键：对左右两半递归排序
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    # 合并两个有序的左右部分
    return merge(left, right)

# 测试
nums = [8, 3, 5, 4, 7, 6, 1, 2]
print(merge_sort(nums))