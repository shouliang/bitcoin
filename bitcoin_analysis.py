# 比特币走势预测，使用时间序列ARMA
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

import warnings
from itertools import product
from datetime import datetime
warnings.filterwarnings('ignore')

# 数据加载
df = pd.read_csv('./bitcoin_2012-01-01_to_2018-10-31.csv')
