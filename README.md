Descrição do Trabalho de Pesquisa Operacional

Este trabalho propõe a aplicação de conceitos da disciplina Pesquisa Operacional realizada pelo professor Vinicius De Filippo na Escola Superior Dom Helder, onde tem o intuito de resolver um problema de otimização específico. Nossa abordagem envolverá a utilização de programação linear método simpelx para maximizar  uma função objetivo, sujeita a um conjunto de restrições, com o objetivo de encontrar a melhor solução possível.


---------------------------------------------------------------------------------------------------------------------------------------------------------------------
Integrantes do Grupo:

Caio Amorim - E01601,
Marcela Almeida - E01597,
Samuel Romaskesvis - E01752,
Wenner Cruz - E01762.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------
Contexto do Problema:

A loja Gammasi, especializada em jóias e semijóias, está em busca de otimizar suas operações e maximizar as vendas da sua loja online. Para atingir esse objetivo, a loja oferece uma variedade de produtos, incluindo colares, pulseiras, brincos e anéis, cada um com seu preço específico de mercado.

Entretanto, a produção dessas peças demanda diferentes materiais, como ouro, prata, metal, materiais recicláveis, acrílico, nylon e gancho. Existem restrições quanto à quantidade disponível desses materiais, limitando a produção máxima de cada peça.

O desafio é encontrar a combinação ideal de produção dessas peças, considerando as limitações de materiais, de modo a maximizar o lucro total da loja Gammasi.


---------------------------------------------------------------------------------------------------------------------------------------------------------------------

Objetivo:

O objetivo da loja Gammasi é maximizar as vendas da sua loja online, considerando diferentes produtos, tais como colares, pulseiras, brincos e anéis. Cada peça possui um preço de venda específico (R$50 para colares, R$30 para pulseiras, R$20 para brincos e R$10 para anéis). O desafio é determinar a quantidade ideal de cada peça a ser produzida para maximizar o lucro, levando em consideração as restrições dos materiais disponíveis (ouro, prata, metal, materiais recicláveis, acrílico, nylon e gancho).

---------------------------------------------------------------------------------------------------------------------------------------------------------------------

Modelagem Matemática:
Variáveis:
x1:número de colares a serem produzidos
x2: número de pulseiras a serem produzidas
x3: número de brincos a serem produzidos
x4: número de anéis a serem produzidos

Função Objetivo: Max Z=50x1+30x2+20x3+10x4

Restrições:
Restrições de ouro: 68x1+38x2+28x3+58x4≤300
Restrições de prata: 26x1+16x2+10x3+30x4≤600
Restrições de metal: 20x1+10x2+5x3+25x4≤100
Restrições de material reciclável: 5x1+3x2+2x3≤25
Restrições de acrílico: 2x2≤10
Restrições de nylon: 4x2+8x3+4x4≤50
Restrições de gancho: 8x1+4x2≤25
Não-negatividade: x1≥0, x2≥0, x3≥0, x4≥0

OBS: No arquivo 2_trabalho_PO_problema.pdf, apresenta o problema de forma detalhada e sua modelagem.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------

Algoritmo Utilizado:

Desenvolvemos o algoritmo  sem utilizar biblioteca no Python, onde o mesmo tem o objetivo de implementar o problema de programação linear no simplex. Este algoritmo foi escolhido devido à sua eficácia na resolução de problemas de otimização. 

----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Implementação e Execução:

É possivel ver a implementação e execução no link: https://github.com/gamatecnologies/trabalhoPesquisaOperacional.git

Para verificação busque os seguintes arquivos:
1. Código Principal Executavel: 3_codigo_principalTrabalho.py
2. Código Teste: 4_codigo_testeProfessor.py (onde foi realizado obtendo uma resposta já validada)

---------------------------------------------------------------------------------------------------------------------------------------------------------------------

Interpretação dos Resultados:

Esse problema de programação linear busca otimizar a produção de joias e semijoias na loja Gammasi para maximizar o lucro. A loja deseja determinar quantas unidades de cada tipo de jóias (colares, pulseiras, brincos, anéis) deve produzir para maximizar o lucro total, considerando as limitações nos recursos disponíveis.

Os recursos limitados são os materiais necessários para fazer as jóias, como ouro, prata, metal, material reciclável, acrílico, nylon e ganchos. As quantidades desses materiais são restritas e não podem ser ultrapassadas. O objetivo é determinar a quantidade de cada tipo de bijuteria a ser produzida de modo a maximizar o lucro total, considerando os preços de venda de cada tipo.

Portanto, a solução desse problema fornece informações sobre como a loja deve distribuir seus recursos e produzir diferentes tipos de joias e semijóias para obter o máximo retorno financeiro.


---------------------------------------------------------------------------------------------------------------------------------------------------------------------


Este trabalho visa não apenas resolver um problema específico, mas também proporcionar uma compreensão profunda dos conceitos de Pesquisa Operacional e sua aplicação prática.


====> VEJA NOSSO VÍDEO EXPLICANDO DETALHADAMENTE SOBRE O TRABALHO! <=============

LINK: https://www.youtube.com/watch?v=bXeOLFxzXWs&ab_channel=MarcelaAlmeida


