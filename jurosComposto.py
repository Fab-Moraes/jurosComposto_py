def calcular_valor_final_investimento(valor_inicial, taxa_juros, periodo):
    # Converte a taxa de juros anual para uma taxa de juros periódica
    taxa_periodica = 1 + taxa_juros
    # Calcula o valor final com juros compostos
    valor_final = valor_inicial * (taxa_periodica ** periodo)
    return round(valor_final, 2)

# Obtenha os valores de entrada
valor_inicial = float(input())
taxa_juros = float(input())
periodo = int(input())

# Chame a função para calcular o valor final do investimento
valor_final = calcular_valor_final_investimento(valor_inicial, taxa_juros, periodo)

# Imprima o resultado
print("Valor final do investimento: R$", valor_final)
