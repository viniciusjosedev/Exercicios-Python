'''login = input ("Digite o seu Login: ")
senha = input ("Digite sua Senha: ")

print ("Seu Login é: %s, e sua senha é: %s" %(login, senha))
'''

'''num1 = float (input ("Digite o Pimeiro Valor: "))
num2 = float (input ("Digite o Segundo Valor: "))
divisao = num1 / num2
resto = num1 % num2

print ()

print ("O resultado da Divisão entre o %s, e %s foi: %s " %(num1, num2, divisao))
print ("E a sobra foi exatos: ", resto)'''

'''print ("Calculadora de Bhaskara")

print ()

a = float (input("Digite o Valor 'a' da Questão: "))
b = float (input("Digite o Valor 'b' da Questão: "))
c = float (input("Digite o Valor 'c' da Questão: "))
delta = (b**2-4*a*c)
delta1 = (delta ** (1/2))
x1 = (-b + delta1) / (2*a)
x2 = (-b - delta1)/ (2*a)

if (delta < 0 ):
    print ("O valor de Delta é Negativo, Portanto, Não é Possivel caucular a Raiz do Mesmo, A conta Para Por Aqui.")
    print ()
    print ("O resultado do Delta Foi: %s" %delta)

else:
    if (delta > 0):
        print("O resultado do Delta Foi: %s, Tirando-o da Raiz: %s" % (delta, delta1))
        print("O resultado Do x1 e x2 foi, respectivamente: %s, %s" % (x1, x2))'''

'''idade = int(input("Informe a sua idade: "))
print()
2
if (idade<=0):
    print ("VocÊ é tão novo que nem nasceu ainda hein")

elif (idade >= 150):
    print ("Tá velho hein, como era viver com os dinossauros?")

elif (idade < 18):
    print("Desculpe, mas você nao pode entrar aqui por ser menor de idade.")

else:
    print ("Entrada Permitida.")'''

'''num1 = input("Digite um Valor: ")
num1 = int (num1)
if (type(num1) == int):
    print("O valor Digitado é do tipo int.")
else:
    print("O valor digitado não é do tipo int.")'''

'''print ("-----CALCULADORA-----")

print ()

num1 = float(input("Digite o 1ª Numero (com excessão do zero): "))
num2 = float(input("Digite o 2ª Numero (com excessão do zero): "))
op = str(input("Digite a Operação, Lembrando que a mesma são as seguintes; '+' = soma, '-' = subtração, '*' = multiplicação, '/' = divisão e '**' = potenciação. Escolha a Desejada:  "))
numsoma= (num1 + num2)
numsubtracao = (num1 - num2)
nummultiplicacao = (num1 * num2)
numdivisao = (num1 / num2)
numpotenciacao = (num1 ** num2)

while num1 and num2 != 0:
    if (op == '+'):
        print ("A soma entre o 1ª e o 2ª Número foi: ", numsoma)
    elif (op == '-'):
        print ("A Subtração entre o 1ª e o 2ª Número foi: ", numsubtracao)
    elif (op == '*'):
        print ("A Multiplicação entre o 1ª e o 2ª numero foi: ", nummultiplicacao)
    elif (op == '/'):
        print ("A Divisão entre o 1ª e o 2ª Número foi: ", numdivisao)
    elif (op == '**'):
        print ("A Potencia do 1ª valor elevado ao 2ª foi: ", numpotenciacao)
    else:
        print ("'ERRO', Verifique o Símbolo da Sua Operação e tente Novamente")

    print()

    num1 = float(input("Digite o 1ª Numero (com excessão do zero): "))
    num2 = float(input("Digite o 2ª Numero (com excessão do zero): "))
    op = str(input(
        "Digite a Operação, Lembrando que a mesma são as seguintes; '+' = soma, '-' = subtração, '*' = multiplicação, '/' = divisão e '**' = potenciação. Escolha a Desejada:  "))
    numsoma = (num1 + num2)
    numsubtracao = (num1 - num2)
    nummultiplicacao = (num1 * num2)
    numdivisao = (num1 / num2)
    numpotenciacao = (num1 ** num2)'''


'''num1 = int(input("Digite um Numero e veja se ele é par ou Impar: "))
while (num1 % 2 == 0):
    print ("Par")
    print()
    num1 = int(input("Digite um Numero e veja se ele é par ou Impar: "))
while (num1 % 2 != 0 ):
    print("Impar")
    print ()
    num1 = int(input("Digite um Numero e veja se ele é par ou Impar: "))'''


'''a = 1
while (a <= 10):
    print (a)
    a += 1
else:
        print("A é maior que 10")'''

'''a = 10
for a in "10":
    print (a, end="")'''

'''uc = int(input("Deseja fazer a contagem a partir de qual numero?: "))
uc2 = int(input("Qual o valor maximo?: "))
uc3 = int(input("Quantos passos?: "))
for c in range ((uc), uc2+1, uc3):
    print (c)'''

'''for a in range (10):
    print (a)
    if (a == 6):
        break'''

'''print ("----TELA DE LOGIN----")
print ()

login = str(input("Digite o seu Login: "):
senha = str(input("Digite sua Senha: "))

while (login):
    print ("")'''

'''num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro npumero: "))
if (num1 + num2 == 10):
    print ("O resultado é igual a 10")
elif (num1 + num2 != 10):
    print ("O resultado é diferente de 10")
elif (num1 + num2 > 10):
    print ("O resultado é maior que 10")
elif (num1 + num2 < 10):
    print ("O resultado é menor que 10")
elif (num1 + num2 >= 10):
    print ("O resultado é maior ou igual a 10")
elif (num1 + num2 <= 10):
    print ("O resultado é menor ou igual a 10")'''


'''a = 0
while (a < 20):
    print (a)
    a += 1
    if (a == 10 + 1):
        break'''

'''for a in range(20):
    print (a)
    if (a == 10):
        break'''


'''lista = [100,200,300,400]
for a in lista:
    a += 1000
    print (a)'''

'''nome = input("Digite seu nome: ")
a = nome[::-1]
print(a)'''


'''b = 10
while (b == 10):
    f = int(input("Digite o a quantidade de faces: "))
    v = int(input("Digite a auantidade de vertices: "))
    a = int(input("Digite a quantidade de arestas: "))
    if (f == 0 and v == 0 and a == 0):
        print ("Nada de Palhaçadas!")
        continue
    elif (f == 0 and v > 0 and a > 0):
        print ("O valor das faces é: ", (a + 2 - v))
        continue
    elif(f > 0 and v == 0 and a > 0):
        print ("O valor das Vertices é: ", (a + 2 - f))
        continue
    elif (f > 0 and a == 0 and v > 0):
        print ("O valor das arestas é: ", f / 2)
        continue
    elif (f > 0):
        print ("O valor da Vertice e da aresta é, respectivamente: ", (f/2) + 2 -f)
print(range(50))'''

NUMEROS = 20
inteiros = []
pares = []
impares = []

for i in range(NUMEROS):
    numero = int(input("Digite um inteiro: "))
    inteiros.append(numero)
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)


print("\nInteiros")
for numero in inteiros:
    print(f"{numero}", end=" ")

print("\nPares")
for numero in pares:
    print(f"{numero}", end=" ")

print("\nImpares")
for numero in impares:
    print(f"{numero}", end=" ")
