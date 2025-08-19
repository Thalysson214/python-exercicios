def soma(a, b): return a + b
def subtracao(a, b): return a - b
def multiplicacao(a, b): return a * b
def divisao(a, b): return a / b if b != 0 else "Erro: divisão por zero"

print("Calculadora Simples")
print("1. Soma\n2. Subtração\n3. Multiplicação\n4. Divisão")
opcao = int(input("Escolha a operação: "))

x = float(input("Digite o primeiro número: "))
y = float(input("Digite o segundo número: "))

if opcao == 1:
    print("Resultado:", soma(x, y))
elif opcao == 2:
    print("Resultado:", subtracao(x, y))
elif opcao == 3:
    print("Resultado:", multiplicacao(x, y))
elif opcao == 4:
    print("Resultado:", divisao(x, y))
else:
    print("Opção inválida.")
