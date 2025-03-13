def calculador_de_media(numero_de_notas):
    match numero_de_notas:
        case 2:
            nota1 = int(input('Digite a primeira nota do aluno(a): '))
            nota2 = int(input('Digite a segunda nota do aluno(a): '))
            resultado_das_notas = (nota1 + nota2) / numero_de_notas
            print('O resultado da nota do aluno(a): {:.1f}'.format(resultado_das_notas))
        case 3:
            nota1 = int(input('Digite a primeira nota do aluno(a): '))
            nota2 = int(input('Digite a segunda nota do aluno(a): '))
            nota3 = int(input('Digite a terceira nota do aluno(a): '))
            resultado_das_notas = (nota1 + nota2 + nota3) / numero_de_notas
            print('O resultado da nota do aluno(a): {:.1f}'.format(resultado_das_notas))
        case 4:
            nota1 = int(input('Digite a primeira nota do aluno(a): '))
            nota2 = int(input('Digite a segunda nota do aluno(a): '))
            nota3 = int(input('Digite a terceira nota do aluno(a): '))
            nota4 = int(input('Digite a quarta nota do aluno(a): '))
            resultado_das_notas = (nota1 + nota2 + nota3 + nota4) / numero_de_notas
            print('O resultado da nota do aluno(a): {:.1f}'.format(resultado_das_notas))
        case _:
            print('Digite uma resposta valida!')

nota = int(input('Digite o número de notas do aluno(a): '))
resultado = calculador_de_media(nota)


            
