# #  Calculo matemático que eu usei pra responder a pergunta da minha faculdade kkkkk

def calculo_matematico(valor1, valor2):
    fator_de_velocidade = (valor1 * valor2 / 100)

    return fator_de_velocidade

capacidade_de_produção = int(input('Digite o número de capacidade de produção: '))
fator_de_foco = int(input('Digite o número de fator de foco: '))
fator_de_velocidade = calculo_matematico(capacidade_de_produção, fator_de_foco)
print(fator_de_velocidade)