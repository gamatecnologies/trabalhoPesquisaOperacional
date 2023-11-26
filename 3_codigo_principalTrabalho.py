# ============ TRABALHO PESQUISA OPERACIONAL =================
# Feito por: Caio Amorim, Marcela Almeida, Samuel Romaskevis, Wenner Cruz
# ------------------------------------------------------------
# CODIGO PRINCIPAL
# Descrição: Problema da loja de jóias Gammasi, o objetivo é saber qual a quantidade correta
# de materiais precisa ser usado para gerar o lucro maximo.
def print_table(table):
    for row in table:
        print(" ".join(map(str, row)))

def simplex_maximize(c, A, b):
    m, n = len(A), len(c)

    # Multiplica por -1 para transformar o problema de minimização em maximização
    c = [-x for x in c]

    # Adicionando variáveis de folga e criando a tabela inicial com números inteiros
    table = [[0] * (n + m + 1) for _ in range(m + 1)]
    for i in range(m):
        table[i + 1][:n] = A[i]
        table[i + 1][n + i] = 1
        table[i + 1][-1] = b[i]

    table[0][:n] = c

    iteration = 1
    while any(x < 0 for x in table[0][:-1]):
        # Encontrar a coluna do elemento pivô (mais negativo)
        pivot_col = min(range(n + m), key=lambda i: table[0][i])

        # Calcular as razões para encontrar a linha do elemento pivô
        ratios = [(i, table[i][-1] / table[i][pivot_col]) for i in range(1, m + 1) if table[i][pivot_col] > 0]
        if not ratios:
            break

        # Encontrar a linha do elemento pivô com a menor razão
        pivot_row = min(ratios, key=lambda x: x[1])[0]

        # Normalizar a linha do elemento pivô
        pivot_value = table[pivot_row][pivot_col]
        table[pivot_row] = [x // pivot_value for x in table[pivot_row]]

        # Atualizar as outras linhas da tabela
        for i in range(m + 1):
            if i != pivot_row:
                factor = table[i][pivot_col]
                table[i] = [x - factor * table[pivot_row][j] for j, x in enumerate(table[i])]

        print(f"\nIteração {iteration}:")
        print_table(table)
        iteration += 1

    # Extrai as variáveis originais
    x_optimal = [table[i][-1] if i < m + 1 else 0 for i in range(n)]
    Z_optimal = table[0][-1]  # Mantendo o sinal negativo

    print("\nSolução Ótima encontrada:")
    print_table(table)
    print(f"Z* (Valor máximo): {Z_optimal}")
    print(f"Número de colares: {x_optimal[0]}")
    print(f"Número de pulseiras: {x_optimal[1]}")
    print(f"Número de brincos: {x_optimal[2]}")
    print(f"Número de anéis: {x_optimal[3]}")

    return x_optimal, Z_optimal

# Coeficientes da função objetivo para maximização
c_maximize = [50, 30, 20, 10]

# Coeficientes das restrições
A_maximize = [
    [68, 38, 28, 58],
    [26, 16, 10, 30],
    [20, 10, 5, 25],
    [5, 3, 2, 0],
    [0, 2, 0, 0],  # Acrílico
    [0, 4, 8, 4],
    [8, 4, 0, 0]
]

# Limites superiores das restrições
b_maximize = [300, 600, 100, 25, 10, 50, 25]

# Resolvendo o problema de programação linear para maximização
solution = simplex_maximize(c_maximize, A_maximize, b_maximize)

# A solução ótima pode ser acessada da seguinte forma:
x_optimal, Z_optimal = solution

