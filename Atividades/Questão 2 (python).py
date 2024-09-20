valor1 = int(0)
valor2 = int(1)
valor3 = int
numEscolha = int(input("Digite um número para saber se ele pertence à sequência de Fibonacci: \n"))

while numEscolha != valor3:
    valor3 = valor1 + valor2
    valor1 = valor2
    valor2 = valor3
    if numEscolha < valor3:
        print(numEscolha, "não pertence à sequência de Fibonacci")
        break

if numEscolha == valor3:
    print(numEscolha, "pertence à sequência de Fibonacci")