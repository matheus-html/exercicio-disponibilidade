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

def disponibilidade(n, k, p):
    return sum(comb(n, i) * p ** i * (1 - p) ** (n - i) for i in range(k, n + 1))

def consulta(n, p):
    return 1 - (1 - p) ** n

def atualizacao(n, p):
    return p ** n