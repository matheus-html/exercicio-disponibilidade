import matplotlib.pyplot as plt
from exercicio_1_1 import disponibilidade

valores_p = [0.1, 0.3, 0.5, 0.7, 0.9, 0.95, 0.99]

# variando p
n = 6

print("Disponibilidade variando p")
print("k    p       resultado")

for k in [1, n // 2, n]:
    for p in valores_p:
        print(f"{k}    {p:.2f}    {disponibilidade(n, k, p):.6f}")

    resultado = []
    for p in valores_p:
        resultado.append(disponibilidade(n, k, p))

    plt.plot(valores_p, resultado, marker="o", label=f"k={k}")

plt.xlabel("p")
plt.ylabel("Disponibilidade")
plt.title("Disponibilidade variando p")
plt.legend()
plt.grid()
plt.savefig("graficos/analitico_por_p.png")
plt.close()


# variando n
p = 0.9
valores_n = [2, 4, 6, 8, 10, 12]

print("\nDisponibilidade variando n")
print("k    n       resultado")

for n in valores_n:
    print(f"1    {n}       {disponibilidade(n, 1, p):.6f}")
    print(f"{n//2}    {n}       {disponibilidade(n, n//2, p):.6f}")
    print(f"{n}    {n}       {disponibilidade(n, n, p):.6f}")

for nome in ["k=1", "k=n/2", "k=n"]:
    resultado = []

    for n in valores_n:
        if nome == "k=1":
            k = 1
        elif nome == "k=n/2":
            k = n // 2
        else:
            k = n

        resultado.append(disponibilidade(n, k, p))

    plt.plot(valores_n, resultado, marker="o", label=nome)

plt.xlabel("n")
plt.ylabel("Disponibilidade")
plt.title("Disponibilidade variando n")
plt.legend()
plt.grid()
plt.savefig("graficos/analitico_por_n.png")
plt.close()


# variando k
n = 10
p = 0.9

resultado = []

for k in range(1, n + 1):
    resultado.append(disponibilidade(n, k, p))

print("\nDisponibilidade variando k")
print("k    resultado")

for k in range(1, n + 1):
    print(f"{k}    {resultado[k - 1]:.6f}")

plt.figure()
plt.plot(range(1, n + 1), resultado, marker="o")
plt.xlabel("k")
plt.ylabel("Disponibilidade")
plt.title("Disponibilidade variando k")
plt.grid()
plt.savefig("graficos/analitico_por_k.png")
plt.close()