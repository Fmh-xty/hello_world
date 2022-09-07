import numpy as np
import cvxpy as cp
# 构造决策向量, boolean=True表示0, 1解
x = cp.Variable((5, 1), boolean=True)
# 构造目标向量
c = np.array([[150., 210, 60, 80, 180]])
# 构造约束条件系数阵
A = np.array([[210., 300, 100, 130, 260]])
A1 = np.array([[1., 1, 1, 0, 0],
              [0, 0, 1, 1, 0],
              [1, 0, 0, 0, 1]])
# 构造资源向量
b1 = np.array([[1., 1, 2]]).T
# 构造目标函数
obj = cp.Maximize(c  @ x)
# 构造约束条件
con = [A@x <= 600, A1@x == b1]
# cvxpy构造问题
prob = cp.Problem(obj, con)
# GLPK_MI解决方法
prob.solve(solver='GLPK_MI')
# 打印结果
print('最优值：{}\n最优解:\n{}'.format(prob.value, x.value))