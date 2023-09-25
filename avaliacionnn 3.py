# Questão 03
data = input("Digite uma data no formato Dia/Mes/ano: ")

dia, mes, ano = data.split("/")
dia = int(dia)
mes = int(mes)
ano = int(ano)

texto = input("Digite um texto aí: ")

num_letras = len(texto)
print("O texto possui", num_letras, "letras.")

texto_maiusculo = texto.upper()
palavras = texto_maiusculo.split()

numero_decimal = float(input("Digite um número: "))

numero_decimal_str = str(numero_decimal)
numero_decimal_str = numero_decimal_str.replace(".", ",")

print("Data:", data)
print("Dia:", dia)
print("Mês:", mes)
print("Ano:", ano)
print("Texto:", texto)
print("Número de letras:", num_letras)
print("Texto em maiúsculas:", texto_maiusculo)
print("Lista de palavras:", palavras)
print("Número:", numero_decimal)
print("Número com vírgula:", numero_decimal_str)