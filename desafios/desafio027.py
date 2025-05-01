frase = str(input('Digite uma frase: ')).strip()
munu = frase.lower()

a = munu.count('a')
palavra =  'python'

print(munu.find(palavra))
print(munu.find(palavra[-1]))
print(a)