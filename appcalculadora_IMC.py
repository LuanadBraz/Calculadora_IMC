####################### CALCULADORA IMC #######################
import time

print('-----------------------------------------')
print('------------ CALCULADORA IMC ------------')
print('-----------------------------------------')
nome = input('Digite seu Nome: ')
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / (altura * altura)
print('Calculando...')
time.sleep(1.9) #temporizador


print(nome,'Seu índice de massa corporal é de {:.2f}.'.format(imc))
if imc <= 18.5:
    print('Abaixo do Peso')
elif imc >= 18.5 and imc <= 24.9:
    print('Peso Normal!')
elif imc >= 25 and imc <= 29.9:
    print('Sobrepeso!')
elif imc >= 30 and imc <= 34.9:
    print('Obesidade Grau I!')
elif imc >= 35 and imc <= 39.9:
    print('Obesidade Grau II!')
elif imc >= 40:
    print('Obesidade Grau III ou Mórbida!')
else:
    print('ERROR! Verifique os dados digitados e calcule novamente!')

print('-----------------------------------------')
print('------------ CALCULADORA IMC ------------')
print('-----------------------------------------')