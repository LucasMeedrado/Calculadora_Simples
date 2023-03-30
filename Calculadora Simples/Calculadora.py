# Função para adição
def add(x, y):
   return x + y

# Função para subtração
def subtract(x, y):
   return x - y

# Função para multiplicação
def multiply(x, y):
   return x * y

# Função para divisão
def divide(x, y):
   return x / y

# Menu da calculadora
print("Selecione a operação:")
print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

# Recebe a entrada do usuário
op = input("Digite sua escolha (1/2/3/4): ")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Executa a operação selecionada
if op == '1':
   print(num1,"+",num2,"=", add(num1,num2))

elif op == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))

elif op == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))

elif op == '4':
   print(num1,"/",num2,"=", divide(num1,num2))

else:
   print("Opção inválida.")
