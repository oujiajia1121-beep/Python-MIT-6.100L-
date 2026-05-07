
# #########例子
# class Coordinate(object):
#     def __init__(self,xval,yval):
#         # print("self是谁？",self)
#         self.x=xval
#         self.y=yval

# # c=Coordinate(3,4)
# # print("实例c是谁？",c)
# # print(c.x,c.y)

# # origin=Coordinate(0,0)
# # print("实例origin是谁？",origin)
# # print(origin.x,origin.y)
# # #self 就是实例本身


# #算两坐标之间的距离
#     def distance(self,other):
#         x_diff_sq=(self.x-other.x)**2
#         y_diff_sq=(self.y-other.x)**2
#         return (x_diff_sq+y_diff_sq)**0.5

# c=Coordinate(3,4)
# origin=Coordinate(0,0)
# print(c.distance(origin))#这个是固定格式，实例.方法名(实例) 意思是“让实例c，计算它和实例origin之间的距离”



#########part_1 定义一个student类，属性有name，student_id,scores(列表)，方法有add_scores(scores),geta_average(),get_highest_score()
# class student(object):
#     def __init__(self,name,student_id,scores):
#         #初始化属性
#         self.name=name
#         self.student_id=student_id
#         self.scores=scores
#     #添加成绩后列表
#     def add_score(self,score):
#         #scores=[]
#         self.scores.append(score)
#         return self.scores
#     #算平均成绩
#     def get_average(self):
#         total=0
#         for i in self.scores:
#             total += i
#         return total/len(self.scores)
#     #取最高成绩
#     def get_highest_score(self):
#         return max(self.scores)
    
# if __name__=="__main__":
#     s=student("张三","2024001",[85,95,78])
#     print("初始成绩：",s.scores)
#     s.add_score(95)
#     print("添加后的成绩：",s.scores)
#     print("平均成绩：",s.get_average())
#     print("最高成绩：",s.get_highest_score())


######part_2 定义一个BankAccount类，属性有owner、balance，方法有deposit(amount)、withddraw(amount)、get_balance()
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

if __name__=="__main__":
    first=BankAccount("小明",100000)
    print("存入1000元，账户余额为：",first.deposit(1000))
    print("取出9000元，账户余额为：",first.withdraw(9000))
    print("取出1000000元，账户余额为：",first.withdraw(1000000))
