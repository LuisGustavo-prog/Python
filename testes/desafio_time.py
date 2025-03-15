import time

def relogio(valor1, valor2):
    match valor2:
        case 'y':
            for sequencia in range(valor1):
                print(valor1 -sequencia, end='\r', flush=True)
                time.sleep(1)
        case 'n':
            for sequencia in range(valor1):
                print(sequencia, end='\r', flush=True)
                time.sleep(1)
        case _:
            print('Digite uma resposta valida!')



numero_da_contagem = int(input('Digite o número pra contagem: '))
contagem_contraria = str(input('Digite y para uma contagem ao contrária, ou digite n para uma contagem normal: '))
contagem = relogio(numero_da_contagem, contagem_contraria)
print(contagem)
print('sua contagem terminou!')
