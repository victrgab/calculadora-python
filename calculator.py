import os

def titulo():
    print('Calculadora de números inteiros')
def invalido():
    os.system('cls')
    print('Opção inválida!')

def calculadora():
    titulo()
    while True:
        try:
            numero_1 = int(input('\nInsira um valor: '))
            break
        except:
            invalido()
    while True:
        try:
            operacao = int(input(f'\n1 - Somar {numero_1} com X\n2 - Subtrair {numero_1} por X\n3 - Dividir {numero_1} por X\n4 - Multiplicar {numero_1} com X\nEscolha a operação desejada: '))

            if operacao == 1:
                os.system('cls')
                numero_2 = int(input(f'Insira um valor para somar com {numero_1}: '))
                resultado = numero_1 + numero_2 
                print(f'Resultado: {resultado}')         
            elif operacao == 2:
                os.system('cls')
                numero_2 = int(input(f'Insira um valor para subtrair com {numero_1}: '))
                resultado = numero_1 - numero_2 
                print(f'Resultado: {resultado}')
            
            elif operacao == 3:
                try:
                    os.system('cls')
                    numero_2 = int(input(f'Insira um valor para dividir com {numero_1}: '))
                    resultado = numero_1 / numero_2 
                    print(f'Resultado: {resultado}')
                except:
                    print('Um numero não pode ser dividido por 0')
            elif operacao == 4:
                os.system('cls')
                numero_2 = int(input(f'Insira um valor para multiplicar com {numero_1}: '))
                resultado = numero_1 * numero_2 
                print(f'Resultado: {resultado}')
            else:
                invalido()
        except:
            invalido()
        try:
            escolha = int(input('\n1 - Continuar\n2 - Reiniciar\n3 - Sair\nEscolha uma opção: '))
            if escolha == 1:
                if resultado == True:
                    numero_1 = resultado
            elif escolha == 2:
                titulo()
                numero_1 = int(input('\nInsira um valor: '))
            elif escolha == 3:
                break
            else:
                invalido()
        except:
            invalido()
        
calculadora()