import numpy as np
import statsmodels.api as sm
# 获得样本数据, 此例数据来源p151 表4.10
y = np.array([1620., 1670, 1700, 1750, 1800, 1580, 1600, 1640, 1720, 1460, 1540, 1620, 1680, 1500, 1550, 1610])
# 对数据按对应因素，不同水平分组
x = np.hstack([np.full(5, 1.), np.full(4, 2.), np.full(4, 3.), np.full(3, 4.)])
# 构造字典
d = {'x': x, 'y': y}
# 构造模型
model = sm.formula.ols('y~C(x)', d).fit()
# 进行单因素方差分析
anovat = sm.stats.anova_lm(model)
print(anovat)