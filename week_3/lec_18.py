
#########上课的例子
# class Coordinate(object):
#     def __init__(self,xval,yval):
#         #实例的右边必须与属性保持一致
#         self.x=xval
#         self.y=yval
#     #定义了这份特殊的函数方式就可以把坐标打印出来，不然就只是表示一个类
#     def __str__(self):
#         return "<"+str(self.x)+","+str(self.y)+">"

# class circle(object):
#     def __init__(self,center,radius):
#         if type(center) != Coordinate:#从这个地方看出来其实定义一个类就和自己设立一个类似于字符串、浮点数
#             #（接上）、整数、布尔值的东西，只不过那些事python内置的
#             raise ValueError
#         if type(radius) != int:
#             #也可以这样写 if not isintance(radius,int):
#             raise ValueError
#         self.center=center
#         self.radius=radius

#     #判断一个点是否在圆内
#     def is_circle(self,other_c):
#         # self.center=Coordinate()
#         # other_c=Coordinate()
#         #把这个写上会把center和other_c重置为空集 
#         diff_x_sq=(self.center.x-other_c.x)**2
#         diff_y_sq=(self.center.y-other_c.y)**2
#         distance=(diff_x_sq+diff_y_sq)**0.5
#         if distance<=self.radius:
#             return True
#         return False
    
# center=Coordinate(0,0)
# other=Coordinate(3,4)
# circle_1=circle(center,6)
# print(circle_1.is_circle(other))
# print(center)
# print(type(center))




####part_1 为student类添加__len__方法返回成绩数量，添加__eq__方法根据学号判断是否相等
# class Student(object):
#     def __init__(self,name,student_id,grade):
#         self.name=name
#         self.grade=grade
#         self.student_id=student_id
#     #魔术方式：len(对象)自动触发，返回成绩个数
#     def __len__(self):
#         return len(self.grade)
#     #魔术方式：==比较自动触发，按学号判断相等
#     def __eq__(self,other):
#         if not isinstance(other,Student):
#             raise ValueError
#         return self.student_id==other.student_id
    
# if __name__=="__main__":
#     student_1=Student("佳佳","2411040063",[95,96,100])
#     student_2=Student("小明","2411040066",[93,92,95])
#     student_3=Student("JJ","2411040063",[98,99,97])
#     print(len(student_1))#在调用len()时可以直接把所有都填进去，它会自动识别哪一个要提取长度
#     print(student_1==student_3)#同理不用拿学号进行比较，而是可以直接把整个类进行比较，会自动识别
#     print(student_1==student_2)
    


#####part_2 为BankAccount类添加__add__方法实现账户合并
# class BankAccount(object):
#     def __init__(self,owner,balance,bank_name):
#         self.owner=owner
#         self.balance=balance
#         self.bankname=bank_name
#     #魔术方法：把所有属性中的某一个要求相加
#     def __add__(self,other):
#         if not isinstance(other,BankAccount):
#             raise ValueError
#         return self.balance+other.balance
#     #类方法修改银行名称
#     def set_bank_name(self):
#         name=input("请输入新的银行名称：")
#         self.bankname=name
#         return self#如果是return self.banknaem 最后显示的就只会是银行的名称，这样返回能够显示所有的信息
    
#     def __str__(self):
#         return(f"账户所有者：{self.owner}\n"f"账户余额：{self.balance}\n"f"开户银行：{self.bankname}")
    
# if __name__=="__main__":
#     owner_1=BankAccount("佳佳",10000000000,"工商银行")
#     other=BankAccount("JJ",9999999999,"农业银行")
#     print(owner_1+other)
#     print(other.set_bank_name())


#######part_2 实现一个Fraction类，表示分数，支持加法，减法，比较运算
class Fraction(object):
    def __init__(self,numerator,denominator):
        if denominator==0:
            raise ValueError("分母不能为零")
        self.nume=numerator
        self.deno=denominator

    def __add__(self,other):
        if not isinstance(other,Fraction):
            raise ValueError("还没有添加加小数或整数的代码")
        top=self.nume*other.deno+other.nume*self.deno
        bottom=self.deno*other.deno
        return Fraction(top,bottom)
    
    def __sub__(self, other):
        if not isinstance(other,Fraction):
            raise ValueError("还没有添加加小数或整数的代码")
        top=self.nume*other.deno-other.nemo*self.deno
        bottom=self.deno*other.deno
        return Fraction(top,bottom)
    
    def __eq__(self,other):
        return self.nume*other.deno==self.deno*other.nume
    #求最大公约数的辅助函数
    def gcd(self,a,b):
            while b != 0:
                a,b=b,a%b
            return a
            

    def __str__(self):
        #计算分子分母的最大公约数
        g=self.gcd(abs(self.nume),abs(self.deno))
        reduced_nume=self.nume//g
        reduced_deno=self.deno//g
        #保证分母为正，符号放在分子
        if reduced_deno<0:
            reduced_nume=-reduced_nume
            reduced_deno=-reduced_deno
        return f"{reduced_nume}/{reduced_deno}"
       #return srt(reduced_nume)+"/"+str(reduced_deno)
        
if __name__=="__main__":
    first=Fraction(3,4)
    second=Fraction(6,7)
    third=Fraction(2,8)
    print(third)
    print(first.__add__(second))
    print(first+second)
    

    

        