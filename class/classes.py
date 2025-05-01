class ControleRemoto:
    def __init__(self, valor_da_cor, altura, profundidade, largura):
        self.cor = valor_da_cor
        self.altura = altura
        self.profundidade = profundidade
        self.largura = largura

    def passar_canal(self, botao):
        match botao:
            case '+':
                print('Aumentar canal')
            case '-':
                print('Diminuir o canal')



controle_remoto = ControleRemoto('preto', '10cm', '2cm', '2cm') #Esse controle remoto seria uma estância da classe ControleRemoto pq ele usou essa classe.
print(controle_remoto.cor) 
controle_remoto.passar_canal('-')

controle_remoto2 = ControleRemoto('preto', '14cm', '2cm', '1cm') #Esse outro controle remoto seria uma outra estância da classe ControleRemoto pq ele tmb usou essa classe.
print(controle_remoto2.cor)
controle_remoto2.passar_canal('+')
