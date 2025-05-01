class cliente:
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.lista_planos = ['basic', 'premium'] #valor fixo, por isso não foi colocado no init
        if plano in self.lista_planos:
            self.plano = plano
        else:
            raise Exception('plano invalido')
        
    def mudar_plano(self, novo_plano):
        if novo_plano in self.lista_planos:
            self.plano = novo_plano
        else:
            print('Plano invalido  ')
    
    def ver_filmes(self, filme, plano_filme):
        if self.plano == plano_filme:
            print(f'Você pode ver o filme {filme}')
        elif self.plano == 'premium':
            print(f'Você pode ver o filme {filme}')
        elif self.plano == 'basic' and plano_filme == 'premium':
            print('faça um apgrade para ver esse filme!')
        else:
            print('Plano inválido')
            

            

cliente = cliente('shrek', 'shrek@gmail.com', 'basic')
print(cliente.plano) #cliente antigo

cliente.ver_filmes('Harry potter', 'premium')

# mudando o plano 
cliente.mudar_plano('premium') #Mudando o plano do cliente
print(cliente.plano)

cliente.ver_filmes('Harry potter', 'premium')
