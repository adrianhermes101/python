def adicao(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def multiplicacao(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    if num2 == 0:
        return "Não é possível dividir por zero!"
    else:
        return num1 / num2

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

operacao = input("Escolha a operação desejada (+ para soma, - para subtração, * para multiplicação, / para divisão): ")

if operacao == '+':
    resultado = adicao(num1, num2)
elif operacao == '-':
    resultado = subtracao(num1, num2)
elif operacao == '*':
    resultado = multiplicacao(num1, num2)
elif operacao == '/':
    resultado = divisao(num1, num2)
else:
    resultado = "Operação inválida!"

print(resultado)

