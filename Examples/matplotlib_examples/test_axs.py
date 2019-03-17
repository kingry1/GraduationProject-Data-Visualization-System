# -*- coding: utf-8 -*-

# 导入绘图模块
import matplotlib.pyplot as plt
import numpy as np

# 中文乱码的处理
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 构建数据
GDP = [12406.8, 13908.57, 9386.87, 9143.64]

# plt.rcParams['figure.figsize'] = (6.0, 4.0) # 设置figure_size尺寸
# plt.rcParams['savefig.dpi'] = 300
# plt.rcParams['figure.dpi'] = 300

plt.figure(num=1, figsize=(16, 8), dpi=300)
fig, axs = plt.subplots(2, 2)

# 绘图
axs[0, 0].bar(range(4), GDP, align='center', color='steelblue', alpha=0.8)
# 添加轴标签
axs[0, 0].set_ylabel('GDP')
# 添加标题
axs[0, 0].set_title(u'四个直辖市GDP大比拼')
# 添加刻度标签
axs[0, 0].set_xticks(range(4), [u'北京市', u'上海市', u'天津市', u'重庆市'])
# 设置Y轴的刻度范围
axs[0, 0].set_ylim([5000, 15000])
axs[0, 0].set_yticks(np.linspace(5000, 15000, 10, endpoint=True))

# 为每个条形图添加数值标签
for x, y in enumerate(GDP):
    axs[0, 0].text(x, y + 100, '%s' % round(y, 1), ha='center')
# 显示图形
plt.show()
