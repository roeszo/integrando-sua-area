import numpy as np
import matplotlib.pyplot as plt

def f(x, a, b, c):
    return a*x**2 + b*x + c

a = float(input("Digite o coeficiente de 'a' da função: " ))
b = float(input("Digite o coeficiente de 'b' da função: " ))
c = float(input("Digite o coeficiente de 'c' da função: " ))

inicio = float(input("Digite o limite inferior do intervalo: "))
fim = float(input("Digite o limite superior do intervalo: "))

x_vals = np.linspace(inicio, fim, 100)
y_vals = f(x_vals, a, b, c)

plt.plot(x_vals, y_vals, label="f(x) = {}x^2 + {}x + {}" .format(a, b, c))
plt.fill_between(x_vals, y_vals, 0, where=(x_vals >= inicio) & (x_vals <= fim), alpha=0.3)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title("Grafico da Função Quadratica")
plt.legend()
plt.grid(True)
plt.show()

n = 1000
h = (fim - inicio) / n

soma = 0.5 * (f(inicio, a, b, c) + f(fim, a, b, c))

for i in range(1, n):
    xi = inicio + i * h
    soma += f(xi, a, b, c)

area = h * soma

print("A área sob a curva é: ", area)
