import numpy as np
import matplotlib.pyplot as plt

def f(x):
    if 0 <= x <= 0.25:
        return np.exp(np.sin(x))
    elif 0.25 < x <= 0.5:
        return np.exp(x) - 1/np.sqrt(x)

x = np.linspace(0, 0.5, 100)
y = np.vectorize(f)(x)

plt.plot(x, y, label='f(x)')
x_tangent = 0.3

if 0 <= x_tangent <= 0.25:
    df_dx = np.cos(x_tangent) * np.exp(np.sin(x_tangent))
elif 0.25 < x_tangent <= 0.5:
    df_dx = np.exp(x_tangent) + 0.5 * x_tangent**(-1.5)


tangent = df_dx * (x - x_tangent) + f(x_tangent)


plt.plot(x, tangent, label='Касательная', linestyle='--')

plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid()
plt.title('График функции и касательной')

plt.show()
