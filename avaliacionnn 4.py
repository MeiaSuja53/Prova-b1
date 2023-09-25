# Questão 04 

import math
base = float(input("Digite o valor da base do triângulo: "))
altura = float(input("Digite o valor da altura do triângulo: "))

aranha = (base * altura) / 2
perimetro = base + altura + math.sqrt(base**2 + altura**2)

print("A área do triângulo é", aranha, "e o perímetro é", perimetro)