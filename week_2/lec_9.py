#######part.1
# max=lambda a,b:a if a>b else b
# print(max(5,9))


#######part.2
# my_list=[(1,'banana'),(2,'orange'),(3,'cherry')]
# l=sorted(my_list,key=lambda x: x[1])#按第二个元素升序排
# #l=sorted(my_list,key=lambda x:x[1],reverse=True)按第二个元素降序拍的
# print(l)



########part.3
# things=['name','address','fimaly']
# things.append('work')
# del things[1]#这个也是列表中删除某一项
# things.pop(2)#列表中删除某一项
# things.extend([['love','you']])
# print(things)


########part.4
mylist=[]
for i in range(21):
    x=i*i
    mylist.append(x)
print(mylist )