def calculation(a, b):
    result_note = (a + b) / 2
    
    if result_note <= 5.0:
        return 'O aluno(a) está reprovado.'
    elif result_note > 5.0 and result_note < 6.9:
        return 'O aluno(a) está de recuperação.'
    else:
        return 'O aluno está aprovado, parabéns!'

note_1 = 5
note_2 = 7.5

result = print(calculation(note_1, note_2))

