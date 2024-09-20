import json
import random

menorValor = float
maiorValor = float
media = float
faturamento = [round(random.uniform(0,10000), 2) for _ in range(21)] #21 dias úteis quando se tira os finais de semana de um mês

dados = {
    "dados": faturamento
}

with open('dados.json', 'w') as arquivo:
    json.dump(dados, arquivo, indent=1)


with open('dados.json', 'r') as arquivo:
    dados = json.load(arquivo)

faturamento = dados['dados']

media = sum(faturamento)
media = round(media / 21, 2)
menorValor = min(faturamento)
maiorValor = max(faturamento)

print("O menor faturamento do mês foi:", menorValor)
print("O maior faturamento do mês foi:", maiorValor)

quantDias = sum(1 for num in faturamento if num > media)

print("média do mês:", media)
print("em", quantDias, "dias o faturamento diário foi maior que a média do mês")