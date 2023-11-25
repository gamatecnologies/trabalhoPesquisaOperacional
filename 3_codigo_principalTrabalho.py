# ============ TRABALHO PESQUISA OPERACIONAL =================
# Feito por: Caio Amorim, Marcela Almeida, Samuel Romaskevis, Wenner Cruz
# ------------------------------------------------------------
# CODIGO PRINCIPAL
# Descrição: Problema da loja de jóias Gammasi, o objetivo é saber qual a quantidade correta
# de materiais precisa ser usado para gerar o lucro maximo.

def print_table(table):
    for row in table:
        print(" ".join(map(lambda x: f"{x:.2f}", row)))

def simplex_maximize(c, A, b):
    m, n = len(A), len(c)

    # Multiplica por -1 para transformar o problema de minimização em maximização
    c = [-x for x in c]

    # Adicionando variáveis de folga e criando a tabela inicial
    table = [[0.0] * (n + m + 1) for _ in range(m + 1)]
    for i in range(m):
        table[i + 1][:n] = A[i]
        table[i + 1][n + i] = 1.0
        table[i + 1][-1] = b[i]

    table[0][:n] = c

    print("Tabela Inicial:")
    print_table(table)

    iteration = 1
    while any(x < 0 for x in table[0][:-1]):
        pivot_col = min(range(n + m), key=lambda i: table[0][i])

        ratios = [(i, table[i][-1] / table[i][pivot_col]) for i in range(1, m + 1) if table[i][pivot_col] > 0]
        if not ratios:
            break

        pivot_row = min(ratios, key=lambda x: x[1])[0]

        pivot_value = table[pivot_row][pivot_col]
        table[pivot_row] = [x / pivot_value for x in table[pivot_row]]

        for i in range(m + 1):
            if i != pivot_row:
                factor = table[i][pivot_col]
                table[i] = [x - factor * table[pivot_row][j] for j, x in enumerate(table[i])]

        print(f"\nIteração {iteration}:")
        print_table(table)
        iteration += 3

    # Extrai as variáveis originais
    x_optimal = [table[i][-1] if i < m + 1 else 0.0 for i in range(8)]
    Z_optimal = table[0][-1]  

    print("\nSolução Ótima encontrada:")
    print_table(table)
    print(f"Z* (Quantidade de material necessário) = {Z_optimal:.2f}")
    print(f"Ouro = {x_optimal[1]:.2f}")
    print(f"Prata = {x_optimal[2]:.2f}")
    print(f"Metal = {x_optimal[3]:.2f}")
    print(f"Reciclável = {x_optimal[4]:.2f}")
    print(f"Acrílico = {x_optimal[5]:.2f}")
    print(f"Nylon = {x_optimal[6]:.2f}")
    print(f"Gancho = {x_optimal[7]:.2f}")
    

# Coeficientes da função objetivo para maximização
c_maximize = [50, 30, 20, 10]

# Coeficientes das restrições
A_maximize = [
    [68, 38, 28, 58],
    [26, 16, 10, 30],
    [20, 10, 5, 25],
    [5, 3, 2, 0],
    [3, 2, 0, 0],
    [0, 4, 8, 4],
    [8, 4, 0, 0]
]

# Limites superiores das restrições
b_maximize = [300, 600, 100, 25, 10, 50, 25]

# Resolvendo o problema de programação linear para maximização
simplex_maximize(c_maximize, A_maximize, b_maximize)

