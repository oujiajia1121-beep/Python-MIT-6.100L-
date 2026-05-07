########实例 
#
# class Animal(object):
#     def __init__(self,age):
#         self.years=age
#         self.name=None

#     def __str__(self):
#         return "animal:"+str(self.name)+":"+str(self.years)
    
#     def get_age(self):#getter 获取器：拿数据用
#         return self.years
    
#     def set_name(self,newname):
#         self.name=newname
    
#     def set_age(self,newage):#setter 设置器：该数据用，带 规则效验
#         if newage>0:
#             self.years=newage
#         else :
#             print("年龄不合法")

# def animal_dict(l):
#     d={}
#     for n in l :
#         if type(n)==int and n>=0:
#             d[n]=Animal(n)
#     return d

# def make_animals(l1,l2):
#     l3=[]
#     for i in range (len(l1)):
#         age=l1[i]
#         name=l2[i]
#         a=Animal(age)
#         a.set_name(name)
#         l3.append(a)
#     return l3#这个缩进一定要和for一行，不让就会只打印一个结果 
# l=[2,5,0]
# l2=["rabbit","lion","tiger"]
# animals=make_animals(l,l2)
# for i in animals:
#     print(i)
# #print(animals)#直接打印只是在最表层，python 不知道该怎样去表达一个类的字典
# #正确表达
# # for n,a in animals.items():
# #     print(f'key{n} with val {a}')
# #当输出是字典，列表，或者是其他组合时，print不会立即调用__str__来清晰打印，而是调用__repr__,打印结果只是字典值视图
# # print(animal_dict(l).values())

# ###########  Inheritance
# #cat时animal中的一个子集就可以这样表示
# class Cat(Animal):#animal的子集会复制和继承animal类中的所有函数，包括__str__,setter,getter所有内容 
#     #如果是子集，cat会复制animal中的属性，不用在定义__init__():


#########实例.2
# class Rabbit(Animal):
#     tag=1
#     def __init__(self,age,parent1=None,parent2=None):
#         Animal.__init__(self,age)
#         self.parent1=parent1
#         self.parent2=parent2
#         self.rid=Rabbit.tag
#         Rabbit.tag += 1

#     def get_rid(self):
#         return str(self.rid).zfill(5)#zfill(数字)：指定几位数如果没有就在前面补0
    
#     def __add__(self,other):
#         return Rabbit(0,self,other)


# r1=Rabbit(8)
# r2=Rabbit(6)
# r3=Rabbit(7)
# r4=r1+r2
# print(r1.get_rid())
# print(r4)

#########part.1 定义Dog和Cat子类继承Animal，重写speak()方法
# class Animal(object):
#     def __init__(self,name):
#         self.name=name
    
#     def speak(self):
#         print("各种动物的叫声")

# class Dog(Animal):
#     def __init__(self,name,age,type=None):
#         Animal.__init__(self,name)
#         self.age=age
#         self.type=type

#     def speak(self):
#         print("汪汪")

#     def __str__(self):
#         return f"{self.name}今年{self.age}岁了，是一条可爱的{self.type}"
    
# class Cat(Animal):
#     def __init__(self,name,age,type=None):
#         Animal.__init__(self,name)
#         self.age=age
#         self.type=type

#     def speak(self):
#         print("喵喵")

#     def __str__(self):
#         return f"{self.name}今年{self.age}岁了，是一只可爱的{self.type}"
    
# if __name__=="__main__":
#     dog=Dog("毛毛",4,"金毛")
#     cat=Cat("Kitty",2,"金渐层")
#     print(dog)
#     dog.speak()
#     print(cat)
#     cat.speak()


##########part.2 定义Vehicle类，有__init__(make,model,year)和start(),stop()方法。定义Car和Motorcycle子类，添加各自的属性(如Car有num_doors)
# class Vechile(object):
#     def __init__(self,make,model,year):
#         self.make=make
#         self.model=model
#         self.year=year
#         self.is_running=False

#     def start(self):
#         """启动交通工具
#         """
#         if not self.is_running:
#             self.is_running=True
#             print(f"{self.year} {self.make} {self.model}已启动")

#         else:
#             print(f"{self.year} {self.make} {self.model}未启动")

#     def stop(self):
#         """暂停交通工具
#         """
#         if self.is_running:
#             self.is_running=False
#             print(f"{self.year} {self.make} {self.model}已停止")

#         else:
#             print(f"{self.year} {self.make} {self.model}已处于停止状态")

# class Car(Vechile):
#     def __init__(self,num_doors,make,model,year):
#         super().__init__(make,model,year)#用super(). 调用时不需要传 self
#         self.num_doors=num_doors

#     def get_num_doors(self):
#         print(f"{self.model}有{self.num_doors}个轮子")

#     def __str__(self):
#         return f"{self.model}是{self.make} {self.year}年生产的"


# class Motorcycle(Vechile):
#     def __init__(self,num_doors,make,model,year):
#         Vechile.__init__(self,make,model,year)#用 父类. 时需要传self
#         self.num_doors=num_doors

#     def get_num_doors(self):
#         print(f"{self.model}有{self.num_doors}个轮子")

#     def __str__(self):
#         return f"{self.model}是{self.make} {self.year}年生产的"
    
# if __name__=="__main__":
#     a=Car(4,"大众","SUV",2006)
#     b=Motorcycle(2,"川崎摩托株式会社","川崎",1961)
#     print(a)
#     a.get_num_doors()
#     a.start()
#     a.stop()
#     print(b)
#     b.get_num_doors()
#     b.start()
#     b.stop()



##########part.3 实现一个SavingAccount类继承BankAccount，添加interest_rate属性和apply_interest()方法
class BankAccount(object):
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount
        return self.balance
    
    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance -= amount
            return self.balance
        else:
            print("账户余额不足")
            return self.balance-amount
        
class SavingAccount(BankAccount):
    def __init__(self,owner,balance,interest_rate,years):
        super().__init__(owner,balance)
        self.interest_rate=interest_rate
        self.years=years

    def apply_interest(self):
        #计算单利
        # interest=self.balance * self.interest_rate * self.years
        # self.balance += interest
        #算复利
        self.balance=self.balance*(1+self.interest_rate)**self.years
        return self.balance

    def __str__(self):
        #先调用apply_interest计算利息，再显示最终余额
        self.apply_interest()
        return f"{self.owner}，您的账户余额按{self.interest_rate}利率来算，存{self.years}年，包括利息在内的总余额为{self.balance}"
    

if __name__=="__main__":
    bankaccount=SavingAccount("佳佳",100000000,0.03,10)
    print(bankaccount)