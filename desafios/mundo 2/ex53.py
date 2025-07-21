def game(a):
    import random

    lists = ['pedra', 'papel', 'tesoura']
    choice = random.choice(lists)
    
    if a.lower() == 'pedra':
        if choice == 'tesoura':
            return 'Você ganhou'
        elif choice == 'papel':
            return 'Você perdeu'
        else:
            return 'Empate'
    elif a.lower() == 'papel':
        if choice == 'pedra':
            return 'Você ganhou'
        elif choice == 'tesoura':
            return 'Você perdeu'
        else:
            return 'Empate'
    elif a.lower() == 'tesoura':
        if choice == 'papel':
            return 'Você ganhou'
        elif choice == 'pedra':
            return 'Você perdeu'
        else:
            return 'Empate'
    else:
        return 'Resposta inválida'
        
print(game('pedra'))