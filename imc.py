import sys

peso = float(sys.argv[1])
altura = float(sys.argv[2])

imc = round(peso / (altura/100)**2, 2)

print(f'Su IMC es {imc}')
if imc < 18.5:
    print('La clasificación OMS es BajoPeso')
elif imc < 25:
    print('La clasificación OMS es Adecuado')
elif imc < 30:
    print('La clasificación OMS es Sobrepeso')
elif imc < 35:
    print('La clasificación OMS es Obesidad grado I')
elif imc < 40:
    print('La clasificación OMS es Obesidad grado II')
else:
    print('La clasificación OMS es Obesidad grado III')

