# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 50)
y1 = 2 * x + 1
y2 = x ** 2
plt.figure()
plt.plot(x, y1)
plt.plot(x, y2, color='red', linewidth=2, linestyle='--')
# plt.xlim(-1,2)
# plt.ylim(-2,3)

ax = plt.gca()
# 设置有边框和头部边框颜色为空right、top、bottom、left
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
# 设置底边的移动范围，移动到y轴的0位置
# data:移动y轴的位置  outward:  axes:0.0 - 1.0之间的值，整个轴上的比例  center:('axes',0.5) zero:('data',0.0)
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))
# 利用axes对象设置轴线的显示范围，与plt.xlim(-1,2)和plt.ylim(-2,3)的作用相同
ax.set_xlim(-1, 2)
ax.set_ylim(-2, 3)
# 利用axes对象设置坐标轴的标签
ax.set_xlabel('x data')
ax.set_ylabel('y data')

# 设置坐标轴上的数字显示的位置，top:显示在顶部  bottom:显示在底部,默认是none
ax.xaxis.set_ticks_position('top')
ax.yaxis.set_ticks_position('left')
plt.show()

