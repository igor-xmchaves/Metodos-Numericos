# Metodos-Numericos
 Trabalho de Cálculo Numérico
 Tema2: Ciência de Dados, Engenharia de Produção e Computação
A indústria de alimentos está constantemente em busca de otimizações em seus processos para garantir seus
ganhos e a qualidade de seus produtos. Uma empresa da área deseja determinar a quantidade ideal de
ingredientes para utilizar em um novo produto, de modo a maximizar a lucratividade. Seja o custo de
produção regido pela função f(Q) = C*e^Q – 4*Q^2, onde C é o valor de custo dos ingredientes (em bilhão) dado
conforme a escolha do fornecedor e Q é a respectiva quantidade de ingredientes comprada para o produto
considerado onde Q varia conforme o valor de C. Caso essa quantidade Q de ingredientes passe de 0,7 (em
TONELADAS) a quantidade de ingredientes se torna inviável, causando um problema grave por falta de
espaço para alocação da produção e sérios prejuízos financeiros.
O método de Newton modificado é tal que a função de iteração (x) é dada por (x) = x – (f(x) / f’(xo)), onde
xo é uma aproximação inicial e é tal que o denominador f ’(xo)  0, evitando assim uma indeterminação.
Desenvolva um sistema para calcular o valor do deslocamento d que deve atender a todos requisitos abaixo:
a) Implementar algoritmo para calcular Q pelo método do Ponto Fixo com um Φ que converge.
b) Implementar algoritmo para calcular Q pelo método de Newton modificado.
c) Implementar algoritmo para calcular Q pelo método da Secante original.
d) Testar os resultados para d usando como padrão C = 1, Q0 = 0,5 e  = 10-4.
e) Fornecer um quadro resposta, com Q calculado para cada método dado (comparando resposta, acurácia
(erro), tempo, número de iterações etc).
f) Fornecer um quadro comparativo, com todos os dados para cada método (comparando resposta, acurácia
(erro), tempo, número de iterações etc).
g) Analisar o efeito da variação do valor de C (diferentes fornecedores) para cada método considerado
(comparando resposta, acurácia (erro), tempo, número de iterações etc).
Dados de entrada: n (número de valores de C), C (para cada n) e  (precisão).
Dados de saída: quadros resposta (com Q e erro para cada C e método) e comparativo.
*Em todos os itens e resultados mostre se a empresa terá ou não falta de espaço e prejuízo financeiro
