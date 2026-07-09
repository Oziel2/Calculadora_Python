
import os
import math

def limpar_console():
    # os.name retorna 'nt' se for Windows e 'posix' se for Linux/macOS
    os.system('cls' if os.name == 'nt' else 'clear')


def numero_valido(num):
    if num.replace('.', '', 1).isdigit() or (num.startswith('-') and num[1:].replace('.', '', 1).isdigit()):
        return float(num)
    else:
        print("O input não pode ser diferente de números.")
        exit()


class Calculadora:
    def __init__(self):
        pass

    def soma(self, num1, num2):
        limpar_console()
        print("Soma de", num1, "e", num2)
        return num1 + num2

    def subtracao(self, num1, num2):
        limpar_console()
        print("Subtração de", num1, "e", num2)
        return num1 - num2

    def multiplicacao(self, num1, num2):
        limpar_console()
        print("Multiplicação de", num1, "e", num2)
        return num1 * num2

    def divisao(self, num1, num2):
        limpar_console()
        print("Divisão de", num1, "e", num2)
        return num1 / num2

    def raiz_quadrada(self, num1):
        limpar_console()
        print("Raiz quadrada de", num1)
        return math.sqrt(num1)


calc = Calculadora()  # para chamar a classe
limpar_console()
while True:

    num1 = numero_valido(input("Primeiro número: "))
    num2 = numero_valido(input("Segundo número: "))

    print("Escolha a operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Raiz quadrada")
    print("6. Sair")

    escolha = input("Digite sua escolha (1/2/3/4/5/6): ")

    if escolha == '1':
        resultado = calc.soma(num1, num2)
        print("O resultado é:", resultado)
    elif escolha == '2':
        resultado = calc.subtracao(num1, num2)
        print("O resultado é:", resultado)
    elif escolha == '3':
        resultado = calc.multiplicacao(num1, num2)
        print("O resultado é:", resultado)
    elif escolha == '4':
        if num2 != 0:
            resultado = calc.divisao(num1, num2)
            print("O resultado é:", resultado)
        else:
            print("Erro: Divisão por zero não é permitida.")
    elif escolha == '5':
        if num1 < 0:
            print("Erro: não é possível calcular raiz quadrada de número negativo.")
        else:
            resultado = calc.raiz_quadrada(num1)
            print("O resultado é:", resultado)
    elif escolha == '6':
        print("Saindo...")
        limpar_console()
        break
    else:
        print("Escolha inválida. Tente novamente!!")

      