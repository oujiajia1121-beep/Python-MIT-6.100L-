########实例
import time
def sum_of(l):
    total=0.0
    for elt in l:
        total=total+elt
    return total
l_n=[1]
for i in range(7):
    l_n.append(l_n[-1]*10)
print(l_n)
for n in l_n:
    l=list(range(n))
    t=time.perf_counter()#就当前的高精度时间，作为计时的起点。
    #time.perf_counter() 是来统计对这个列表做操作的耗时 是 time 里的内置函数
    s=sum_of(l)
    dt=time.perf_counter()-t
    print(f"sum_of  {n}  took  {dt}  seconds(  {1/dt}  /sec)")
