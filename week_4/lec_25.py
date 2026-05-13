# import matplotlib.pyplot as plt
#import：Python的关键字，作用是导入外部模块/库
#matplotlib：Python最主流的数据可视化第三方库
# .pyplot ： matplotlib 库里的一个核心模块，提供面向对象的绘图接口
#as plt ：as关键字用来给导入的模块起别名

# 解决中文显示
# plt.rcParams['font.sans-serif'] = ['SimHei']
# 1.  plt.rcParams ：matplotlib 的全局配置字典，用来修改所有默认设置。

# 2.  font.sans-serif ：代表无衬线字体（图表所有文字的字体设置）。

# 3.  = ['SimHei'] ：指定默认字体为 黑体。
 
# 作用：强制让图表所有文字改用黑体，专门解决中文变成方框乱码。

# 解决负号乱码
# plt.rcParams['axes.unicode_minus'] = False
# 1.axes.unicode_minus ：坐标轴上的负号编码设置。

# 2.  = False ：关闭负号的 unicode 编码模式。

# x=[1,2,3,4,5]
# y=[6,7,8,9,0]
# plt.figure('exp')
# #plt.figure(num=画布名称,figsize=(宽度,高度))：新建一张空白画布
# plt.plot(x,y)
# # plt.plot(x轴数据,y轴书局，格式字符串，其它参数)：是用来画折线图的（或带标记的线）的函数图像，它会把你给的点按顺序用线段连起来，用来展示数据趋势、变化和连续性
# plt.title("x,y折线图")#用来设置标题的
# # plt.show()
# plt.figure('xxy')
# plt.scatter(x,y)
# #plt.scatter(X轴数据，Y轴数据，s=点的大小，c=点的颜色，其它参数)
# #用来画散点图的函数，它只会把你给的每个点画出来，不会用线连接，用来展示数据的分布、相关性和离散程度
# plt.xlabel("横坐标")
# plt.ylabel("纵坐标")
# plt.xlim(1,5)#设置x轴的范围
# plt.ylim(1,10)#设置y轴的范围
# plt.xticks((1,2,3,4,5),('jan','feb','mar','apr','may'))
# #给横坐标的每个点命名
# plt.show()

import matplotlib.pyplot as plt

# --- 解决中文和负号乱码问题 ---
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 数据定义
months = range(1, 13, 1)  # 月份 1-12
boston = [28, 32, 39, 48, 59, 68, 75, 73, 66, 54, 45, 34]
phoenix = [54, 57, 61, 68, 77, 86, 91, 90, 84, 73, 61, 54]

# 绘制两条折线，并给它们加上标签（用于图例）
plt.subplot(2,1,1)
# plt.subplot(norws,ncols,index)：在一个画布上创建多个子图。 nrows：子图的行数。 ncols：子图的列数。 index：当前子图的编号（从 1 开始，从左到右，从上到下开始计数）
plt.ylim(0,100)
plt.plot(months, boston,'vb-', label='Boston',linewidth=2)
plt.title('Ave. Temperatures Boston vs Phoenix')
plt.xlabel('Month')
plt.ylabel('Degrees F°')
plt.xticks(
    (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),
    ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
)
plt.legend(loc='best', fontsize=10,title='city')

plt.subplot(2,1,2)
plt.ylim(0,100)
plt.plot(months, phoenix, label='Phoenix',color='g',linestyle='--',marker='^',linewidth=3)

# 添加坐标轴标签
plt.xlabel('Month')
plt.ylabel('Degrees F°')

# 自定义X轴刻度：把数字1-12换成月份缩写
plt.xticks(
    (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),
    ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
)

# 添加图例（显示每条线代表的城市），放在最佳位置
plt.legend(loc='best', fontsize=10,title='city')
#loc  设置图例位置  loc='best' （自动选不挡线条的位置，最推荐）  loc='upper left' （左上角）  loc='upper right' （右上角）

# 显示网格（原视频里的 plt.grid() 也加上）
plt.grid(True, alpha=0.3)

# 显示图表
plt.show()