class cinema:
    def __init__(self, nome, email, plano, valor):
        self.nome = nome
        self.email = email
        self.plano_preço = {'basic': 'R$32,99', 'gold': 'R$59,99'}
        if plano in self.plano_preço:
            self.plano = plano
            self.valor = self.plano_preço[plano]
        else:
            raise Exception('Error502')
        if valor == self.valor:
            self.valor = valor
        else:
            raise Exception('Error503')
        
    def up(self, novo_plano):
        if novo_plano in self.plano_preço:
            self.plano = novo_plano
            self.valor = self.plano_preço[novo_plano]
        else:
            raise Exception('Error504')
    
    def sala1(self, filme):
        if self.plano == 'gold':
            print(f'Acesso liberado ao filme {filme}')
        elif self.plano == 'basic':
            print('Faça um upgrade para acessar essa sala')
        else:
            raise Exception('Error505')

    def sala_1(self, filme):
        if self.plano == 'gold':
            print('Olá, seu plano corresponde ao gold, sugiro você ir para uma sala gold.')
        elif self.plano == 'basic':
            print(f'Acesso a sala liberado {filme}')
        else:
            raise Exception('Erro506')
        
    
            
        

cinema = cinema('jinx', 'jinx@gmail.com', 'basic', 'R$32,99')
print(cinema.nome)   
print(cinema.email)   
print(cinema.plano)    
print(cinema.valor)

cinema.sala1('harry potter')
cinema.sala_1('Harry potter')

cinema.up('gold')
print(cinema.nome)   
print(cinema.email)   
print(cinema.plano)    
print(cinema.valor)  

cinema.sala1('harry potter')
cinema.sala_1('Harry potter')

