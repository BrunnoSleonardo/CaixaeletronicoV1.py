import time

def  titulo(txt):
    tam = len(txt)
    print('=' * tam)
    print(txt)
    print('=' * tam)


def dinheiro(txt):
    while True:
        try:
            valor = int(input(txt))
        except(TypeError, ValueError):
            print('Cara, isso é um caixa eletrônico. Digite o valor que você quer sacar em números inteiros')
            continue
        except(KeyboardInterrupt):
            print('Sua conta foi deslogada, não se preocupe ;)')
            break
        else:
            return valor

ced200 = 200      #Variaveis:notas, valor_digitado, total_de_notas
ced100 = 100
ced50 = 50
ced20 = 20
ced10 = 10
ced5 = 5
ced1 = 1
valor = 0
totalced200 = 0
totalced100 = 0
totalced50 = 0
totalced20 = 0
totalced10 = 0
totalced5 = 0
totalced1 = 0

titulo('BANCO DO MAMÃO')

print('Olá, seja muito bem vindo(a) ao banco do Mamão!')
time.sleep(1)
print('\ncarregando...')
time.sleep(2)

valor = dinheiro('\nDigite a quantidade que você quer sacar: R$')
total = valor

while True:
    if total >= ced200:
        total -= ced200
        totalced200 = totalced200 + 1
    elif total >= ced100:
        total -= ced100
        totalced100 += 1
    elif total >= ced50:
        total -= ced50
        totalced50 += 1
    elif total >= ced20:
        total -= ced20
        totalced20 += 1
    elif total >= ced10:
        total -= ced10
        totalced10 += 1
    elif total >= ced5:
        total -= ced5
        totalced5 += 1
    elif total >= ced1:
        total -= ced1
        totalced1 += 1
    else:
        break

if totalced200 > 1:
    print(f'{totalced200} notas de R$ {ced200}')
elif totalced200 == 1:
    print(f'Uma nota de R$ {ced200}')

if totalced100 > 1:
    print(f'{totalced100} notas de R$ {ced100}')
elif totalced100 == 1:
    print(f'Uma nota de R$ {ced100}')

if totalced50 > 1:
    print(f'{totalced50} notas de R$ {ced50}')
elif totalced50 == 1:
    print(f'Uma nota de R$ {ced50}')

if totalced20 > 1:
    print(f'{totalced20} notas de R$ {ced20}')
elif totalced20 == 1:
    print(f'Uma nota de R$ {ced20}')

if totalced10 > 1:
    print(f'Uma nota de {ced10}')
elif totalced10 == 1:
    print(f'Uma nota de R$ {ced10}')

if totalced5 > 1:
    print(f'{totalced5} notas de R$ {ced5}')
elif totalced5 == 1:
    print(f'Uma nota de R$ {ced5}')

if totalced1 > 1:
    print(f'{totalced1} notas de R$ {ced1}')
elif totalced1 == 1:
    print(f'Uma nota de R$ {ced1}')

time.sleep(1)

print('\nMuito obrigado por usar o banco do Mamão!')