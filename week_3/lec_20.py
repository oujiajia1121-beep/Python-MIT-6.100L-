########实例——1
# from dateutil import parser#正确导入时间解析器
# class Workout:
#     cal_per_hour=200
#     def __init__(self,start,end,calories=None):
#         #把时间字符串转化为datetime
#         self.start=parser.parse(start)
#         self.end=parser.parse(end)
#         self.calories=calories#如果没有输入就默认为None
#         self.icon="😭"
#         self.kind="Workout"

#     def get_calories(self):
#         if (self.calories==None):
#             return self.cal_per_hour*(self.end-self.start).total_seconds()/3600#这样的操作在datetime对象上是允许的
#             #这里的 self.cal_per_hour 也可以写成 Workout.cal_per_hour
#             #delta=self.end-self.start
#             #delta.total_seconds()是相当于dateutil类里面的内置方法，表示总用时多少秒这里还/3600是把它置换成了小时
#         else:
#             return self.calories
        
#     def __str__(self):
#         calories=self.get_calories()
#         return f"用时{(self.end-self.start).total_seconds()/3600}小时，消耗的卡路里为{calories}"
    

# if __name__=="__main__":
#     w_one=Workout("June 1 2021 3:30 PM","June 1 2021 4:00 PM",300)
#     print(w_one)



############part.1 独立设计一个“图书管理系统”：包含Book类和Library类，支持添加书籍，借阅，归还，搜索
class Book(object):
    def __init__(self,book_id,book_name,author):
        self.book_id=book_id
        self.book_name=book_name
        self.author=author
        self.is_borrow=False#False未出借，True已出借

class Library(object):
    def __init__(self):
        #存储所有书籍列表
        self.books_list=[]
    #添加书籍
    def add_books(self,newbook):
        if isinstance(newbook,Book):
                if newbook in self.books_list:
                    print(f"{newbook.book_name}该书已经存在图书系统中")
                else:
                    self.books_list.append(newbook)
                    return self.books_list
        else:
            raise ValueError ("添加的不是书")#添加的内容要用括号括起来，不然就错了
     #按编号借阅书籍   
    def borrow_book(self,book_id):
        for book in self.books_list:
            if book.book_id == book_id:#这个地方book里面包括book_id、book_name、author，用book.book_id 就可以特指里面的book_id
                if not book.is_borrow:
                    book.is_borrow=True
                    print(f"📚成功借阅：{book.book_name}")
                else:
                    print(f"❌️该书已被借出，无法借阅")
                return
        print("❌️未找到该书编号")
        
    #归还书籍
    def return_books(self,book_id):
        for book in self.books_list:
            if book.book_id==book_id:
                if book.is_borrow:
                    book.is_borrow=False
                    print(f"成功归还：{book.book_name}")
                else:
                    print(f"该书籍未被借出无需归还")
                return 
        print("未找到该书籍编号")
    
    #搜素书籍，按书名模糊搜索
    def search_book(self,name):
        print("\n---------------------------搜索结果------------------------------")
        flag=False
        for book in self.books_list:
            if name in book.book_name:
                status="已借出" if book.is_borrow else "可借阅"
                print(f"编号：{book.book_id} 书名：{book.book_name} 作者：{book.author} 状态：{status}")
                flag=True
        if not flag:
            print("未搜索到相关书籍")

    #查看全部书籍
    def show_all_book(self):
        print("\n==============所有图书===============")
        if len(self.books_list)==0:
            print("暂无书籍")
            return
        for book in self.books_list:
            status="已借出" if book.is_borrow else "可借阅"
            print(f"编号：{book.book_id} | 书名：{book.book_name} | 作者：{book.author} | 状态：{status}")

if __name__=="__main__":
    lib=Library()
    #添加测试书籍
    b1=Book(101,"西游记","吴承恩")
    b2=Book(102,"红楼梦","曹雪芹")
    b3=Book(103,"Python编程","张三")
    lib.add_books(b1)
    lib.add_books(b2)
    lib.add_books(b3)
    lib.add_books(b3)
    #查看所有书籍
    lib.show_all_book()
    #借阅书籍
    lib.borrow_book(101)
    lib.borrow_book(103)
    #归还书籍
    lib.return_books(101)
    #搜索书籍
    lib.search_book("西")
    lib.show_all_book()




