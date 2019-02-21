numeros = int(input('Quantos números você deseja ter nessa média?'))
valores = 0

for i in range(0, numeros):
    valores += int(input('Quais são esses valores?')) 

media = (valores)/numeros
print(media)