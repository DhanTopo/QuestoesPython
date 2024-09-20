
estados = {
    "SP" : (67836.43),
    "RJ" : (36678.66),
    "MG" : (29229.88),
    "ES" : (27165.48),
    "outros" : (19849.53)
}


total_mensal = sum(estados.values())


percentuais = {estado: (valor / total_mensal) * 100 for estado, valor in estados.items()}


print(f"Total Mensal: R${total_mensal:.2f}")
print("Percentuais de Representação:")
for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")