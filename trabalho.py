

from pulp import LpMaximize, LpProblem, LpVariable

# Cria o problema de maximização
problem = LpProblem(name="Maximize_Profit", sense=LpMaximize)

# Variáveis de decisão
x1 = LpVariable(name="x1", lowBound=0, cat="Continuous")
x2 = LpVariable(name="x2", lowBound=0, cat="Continuous")

# Função objetivo
problem += 5 * x1 + 4 * x2, "Objective"

# Restrições
problem += 2 * x1 + x2 <= 100, "Constraint1"
problem += x1 + 3 * x2 <= 90, "Constraint2"

# Resolve o problema
problem.solve()

# Imprime os resultados
print("Status:", problem.status)
print("Quantidade de A a ser produzida:", x1.value())
print("Quantidade de B a ser produzida:", x2.value())
print("Lucro máximo:", problem.objective.value())
