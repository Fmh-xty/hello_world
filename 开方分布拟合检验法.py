import numpy as np
import scipy.stats as ss
# 数据来源P147 表4.8
n = 238   # 样本总量
alpha = 0.05  # 显著性水平
r = 0  # 未知参数的个数
k = np.arange(1., 8)  # 数据分组
p = np.tile([1/7], (1, 7))  # 对应分组的对应拟合函数的概率
m = np.array([36., 23, 29, 31, 34, 60, 25])  # 对应分组的频数
cha2 = np.sum(m**2/(n*p))-n   # 统计量的观察值计算
cha2a = ss.chi2.ppf(1-alpha, len(k)-1-r)  # 上alpha分位点计算， len(k)-1-r表示自由度
print(cha2, cha2a)    # 输出统计量的观察值和分位点， 进行假设检验分析