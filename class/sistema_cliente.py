class cliente:
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.lista_planos = ['basic', 'premium']
        if plano in self.lista_planos:
            self.plano = plano
        else:
            print('Você não tem acesso a esse conteúdo.')
        
    def up(self, novo_plano):
        if novo_plano in self.lista_planos:
            self.plano = novo_plano
        else:
            raise Exception('Plano invalido!')

    def filme_premium(self, filme, ver_filmes):
        if self.plano == ver_filmes:
            print(f'Você pode assistir ao filme: {filme}')
        elif self.plano == 'premium':
            print(f'Você pode ver o filme {filme}')
        elif self.plano ==  'basic':
            print('Você não tem acesso ao conteúdo do site')
        else:
            raise Exception('Error')

cliente = cliente('shrek', 'shrek@gmail.com', 'basic')
print(cliente.plano)

cliente.filme_premium('harry potter', 'premium')

cliente.up('premium')
print(cliente.plano)
        
cliente.filme_premium('harry potter', 'premium')
