def is_sorted(L):
    """检查是否是从大到小的顺序
    """
    i=0
    j=len(L)
    while i+1<j:
        if L[i]>L[i+1]:
            return False
        i+=1
    return True

import random
import time
##随机排序
def bogo_sort(L):
    count=0
    while not is_sorted(L):
        random.shuffle(L)#随机打乱一个列表的元素顺序，而且是原地修复
        count += 1
    return count
L=[2,1,9,4,8,6,7]
t0=time.time()#记录开始时间
count=bogo_sort(L)
t1=time.time()
total_time=t1-t0
print(f"总共循环了{count}，排序后的列表为{L}，总用时{total_time}")


def bubble_sort(L,detail=False):
    """
    冒泡排序法:相邻两两比较，大的往后冒，每一轮把最大值沉到最后
    """
    did_swap=True
    while did_swap:
        did_swap=False
        for j in range(1,len(L)):
            if L[j-1]>L[j]:
                did_swap=True
                L[j],L[j-1]=L[j-1],L[j]
    if detail==True:
        print(L)
    return L

def selection_sort(L):
    """
    每一轮找最小值，放在最前面
    """
    for i in range(len(L)):
        for j in range (i,len(L)):
            if L[j]<L[i]:
                L[i],L[j]=L[j],L[i]
    return L

def merge(left,right):#这是合并的代码
    """
    把数组不断从中间切成两半，一直切到只剩单个元素，再把切分的两部分，两两合并成有序数组
    """
    result=[]
    i,j=0,0
    while i in len(left) and j in len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    while(i<len(left)):
        result.append(left[i])
        i+=1
    while(j<len(right)):
        result.append(right[j])
        j+=1
    return result

def merge_sort(L):#切割的代码
    if len(L)<2:
        return L[:]
    else:
        middle=len(L)//2
        left=merge_sort(L[:middle])
        right=merge_sort(L[middle:])
        return merge(left,right)