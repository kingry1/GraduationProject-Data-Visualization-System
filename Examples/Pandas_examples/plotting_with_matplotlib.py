# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pandas import Series, DataFrame


# fig, axes = plt.subplots(2, 1)
fig, axes = plt.subplots(2, 2, figsize=(8, 8), dpi=300)
s = Series(np.random.randn(10).cumsum(), index=np.arange(0, 100, 10))
# s.plot(ax=axes[1])
s.plot(kind='line', ax=axes[1, 1])
axes[1, 1].set_ylabel('GDP')
plt.show()
