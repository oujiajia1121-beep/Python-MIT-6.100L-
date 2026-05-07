###########example
# def find_grades(grades,students):
#     Lnew=[]
#     for element in students:#element是字典里的key
#         grade=grades[element]
#         Lnew.append(grade)
#     return Lnew
# d={'a':'B','m':'C','J':'B','k':'A'}
# d['grace']='B'#在字典中添加元素的格式dict['key']=value
# d['a']='A'#更改字典中的元素也很简单，就是和添加一样的，所以这个没有就添加，有就更改
# del(d['m'])#删除字典中的某个元素
# print('J' in d)#检查某个key是否在字典中,只会返回True or False 。这个只能检查key，不能检查value
# print(d.keys()) #return dict_keys(["所有的key"])
# print(list(d.keys()))#return ['所有的key']  这个时候返回的是列表
# print(d.values()) #return dict_values(['所有value'])
# print(list(d.values())) #return ['所有value'] 这个时候返回的是列表
# print(d.items())#将key和value组合起来
# print(find_grades(d,['a','grace']))
##字典中的key必须是不可变的

# grades={'ana':{'mq':[5,4,4],'ps':[10,9,9],'find':'B'},
#         'bob':{'mq':[6,7,8],'ps':[8,9,10],'find':'A'}}
# print(grades['ana']['mq'][1])
# print(grades['bob']['ps'][2])



###########part_1#添加字典并且按字数排序
# article="You know you love me, I know you careJust shout whenever, and I'll be thereYou want my love, you want my heartAnd /" 
# " we will never, ever, ever be apartAre we an item? Girl, quit playing and looked right in my eyesMy first love broke my heart for the first timeAnd I was like baby, baby, /"
# "baby, ohLike baby, baby, baby, ohLike baby, baby, baby, oh"
# def word_frequence(words):#转换成字典
#     words_list=words.split()
#     word_dict={}
#     for w in words_list:
#         if w in word_dict:
#             word_dict[w] += 1
#         else:
#             word_dict[w]=1
#     return word_dict
# #直接按词频降序进行排序
# def find_words_tumple(word_dict):
#     sorted_items=sorted(word_dict.items(),key=lambda items:items[1],reverse=True)
#     return sorted_items


# #dict.setdefault(k,v)  是在字典中添加新元素和list 中的 list.append()是差不多的功能
# #dict.get(key,deflaut=None):安全取键，键不存在返回默认值
# #如print(dict.get("gender","未知"))#输出为：未知
# #dict.pop(key,default=None):删除指定键并返回对应值，键不存在返回默认值
# #dict.update(other_dict):批量添加、修改，可合并另一个字典
# if __name__=="__main__":
#     a=word_frequence(article)
#     last_dict=find_words_tumple(a)
#     # groups={}
#     # for k,v in last_dict.items():
#     #     if v not in groups:
#     #         groups[v]=[]
#     #         groups[v].append(k)

#     print(last_dict)
        



##########part_2#实现一个简易的英汉词典
# def translation_dict(d,word):
#     for k,v in d.items():
#         if word==k:
#             return d[word]
#     return "没有该单词"

# if __name__=="__main__":
#     d={'hello':"👋",'world':"世界",'sister':"姐姐"}
#     print(translation_dict(d,'world'))



#########part_3#合并两个字典，遇到重复的键时保留dict2的值
def merge_dict(dict_1,dict_2):
    dict_copy=dict_1.copy()
    dict_1_key=dict_copy.keys()
    dict_2_key=dict_2.keys()
    for k_1 in dict_1_key:
        for k_2 in dict_2_key:
            if k_1==k_2:
                del dict_1[k_1]
                dict_1.update(dict_2)
    return dict_1

a={'a':1,'b':2,'c':4,'p':9}
b={'b':8,'o':2,'y':7}
print(merge_dict(a,b))