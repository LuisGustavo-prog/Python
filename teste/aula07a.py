nome = input('Digite seu nome: ')
# print('Prazer em te conhecer, {:20}!' .format(nome)) Faz a variável nome aparecer em 20 caracteres mesmo não tendo essa quantidade, ele cria como se fosse um espaço.
# print('Prazer em te conhecer, {:<20}!' .format(nome))  Faz a variável nome ficar 20 casas pra direita, o número de casa é de acordo com a quantidade colocada dentro das chaves.
# print('Prazer em te conhecer, {:>20}!' .format(nome))  Faz a variável nome ficar 20 casas pra esquerda, o número de casa é de acordo com a quantidade colocada dentro das chaves.
# print('Prazer em te conhecer, {:^20}!' .format(nome)) Faz a variável nome ficar no meio das 20 caracteres, o número de caracteres é de acordo com a quantidade colocada dentro das chaves.
# print('Prazer em te conhecer, {:^20}!' .format(nome)) Para poder fazer esse comandos é necessario colocar dentro das chaves ":" sem isso o comando não funcionara.
print('Prazer em te conhecer, {:^20}!' .format(nome))
