# -*- coding: utf-8 -*-
"""
@author: tz_zs
"""
import matplotlib.pyplot as plt
import pandas as pd

list_l = [[1, 4, 3, 5, 4], [11, 15, 15, 13, 9], [4, 2, 7, 9, 3], [15, 8, 12, 6, 11]]
date_range = pd.date_range(start="20180701", periods=4)
df = pd.DataFrame(list_l, index=date_range,
                  columns=['a', 'b', 'c', 'd', 'e'])
print(df['a'])

fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, gridspec_kw={'height_ratios': [1, 1, 1, 1]},
                                         figsize=(10, 12))
df["a"].plot(ax=ax1)
ax1.set_xlabel("time")
ax1.set_ylabel("num_a")
ax1.legend(loc="best")
ax1.grid(True)

df["b"].plot(ax=ax2)
ax2.set_xlabel("time")
ax2.set_ylabel("num_b")
ax2.legend(loc="best")
ax2.grid(True)
ax2.set_ylim(2, 10)  # 限制y轴显示的区间

df["c"].plot(ax=ax3)
ax3.set_xlabel("time")
ax3.set_ylabel("num_c")
ax3.legend(loc="best")
ax3.grid(True)
ax3.scatter(df.index, df["c"], c="red", marker="v")  # 在拐点处画标记

df["d"].plot(ax=ax4)
ax4.set_xlabel("time")
ax4.set_ylabel("num_d")
ax4.legend(loc="best")
ax4.grid(True)
ax4.scatter(df.index, df["e"], c="red", marker="^")

plt.title("title")
plt.tight_layout()  # 布局紧凑
plt.show()
