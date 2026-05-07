#课上的代码
# import copy#要区分深层和浅层必须要引入才能使用，开始错了好几次
# old_list=[[1,2],[3,4],[5,6]]
# # new_list=copy.copy(old_list)#浅层复制，运行就能理解，只能复制浅层的，深层的还是会新旧一起变动
# #new_list=old_list[:]#也是浅层复制
# new_list=copy.deepcopy(old_list)#深层复制，完全复制出了一个新的列表
# old_list.append([7,8])
# old_list[1][1]=9
# print("New list:",new_list)
# print("Old list:",old_list)



# #########part.1
# a=[1,2,[4,5]]
# b=a
# b[2][0]=99
# print(a,b)


#########part.2
# import copy
# a=[[1,9],[2,8],[3,7],[4,6]]
# b=copy.deepcopy(a)
# b[2][0]=5
# b[1].insert(1,0)
# print(b)
# print(a)



########part.3
# import copy
# def remove_diplicates(lst,e):
#     new_lst=copy.deepcopy(lst)
#     for i in lst:
#         if i==e:
#             new_lst.remove(e)
#     return new_lst
# val=remove_diplicates([1,2,3,4,4,4,4,],4)
# print(val)


#########part.4
def reverse_in_place(lst):
    left=0
    right=len(lst)-1
    while left<right:
        lst[left],lst[right]=lst[right],lst[left]
        left += 1
        right -= 1
    
a=[2,3,1,5,7,8]
reverse_in_place(a)
print(a)