class cliente:
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.lista_plano = ['basic', 'gold']
        if plano in self.lista_plano:
            self.plano = plano
        else:
            print('Error')

    def up(self, novo_plano):
        if self.plano in self.lista_plano:
            self.plano = novo_plano
        else:
            raise Exception('Não foi possível mudar de plano!')
    
    def filme_premium(self, filme, filme_premium):
        if self.plano == filme_premium:
            print(f'Você pode assistir ao filme {filme}')
        elif self.plano == 'gold':
            print(f'você pode assistir o filme {filme}')
        elif self.plano == 'basic' and self.plano == 'premium':
            print('Você não tem acesso ao filme')
        else:
            print('Você não tem acesso ao conteúdo')

    def filme_premium2(self, filme, filme_premium):
        if self.plano == filme_premium:
            print(f'Você pode assistir ao filme {filme}')
        elif self.plano == 'gold':
            print(f'você pode assistir o filme {filme}')
        elif self.plano == 'basic':
            print('Você não tem acesso ao filme')
        else:
            print('Você nã tem acesso ao conteúdo')

cliente = cliente('jason', 'jason@gmail.com', 'basic')
print(cliente.plano)

cliente.filme_premium('Harry potter', 'gold')
cliente.filme_premium2('Harry potter', 'gold')

cliente.up('gold')
print(cliente.plano)

cliente.filme_premium('Harry potter', 'gold')
cliente.filme_premium2('Harry potter', 'gold')
