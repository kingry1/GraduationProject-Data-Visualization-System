# -*- coding: utf-8 -*-

# 导入绘图模块
import matplotlib.pyplot as plt
import numpy as np

# 中文乱码的处理
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.figure(1, figsize=(8, 8), dpi=300)
labels = [u'娱乐', u'育儿', u'饮食', u'房贷', u'交通', u'其它']
sizes = [2, 5, 12, 70, 2, 9]
explode = (0, 0, 0, 0.1, 0, 0)
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=False, startangle=150)
plt.title(u"饼图示例-8月份家庭支出")
plt.show()
