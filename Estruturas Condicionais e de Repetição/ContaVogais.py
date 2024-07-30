palavra = input('Digite uma palavra: ').lower()

vogais = 'aeiou'

cont = 0

for letra in palavra:
    if letra in vogais:
        cont += 1

        
print(f"O número de vogais na string '{palavra}' é: {cont}")
