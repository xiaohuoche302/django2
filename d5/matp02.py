import matplotlib
from matplotlib import pyplot as plt  # 绘图

#显示中文
matplotlib.rcParams["font.sans-serif"] = ["simhei"]  # 配置字体
matplotlib.rcParams["font.family"] = "sans-serif"

# (x,y)
plt.plot([1,2],[3,4],'--',color='r',label='line1')
plt.xlabel('x轴')
plt.xlabel('y轴')
plt.legend()#绘制
plt.show()

#柱状图
plt.bar([1],[123],label="广州")
plt.bar([2],[23],label="苏州")
plt.bar([4],[63],label="杭州")
plt.legend()
plt.show()