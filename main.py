# imports as bibliotecas
import os
import time

# usuário informe um número
contador = int(input('Informe um número inteiro'))
os.system('cls')

# conta a partir os números informado até 0

while contador >= 0:
    print(f'Contagem regressiva: {contador}...')
    time.sleep(1)
    os.system('cls')
    contador -= 1
print('BOOM!!!')