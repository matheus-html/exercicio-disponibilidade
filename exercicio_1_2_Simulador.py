import random
import matplotlib.pyplot as plt
from exercicio_1_1 import disponibilidade

def simular(n, k, p, rodadas=50000):
    sucessos = 0

    for _ in range(rodadas):
        disponiveis = 0

        for _ in range(n):
            if random.random() <= p:
                disponiveis += 1

        if disponiveis >= k:
            sucessos += 1

    return sucessos / rodadas


valores_p = [0.1, 0.3, 0.5, 0.7, 0.9, 0.95, 0.99]
valores_n = [6, 10]

print("\nComparação analítico x experimental\n")
print(f"{'n':<5}{'k':<8}{'p':<8}{'analítico':<14}{'experimental':<14}")

for n in valores_n:

    resultados = {}

    for nome, k in [("k=1", 1), ("k=n/2", n // 2), ("k=n", n)]:

        analiticos = []
        experimentais = []

        for p in valores_p:
            analitico = disponibilidade(n, k, p)
            experimental = simular(n, k, p)

            analiticos.append(analitico)
            experimentais.append(experimental)

            print(f"{n:<5}{nome:<8}{p:<8.2f}{analitico:<14.6f}{experimental:<14.6f}")

        resultados[nome] = (analiticos, experimentais)

    # Gráfico k = 1
    analiticos, experimentais = resultados["k=1"]

    plt.figure()
    plt.plot(valores_p, analiticos, marker="o", label="analítico")
    plt.plot(valores_p, experimentais, marker="x", linestyle="--", label="experimental")
    plt.xlabel("p")
    plt.ylabel("Disponibilidade")
    plt.title(f"Analítico x experimental (n={n}, k=1)")
    plt.legend()
    plt.grid()
    plt.savefig(f"graficos/comparativo_n{n}_k1.png")
    plt.close()

    # Gráfico k = n/2
    analiticos, experimentais = resultados["k=n/2"]

    plt.figure()
    plt.plot(valores_p, analiticos, marker="o", label="analítico")
    plt.plot(valores_p, experimentais, marker="x", linestyle="--", label="experimental")
    plt.xlabel("p")
    plt.ylabel("Disponibilidade")
    plt.title(f"Analítico x experimental (n={n}, k=n/2)")
    plt.legend()
    plt.grid()
    plt.savefig(f"graficos/comparativo_n{n}_kn2.png")
    plt.close()

    # Gráfico k = n
    analiticos, experimentais = resultados["k=n"]

    plt.figure()
    plt.plot(valores_p, analiticos, marker="o", label="analítico")
    plt.plot(valores_p, experimentais, marker="x", linestyle="--", label="experimental")
    plt.xlabel("p")
    plt.ylabel("Disponibilidade")
    plt.title(f"Analítico x experimental (n={n}, k=n)")
    plt.legend()
    plt.grid()
    plt.savefig(f"graficos/comparativo_n{n}_kn.png")
    plt.close()