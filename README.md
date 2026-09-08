# Exercícios 1.1 e 1.2

Implementação dos exercícios de disponibilidade de serviços com replicação.

## Arquivos

- `exercicio_1_1.py` — fórmulas de disponibilidade.
- `exercicio_1_2_Calculo.py` — cálculos e gráficos.
- `exercicio_1_2_Simulador.py` — simulação e comparação.
- `graficos/` — gráficos gerados.

## Instalação

Crie um ambiente virtual:

```bash
python -m venv .venv
```

Ative o ambiente no Windows:

```bash
.venv\Scripts\activate
```

Instale a biblioteca necessária:

```bash
pip install matplotlib
```

## Execução

Para executar os cálculos:

```bash
python exercicio_1_2_Calculo.py
```

Para executar a simulação:

```bash
python exercicio_1_2_Simulador.py
```

## Parâmetros

São analisados diferentes valores de `n`, `k` e `p`.

- `n` — número de servidores.
- `k` — mínimo de servidores disponíveis.
- `p` — probabilidade de um servidor estar disponível.

Os casos principais são:

- `k = 1`
- `k = n/2`
- `k = n`

A simulação utiliza 50.000 rodadas por combinação.

## Fórmula

```text
A(n,k,p) = Σ C(n,i) * p^i * (1-p)^(n-i)
           i=k até n
```

Os resultados analíticos e experimentais são apresentados no terminal e nos gráficos.
