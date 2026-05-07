#########part.1
# a=[1,2,3]
# a.append(4)
# a.insert(0,0)
# a.remove(2)
# print(a)


#########part.2
# def add_to_list(lst,item):
#     lst.append(item)
#     lst.insert(0,0)
#     lst.remove(2)
#     return lst
# a=[1,2,3,4,5]
# x=add_to_list(a,6)
# print(x)

#########part.3
# def create_new_list(lst,item):
#     new_list=lst[:]
#     new_list.append(item)
#     return lst,new_list
# (a,b)=create_new_list([1,2,3,4,5,6],7)
# print(a)
# print(b)



#########part.4
a=[1,2,3,2,7,1,9]
# b=a[:]
b=a.copy()
b.sort()
print(a)
print(b)