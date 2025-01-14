import numpy as np
import matplotlib.pyplot as plt

def mu_i_minus(k, mu_i_prev, x):
    return 0.33 + (mu_i_prev - 0.33) * (0.99 ** (100 - x))

# 参数设置
mu_i_prev = 0.5  # \mu_i(k-1) 的示例值
x_values = np.linspace(0, 100, 1000)  # x 从 0 到 100

# 计算 \mu_{i}^{-}(k|k-1)
mu_values = mu_i_minus(1, mu_i_prev, x_values)

# 绘制图形
plt.figure(figsize=(10, 6))
plt.plot(x_values, mu_values, label=r'$\mu_{i}^{-}(k|k-1)$', color='blue')

# 标注上周期的 \mu_i(k-1) 值
plt.annotate(f'$\mu_i(k-1) = {mu_i_prev}$', xy=(80, 0.4), fontsize=12, color='red')

plt.title(r'Function Plot of $\mu_{i}^{-}(k|k-1)$')
plt.xlabel('x')
plt.ylabel(r'$\mu_{i}^{-}(k|k-1)$')
plt.grid(True)
plt.legend()
plt.show()
