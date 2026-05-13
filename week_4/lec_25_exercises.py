import matplotlib.pyplot as plt

# 生成x轴数据（0~9的整数）
x = list(range(1000))

# 三条曲线的y值计算（修正了类型问题，直接用i计算）
y = [i**2 for i in x]       # y = x²
y_1 = [i**3 for i in x]    # y = x³
y_2 = [2**i for i in x]    # y = 2^x（指数函数）

# 绘制三条曲线，设置样式和标签
plt.plot(x, y, '*b-', label='y=x**2')
plt.plot(x, y_1, '*b--', label='y=x**3')
plt.plot(x, y_2, '^r:', label='y=2**x')

# 设置坐标轴标签和图例
plt.xlim(0,10)
plt.ylim(0,1000)
plt.xlabel('X')
plt.ylabel('Y')
plt.legend(loc='best', fontsize=10)

# 显示图像
plt.show()


