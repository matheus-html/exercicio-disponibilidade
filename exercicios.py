# Exercício 1.1 - Formula matemática de disponibilidade:
# n = número total de servidores;
# k = número mínimo de servidores disponíveis para o serviço funcionar;
# p = probabilidade de um servidor estar disponível;
# 1 - p = probabilidade de um servidor estar indisponível.

# Primeiro caso: k = 1
# Basta 1 servidor estar disponível.
# Então, A(n, 1, p) = 1 - (1 - p)^n

# Segundo caso: k = n
# Todos os servidores precisam estar disponíveis.
# Então, A(n, n, p) = p^n

# Caso geral:
# O serviço precisa de pelo menos k servidores disponíveis.
# A probabilidade de exatamente i servidores estarem disponíveis é:
# C(n,i) * p^i * (1-p)^(n-i)
# Somando de k até n:
# A(n, k, p) = Σ(i=k até n) C(n,i) * p^i * (1-p)^(n-i)

from math import comb
import random
import matplotlib.pyplot as plt

def disponibilidade(n, k, p):
    return sum(comb(n, i) * p ** i * (1 - p) ** (n - i) for i in range(k, n + 1))

def consulta(n, p):
    return 1 - (1 - p) ** n

def atualizacao(n, p):
    return p ** n

# Exercicio 1.2: Calculo analitico

n_valores = [2, 4, 6, 8, 10, 12]
p_fixo = 0.9

y_k1 = []
for n in n_valores:
    y_k1.append(disponibilidade(n, 1, p_fixo))

y_kn2 = []
for n in n_valores:
    y_kn2.append(disponibilidade(n, n // 2, p_fixo))

y_kn = []
for n in n_valores:
    y_kn.append(disponibilidade(n, n, p_fixo))

plt.figure()
plt.plot(n_valores, y_k1, marker="o", label="k=1")
plt.plot(n_valores, y_kn2, marker="o", label="k=n/2")
plt.plot(n_valores, y_kn, marker="o", label="k=n")
plt.xlabel("n")
plt.ylabel("disponibilidade")
plt.title(f"Disponibilidade analítica (p={p_fixo})")
plt.legend()
plt.grid(True)
plt.savefig("analitico.png")
plt.close()

# Exercicio 1.2: Simulador estocástico