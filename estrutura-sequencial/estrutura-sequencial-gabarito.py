#TODOS OS GABARITOS DA ESTRUTURA SEQUENCIAL DO https://wiki.python.org.br/EstruturaSequencial !

#1ª Exercício
'''print("Olá Mundo")'''

#2ª Exercício
'''num = int(input("Digite um Número: "))
print ("O Número Foi: %s" %num)'''

#3ª Exercício
'''num1 = int(input("Digite o 1ª Número: "))
num2 = int(input("Digite o 2ª Número: "))
print ("A Soma dos Dois Números foi: %s" %(num1 + num2))'''

#4ª Exercício
'''print ("----CAUCULADORA DE MEDIAS----")
media1 = float(input("Digite a 1ª Nota: "))
media2 = float(input("Digite a 2ª Nota: "))
media3 = float(input("Digite a 3ª Nota: "))
media4 = float(input("Digite a 4ª Nota: "))
print ()
print("A sua Média Foi: %f" %float(((media1 + media2 + media3 + media4)/4)))'''

#5ª Exercício
'''print ("----Conversor de Metros para Centimetros----")
print ()
metros = float(input("Digite o Valor em Metros: "))
print ()
print ("O Valor em Cm é: %.1f" %float(metros*100))'''

#6ª Exercício
'''print ("Calculadora de áreas Circulares")
print ()
raio = float(input("Digite o Raio da Circuferência: "))
print()
print ("A área da Circuferência é(elevado ao quadrado): %.2f" %((raio**2)*3.14))'''

#7ª Exercício
'''print ("Calculadora de Áreas Quadradas Perfeitas")
print()
area = float(input("Digite o Valor da Medida do Quadrado: "))
print()
print ("O resultado da área é: %.2f" %(area**2))'''

#8ª Exercício
'''print ("----CALCULADORA DE RENDA MENSAL")
print()
recebo = float(input("Quanto Você Ganha Por Hora?: "))
hora = float(input("Quanto Horas de Trabalho Por Mês: "))
print()
print ("Seu Salário Mensal é de : %.2f" %(recebo*hora))'''

#9ª Exercicio
'''print ("----CONVERSOR DE FARENHEIT----")
print ()
farenheit = float(input("Digite um Valor em Farenheit: "))
print("O Valor em Graus é: %.2f" %(5*(farenheit-32)/9))'''

#10 Exercício
'''print ("----CONVERSOR DE GRAUS----")
print ()
graus = float(input("Digite um Valor em Graus: "))
print("O Valor em Farenheit é: %s" %((graus*1.8)+32))'''

#11 Exercício
'''print ("----SOMA----")
num1 = float(input("Digite um Número Inteiro: "))
num2 = float(input("Digite Outro Número Inteiro: "))
num3 = float(input("Digite um Número Real: "))
print()
print ("O Produto do Dobro do Primeiro com a Metade do Segundo é: %.2f" %((num1*2)+(num2/2)))
print()
print ("A Soma do Triplo do Primeiro com o Terceiro: %.2f" %(num1 * 3 + num3 * 3))
print()
print ("O Terceiro Elevado ao Cubo: %.2f" %(num3**3))'''

#12 e #13 Exercício
'''print ("----CAUCULADORA DE PESO IDEAL----")
altura = float(input("Digite a Sua Altura: "))
sexo = input("Você é Homem ou Mulher: ")
print ()
while (sexo == ("homem")):
    print ("(Você é Homem) Seu Peso Ideal é: %.2f" %((72.7*altura) - 58))
    altura = float(input("Digite a Sua Altura: "))
    sexo = str(input("Você é Homem ou Mulher: "))
    print()
while (sexo == ("mulher")):
    print ("(Você é Mulher) Seu Peso Ideal é: %.2f" %((62.1*altura) - 44.7))
    altura = float(input("Digite a Sua Altura: "))
    sexo = str(input("Você é Homem ou Mulher: "))
    print()'''

#14 Exercício
'''peso = float(input("Digite o Peso Total da Sua Pesca (Em Quilos): "))
excesso = peso - 50
multa = excesso * 4
print ()
print ("O Peso da Pesca Foi: ", peso)
print ("O Excesso da Pesca foi: ", excesso)
print ("E a Multa Foi: ", multa)'''

#15 Exercício
'''area = float(input("Digite a o Tamanho em Metros² da área que deseja ser pintada: "))
tintas = area/3
while (tintas <= 18):
    print ("Para este Espaço a necessida de litros de tinta é: %s, e o preço total é: R$18,00" %tintas)
    break
else:
    print ("Para este espaço a necessidade de litros de tinta é: %s, e o preço é acima de R$18,00" %tintas)'''

#16 Exercício
'''arquivo = float(input("Digite o Tamanho do Arquivo em MB: "))
conexao = float(input("Digite a Velocidade da Sua Internet: "))
print ()
print ("O tempo Aproximado Para o Termino deste Download é aproximadamente de: ", (arquivo/(conexao/0.125)))'''

#====Exercícios Práticos 2 - Tomada de Decisão====
'''num = float(input("Digite um Número: "))
if (num > 0):
    print ("O número é positivo")
elif (num < 0):
    print ("O número é negativo")
elif (num == 0):
    print ("O numero é igual a 0, ou seja, é neutro")
else:
    print ("Digite um valor númerico válido")'''

#2 Exercício
'''num = int(input("Digite um Número (de preferencia inteiro): "))
if (num % 2 == 0):
    print ("O número é par")
elif (num % 2 != 0):
    print ("O númeor é impar")'''

#3 Exercício
'''num1 = str(input("Digite um Número: "))
num2 = str(input("Digite outro Número: "))
if (num1 > num2):
    print (num1)
elif (num1 < num2):
    print (num2)
elif (num1 == num2):
    print ("Os valores são iguais!")
else:
    print ("Digite um valor válido!")'''

#4 Exercício
'''num = int(input("Digite um Número: "))
if (num >= 18):
    print ("Você é maior de idade")
elif (num < 18):
    print ("Você é menor de idade")'''

#5 Exercício
'''iu = int(input("Digite a sua idade: "))
im = int(input("Digite a idade da sua mãe:  "))
print ("A sua mãe lhe teve aos ", im - iu)'''

#6 Exercício
'''print ("-")
print ("-")
print ("-")
print ("-")
print ("-")
print ("-")
print ("-")
print ("-")
print ("-")
print ("-")
print ("-")
print ("-")
print ("-")
print ("-")
print ("-")
print ("-")
print ("-")
print ("-")
print ("-")
print ("-")
print ("-")
print ("-")
print ("-")
print ("-")
print ("-")
print ("-")
print ("-")
print ("-")
print ("-")
print ("-")
print ("-")
print ("-")
print ("-")
print ("-")
print ("-")
print ("-")
print ("-")
print ("-")
print ("-")
print ("-")
print ("-")
print ("-")
print ("-")
print ("-")
print ("-")
print ("-")
print ("-")
print ("-")
print ("-")
print ("-")
print ("-")'''

#7 Exercício

#8 Exercício
'''num1 = int(input("Digite um número: "))
num2 = int(input("Digite um segundo número: "))
if (num1 > num2):
    print (num1)
    print (num2)
else:
    print (num2)
    print (num1)'''

#9 Exercício
'''num = float(input("Digite um número: "))
if (num == int(num)):
    print ("O número é inteiro")
else:
    print ("O número não é inteiro")'''

'''#10 Exercício
num = str(input("Digite um valor: "))
if not num.isdigit():
    print ("O valor é uma string")
else:
    print ("O valor não é uma string")'''

#18 Exercício
'''dia = int(input("Digite o o dia: "))
mes = int(input("Digite o o mes: "))
ano = int(input("Digite o ano: "))
if (dia <= 00 or dia > 31 or mes <= 00 or mes > 12 or ano < 00):
    print ("Data inválida")
elif (dia > 00 and mes > 00 and ano > 00):
    print ("Data Válida")'''

#19 Exercício
'''mes = str(input("Digite um numero para saber o mês: "))
if (mes == '1'):
    print ("Janeiro")
elif (mes == '2'):
    print ("Fevereiro")
elif (mes == '3'):
    print ("Março")
elif (mes == '4'):
    print ("Abril")
elif (mes == '5'):
    print ("Maio")
elif (mes == '6'):
    print ("Junho")
elif (mes == '7'):
    print ("Julho")
elif (mes == '8'):
    print ("Agosto")
elif (mes == '9'):
    print ("Setembro")
elif (mes == '10'):
    print ("Outubro")
elif (mes == '11'):
    print ("Novembro")
elif (mes == '12'):
    print ("Dezembro")
else:
    print ("Digite um Número Válido!")'''

#20 Exercício
'''tipo = input("Digite o tipo da carne: ")
qt = int(input("Digite a quandidade de carne (em KG): "))
fp = input ("Digite a a forma de pagamento: ")
if (tipo == "file duplo" or tipo == "filé duplo" or tipo == "File duplo" or tipo == "File Duplo" or tipo == "Filé duplo" or tipo == "Filé Duplo" or tipo == "file Duplo" or tipo == "filé Duplo" and qt <= 5 and fp == "cartao tabajara" or fp == "Cartao tabajara" or fp == "Cartao Tabajara" or fp == "cartão tabajara" or fp == "Cartão tabajara" or fp == "cartão Tabajara" or fp == "Cartão Tabajara"):
    print ("====CUPOM FISCAL====")
    print ("Tipo de Carne: Filé Duplo")
    print ("Quantidade de carne: ", qt)
    print ("Forma de Pagamento: Cartão Tabajara")
    print ("Preço Total : ", qt * 4.90)
    print ("Desconto: ", (qt * 4.90 * 5) / 100)
    print ("Preço Final: ", (qt * 4.90 - ((qt * 4.90 * 5) / 100)))

elif (tipo == "file duplo" or tipo == "filé duplo" and qt <= 5 and fp == "Avista" or fp == "cartao tabajara"):'''

#Lista de Exercícios 3 - Iteradores
#1 Exercicio

'''b = 0
while(b==10):
    nota = int(input("Digite um uma nota (entre 0 á 10): "))
    if(nota < 0 or nota > 10):
        print("Informe um valor válido")
        continue
    else:
        print("Valor válido.")
        break'''

#2 Exercício
'''b = 0
while(b==0):
    usuario = input("Digite um nome de usuário: ")
    senha = input("Digite uma senha: ")
    if(usuario == senha):
        print("A senha não pode ser a mesma que o usuario!")
        print("Informe novamente os dados.")
        continue
    else:
        print("Cadastro realizado com sucesso.")
        break'''

#3 Exercício
'''b = 0
n = 'aaa'
while(b == 0):
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    salario = float(input("Digite seu salário: "))
    sexo = input("Digite seu sexo, 'F' para feminino e 'M' para masculino: ")
    estadocv = input("Digite seu estado civil: ")
    if(len(nome) > len(n) and idade > 0 and idade <= 150 and salario > 0 and sexo == 'f' or sexo == 'm' and estadocv == 's' or estadocv ==  'd' or estadocv == 'c' or estadocv ==  'v'):
        print("Dados Válidos")
        break
    else:
        print("Dados Invalidos")'''

#4 Exercício
'''c = 0
d = 0
a = 80000
b = 200000
while(d==0):
    a += (a*3)/100
    b += (b*1.5)/100
    c += 1
    if(a>=b):
        print("Eles se Igualam ou A ultrapassa B no exato ano: %s" %c)
        break'''

#5 Exercício
'''d = 0
v = 0
while(v==0):
    ano = 0
    num1 = float(input("Digite o valor da primeira população(menor): "))
    numcres = float(input("Digite a taxa de crescimento da primeira população: "))
    num2 = float(input("Digite o valor da segunda população(maior): "))
    numcres2 = float(input("Digite o valor da taxa de crescimento da segunda população: "))
    while(d==0):
        num1 += (num1*numcres)/100
        num2 += (num2*numcres2)/100
        ano += 1
        if(num1>=num2):
            print("Eles se Igualam ou A ultrapassa B no exato ano: %s" %ano)
            break'''

#6 Exercício
'''for a in range(21):
    print(a)'''

#6.2 Exercício
'''for a in range(21):
    print(a, end='\t')'''

#7
'''a=0
while(a==0):
    num1=float(input("Digite o primeiro numero: "))
    num2=float(input("Digite o segundo numero: "))
    num3=float(input("Digite o terceiro numero: "))
    num4=float(input("Digite o quarto numero: "))
    num5=float(input("Digite o quinto numero: "))
    if(num1 > num2 and num1 > num3 and num1 > num4 and num1> num5):
        print("O primeiro número é o maior: %s" %num1)
        continue
    if(num2 > num1 and num2 > num3 and num2 > num4 and num2 > num5):
        print("O segundo número é o maior: %s" %num2)
        continue
    if(num3>num1 and num3>num2 and num3>num4 and num3>num5):
        print("O terceiro número é o maior: %s" %num3)
        continue
    if(num4>num1 and num4>num2 and num4>num3 and num4>num5):
        print("O quarto número é o maior: %s" %num4)
        continue
    if(num5>num1 and num5>num2 and num5>num3 and num5>num4):
        print("O quinto número é o maior: %s" %num5)
        continue'''

#8
'''a=0
while(a==0):
    num1=float(input("Digite o primeiro numero: "))
    num2=float(input("Digite o segundo numero: "))
    num3=float(input("Digite o terceiro numero: "))
    num4=float(input("Digite o quarto numero: "))
    num5=float(input("Digite o quinto numero: "))
    print("A soma dos 5 primeiros números é: %s" %(num1+num2+num3+num4+num5))
    print("A média dos 5 primeiros números é: %s" %((num1+num2+num3+num4+num5)/4))
    continue'''

#9
'''for a in range(1, 51):
    if(a % 2  == 0):
        continue
    if(a % 2 != 0):
        print(a)'''

#10
'''a = 0
while(a==0):
    num1 = int(input("Digite um Número: "))
    num2 = int(input("Digite o segundo número: "))
    if(num1<num2):
        for b in range(num1, num2+1):
            print(b)
            continue
    if(num1>num2):
        for b in range(num1, num2-1, -1):
            print(b)
            continue'''

#11
'''a = 0
while(a==0):
    num1 = int(input("Digite um Número: "))
    num2 = int(input("Digite o segundo número: "))
    soma = 0
    if(num1<num2):
        for b in range(num1, num2+1):
            soma += b
            print("Sequência: %s" %b)
            print("A soma dos números é: %s" %soma)
            continue
    if(num1>num2):
        for b in range(num1, num2-1, -1):
            soma += b
            print("Sequência: %s" %b)
            print("A soma dos números é: %s" %soma)
            continue'''

#12
'''a = 0
while(a==0):
    tabuada = int(input("Digite qualquer número inteiro para ver a tabuada de 10 do mesmo: "))
    if(type(tabuada) == type(a)):
        print("Tabuada de %s: " %tabuada)
        for b in range(1,11):
            print("%s x %s = %s" %(tabuada, b,(tabuada*b)))'''

#13
'''a = 0
while(a==0):
    num1 = float(input("Digite um número: "))
    num2 = float(input("Digite o segundo número: "))
    print("O primeiro número elevado ao segundo é: %s" %(num2 ** num1))'''

#14
'''a = 0
while(a==0):
    cnp = 0
    cni = 0
    num1 = int(input("Digite o 1ª número: "))
    num2 = int(input("Digite o 2ª número: "))
    num3 = int(input("Digite o 3ª número: "))
    num4 = int(input("Digite o 4ª número: "))
    num5 = int(input("Digite o 5ª número: "))
    num6 = int(input("Digite o 6ª número: "))
    num7 = int(input("Digite o 7ª número: "))
    num8 = int(input("Digite o 8ª número: "))
    num9 = int(input("Digite o 9ª número: "))
    num10 = int(input("Digite o 10ª número: "))
    if(num1 % 2 == 0):
        cnp += 1
    if(num1 % 2 != 0):
        cni += 1
    if (num2 % 2 == 0):
        cnp += 1
    if (num2 % 2 != 0):
        cni += 1
    if (num3 % 2 == 0):
        cnp += 1
    if (num3 % 2 != 0):
        cni += 1
    if (num4 % 2 == 0):
        cnp += 1
    if (num4 % 2 != 0):
        cni += 1
    if(num5 % 2 == 0):
        cnp += 1
    if(num5 % 2 != 0):
        cni += 1
    if (num6 % 2 == 0):
        cnp += 1
    if (num6 % 2 != 0):
        cni += 1
    if(num7 % 2 == 0):
        cnp += 1
    if(num7 % 2 != 0):
        cni += 1
    if (num8 % 2 == 0):
        cnp += 1
    if (num8 % 2 != 0):
        cni += 1
    if(num9 % 2 == 0):
        cnp += 1
    if(num9 % 2 != 0):
        cni += 1
    if (num10 % 2 == 0):
        cnp += 1
    if (num10 % 2 != 0):
        cni += 1
    print("Números pares: %s" %cnp)
    print("Números ímpares: %s" %cni)'''

#15

'''def fibonacci():
    while(True):
        n = int(input("Digite o  número limite da sequencia fibonacci: "))
        num1 = 1
        num2 = 1
        if(n<=0):
            print("Digite outro número!")
            continue
        elif n==1:
            print("0")
            continuar = input("Deseja continuar (s/n): ")
            if continuar == 's':
                continue
            elif continuar == 'n':
                break
            else:
                break
            print("1")
            continuar = input("Deseja continuar (s/n): ")
            if continuar == 's':
                continue
            elif continuar == 'n':
                break
            else:
                break
        elif n==2:
            print("0")
            print("1")  
            continuar = input("Deseja continuar (s/n): ")
            if continuar == 's':
                continue
            elif continuar == 'n':
                break      
            else:
                break      
        elif n==3:
            print("0")
            print("1")  
            print("1")
            continuar = input("Deseja continuar (s/n): ")
            if continuar == 's':
                continue
            elif continuar == 'n':
                break      
            else:
                break  
        elif(n>=4):
            print("0")
            print("1")
            print("1")
            for lista in range(n-1):
                if lista>=2 :
                    print(num1+num2)
                    preserv = num1
                    num1 = num2
                    num2 += preserv
            continuar = input("Deseja continuar (s/n): ")
            if continuar == 's':
                continue
            elif continuar == 'n':
                break
            else:
                break
fibonacci()'''

#Exercicio 16

'''def fibonacci():
    while(True):
        num1 = 1
        num2 = 1
        limite = 0
        print("0")
        print("1")
        print("1")
        while limite <= 500:
                limite = num1+num2
                print(limite)
                preserv = num1
                num1 = num2
                num2 += preserv
        break
fibonacci()'''

#Exercicio 17

'''def func():
    num = int(input("Digite o numero a ser fatorado: "))
    lista = [int(num*(num-1))]
    cont = 1
    for i in range(num-2, 0, -1):
        lista.insert(cont, lista[cont-1]*i)
        cont += 1
    print(lista[-1])
func()'''

#Ecercicio 18

'''def func():
    listaConjunto = list(input("Coloque o conjunto de valores: "))
    listaConjunto.sort()
    menorValor = listaConjunto[0]
    print("O menor valor é: ", menorValor)
    listaConjunto.reverse()
    maiorValor = listaConjunto[0]
    print('O maior valor é: ', maiorValor)
    resultado = 0
    some = int(listaConjunto[0]) + int(listaConjunto[1]) 
    for i in range(2,len(listaConjunto)):
        some += int(listaConjunto[i])  
    print(some)
func()'''

#Exercicio 19
'''def func(conjunto):
    while True:
        listaConjunto = list(str(conjunto))
        if conjunto>=0 and conjunto <=1000:
            pass
        else:
            print("Aceitamos apenas numeros de 0 a 100!")
            continue
        listaConjunto.sort()
        menorValor = listaConjunto[0]
        print("O menor valor é: ", menorValor)
        listaConjunto.reverse()
        maiorValor = listaConjunto[0]
        print('O maior valor é: ', maiorValor)
        resultado = 0
        some = int(listaConjunto[0]) + int(listaConjunto[1]) 
        for i in range(2,len(listaConjunto)):
            some += int(listaConjunto[i])  
        print(some)
        break
func(int(input("Coloque o conjunto de valores: ")))'''

#Exercicio 20

'''def func():
    while True:
        num = int(input("Digite o numero a ser fatorado: "))
        if num < 16 and num>=0:
            if num ==1:
                print(1)
            else:
                lista = [int(num*(num-1))]
                cont = 1
                for i in range(num-2, 0, -1):
                    lista.insert(cont, lista[cont-1]*i)
                    cont += 1
                print(lista[-1])
                continue
        else:
            print("Apenas numeros positivos menores que 16!")
            continue

func()'''

#xercicio 21

'''def func():
    num = int(input("Digite o numero para descobrir se é primo: "))
    if num>0:
        cont = []
        for i in range(1, num+1):
            cont += [1 if num%i==0 else ()]
        if cont.count(1)==2:
            print('É primo!')
        else:
            print("Não é primo!")
func()'''

#Exercicio 22

'''def func():
    num = int(input("Digite o numero para descobrir se é primo: "))
    if num>0:
        cont, cont2 = [], []
        for i in range(1, num+1):
            cont += ['primo' if num%i==0 else ()]; cont2 += [i if num%i==0 else ()] 
        if cont.count('primo')==2:
            print('É primo!')
        elif cont2 != 2:
            varSet = set(cont2); cont2 = list(varSet); cont2.remove(()); cont2.sort()
            print("Não é primo! é divisivel por:", cont2)
func()'''

#Exercicio 23

'''def func(num):
    if num>0:
        cont = []; listaPrimos = []; verific = 0
        for i in range(1, num+1):
            for n in range(1, i+1):
                cont += [i if i%n==0 else ()]; verific += 1
                continue
        for a in range(1, num+1):
            if cont.count(a)==2:
                listaPrimos += [a]
        print(listaPrimos); print('Foram exatas', verific, 'divisões para chegar neste resultado')
func(int(input("Digite o limite para a lista de numeros primos: ")))'''

#Exercicio 24

'''def func(nota):
    listaNotas = []
    while True:
        listaNotas += [nota]; mais = input('Tem mais? (s/n): '); cont = []
        if mais == 's':
            nota = int(input("Digite mais: "))
            continue
        else:
            break
    if len(listaNotas) == 1:
        print('A média é:', listaNotas[-1])
    elif len(listaNotas)==2:
        print('A média é:', (listaNotas[0]+listaNotas[1])/2)
    elif len(listaNotas) > 2:
        cont = [listaNotas[0]+listaNotas[1]]
        for i in range(2, len(listaNotas)):
            cont += [cont[-1]+listaNotas[i]]
        print('A média é:', cont[-1]/len(listaNotas))
func(int(input("Digite sua 1º nota: ")))'''

#Exercicio 25

'''def func(pessoas):
    contadorIdades = 0; a = 0
    print("Digite as idades das pessoas, uma por uma abaixo")
    for i in range(1, pessoas+1):
        if i ==1:
            a = int(input("idade da 1º pessoa: "))
            contadorIdades += a
        else:
            a = int(input("Próxima idade: ")) 
            contadorIdades += a
    if contadorIdades/pessoas<=25:
        print("A turma é jovem!")
    elif contadorIdades/pessoas>26 and contadorIdades/pessoas<=60:
        print("A turma é adulta!")
    else:
        print("A turma é idosa!")
func(int(input("Digite quantas pessoas tem na sala: ")))'''

#Exercicio 26

'''def func(numeroDeEleitores):
    candidatoA = 0; candidatoB = 0; candidatoC = 0
    for i in range(1,numeroDeEleitores+1):
        if i==1:
            voto = input("Primeiro eleitor, pode votar: ")
            if voto=='a' or voto=='A':
                candidatoA+=1
            elif voto=='b' or voto=='B':
                candidatoB+=1
            elif voto=='c' or voto=='C':
                candidatoC+=1
        else:
            voto= input("Próximo eleitor: ")
            if voto=='a' or voto=='A':
                candidatoA+=1
            elif voto=='b' or voto=='B':
                candidatoB+=1
            elif voto=='c' or voto=='C':
                candidatoC+=1
    print("O candidato A recebeu %i votos, o candidato B recebeu %i votos e o candidato C recebeu %i votos!" %(candidatoA, candidatoB, candidatoC))
func(int(input("Digite o numero de eleitores: ")))'''

#Exercicio 27

'''def func(contTurmas, contAlunos, dictAlunos, mediaTurma):
    for i in range(1, contTurmas+1):
        while True:
            print('------', 'Turma', i, '------')
            contAlunos = int(input("Quantos alunos tem nesta turma: "))
            if contAlunos <= 40:
                dictAlunos.update({i:contAlunos})
                break
            else:
                print("As turmas não pdoem ultrapassar de 40 alunos!")    
                continue   
    for i in range(1,len(dictAlunos)+1):
        mediaTurma += dictAlunos[i]
    print('A media de alunos por turma é: ', mediaTurma/len(dictAlunos))        
func(int(input("Digite o numero de turmas: ")), 0, {}, 0)'''

#Exercicio 28

'''def func(contCD, contValor, dictValor, mediaValor):
    for i in range(1, contCD+1):
        print('-------- CD ', i, '--------')
        contValor = int(input("Digite o valor deste CD: "))
        dictValor.update({i:contValor})
    for i in range(1,len(dictValor)+1):
        mediaValor += dictValor[i]
    print("O valor total gasto em CD's foi: %.2f. E o valor médio em cada CD foi: %.2f" %(mediaValor, 
    mediaValor/len(dictValor)))
func(int(input("Dgiite a quantiade de CD's em sua coleção: ")), 0, {}, 0)'''

#Exercicio 29

'''def func():
    num = 0
    print("Lojas quase dois - Tabela de preços")
    for i in range(1, 51):
        num = i*1.99
        print(i, '-', 'R$ %.2f' %(num))
func()'''

#Exercicios 30

'''def func():
    num = 0 
    print("Preço do pão: R$ 0.18")
    print("Panificadora Pão de Ontem - Tabela de preços")
    for i in range(1, 51):
        num = i * 0.18
        print(i, '-', 'R$ %.2f' %(num))
func()'''

#Exercicios 31

'''def func():
    while True:
        valorTotal = 0; num = 0; dictListaCompras = {}; pagamento = 0
        print("Lojas Tabajara")
        for i in range(1, 1000):
            num = (float(input('Produto {}: R$ '.format(i))))
            dictListaCompras.update({i:num})
            if num == 0:
                break
        for i in range(1, len(dictListaCompras)+1):
            valorTotal += dictListaCompras[i]
        print('Total: R$', valorTotal)
        pagamento = float(input("Dinheiro: R$ "))
        print("Troco: R$", pagamento-valorTotal)
        continuar = input("0 para reininar o programa, 1 para finalizar: ")
        if '0'==continuar:
            continue
        elif '1'==continuar:
            break
        else:
            break
func() '''

#Exercicio 32

'''def func(fatorial, listaFatorialString):
    listaFatorialInt = [fatorial]
    print("Fatorial de:", fatorial)
    for i in range(fatorial, 0, -1): 
        listaFatorialString += [str(i) + ' ' + '.' + ' ' if i!=1 else str(i)]
    for i in range(fatorial-1, 0,-1):
        listaFatorialInt += [listaFatorialInt[-1]*i]
    print("{0}! = {1} = {2}".format(fatorial, ''.join(listaFatorialString),listaFatorialInt[-1]))
func(int(input("Digite o numero a ser fatorado: ")), [])'''

#Exercicio 33

'''def func():
    while True:
        numTemperaturas = []
        totalTemperaturas = 0
        print("----------- PROGRAMA PARA TEMPERATURAS --------")
        print("QUANDO ACABAR OS VALORES, DIGITE 0.07")
        for i in range(1,1001):
            numTemperaturas += [float(input("Digite a temperatura em graus Celsius: "))] 
            if numTemperaturas[-1]==0.07:
                break
        numTemperaturas.remove(0.07)
        for i in range(len(numTemperaturas)):
            totalTemperaturas += numTemperaturas[i]
        numTemperaturas.sort();
        print("A temperatura máxima foi %.2f, a mínima foi %.2f e a média foi %.2f" 
        %(numTemperaturas[-1], numTemperaturas[0], totalTemperaturas/len(numTemperaturas)))
        while True:
            continuar = input("0 para reiniciar o programa, 1 para finalizar\n")
            if continuar == '0':
                break
            elif continuar=='1':
                break
            else:
                continue
        if continuar=='1':
            break
func()'''

#Exercicio 34

'''def func():
    while True:
        numPrimo = int(input("Digite um numero para saber se é primo: ")); listaPrimo = []
        for i in range(1, numPrimo+1):
            for a in range(1, i+1):
                listaPrimo += [i if i%a==0 else ()]
        if listaPrimo.count(numPrimo)==2:
            print("É primo!")
        else:
            print("Não é primo")
        continuar = input("0 para reiniciar e 1 para finalizar: ")
        if continuar!='0' and continuar!='1':  
            while True:
                continuar = input("0 para reiniciar e 1 para finalizar: ")
                if continuar!='0' and continuar!='1':
                    continue
                else:
                    break
        elif continuar=='0':
            continue
        else:
            break
func()'''

#Exercicio 35

'''def func():
    while True:
        numPrimo = int(input("Digite o numero limite para a sequência de primos: ")) 
        listaPrimo = []; listaPrimo2 = []
        for i in range(1, numPrimo+1):
            for a in range(1, i+1):
                listaPrimo += [i if i%a==0 else ()]
        print('Lista de numeros primos ate {0}:'.format(numPrimo))
        for i in range(1,len(listaPrimo)+1):    
            if listaPrimo.count(i)==2:
                listaPrimo2 += [i]
        listaPrimo2.sort(); listaCerta = ''.join(str(listaPrimo2))
        a = listaCerta.strip('[]')
        print(a)
        continuar = input("0 para reiniciar e 1 para finalizar: ")
        if continuar!='0' and continuar!='1':  
            while True:
                continuar = input("0 para reiniciar e 1 para finalizar: ")
                if continuar!='0' and continuar!='1':
                    continue
                else:
                    break
        elif continuar=='0':
            continue
        else:
            break
func()'''

#Exercicio 36

'''def func():
    numTabuada = int(input("Montar tabuada de: "))
    numComecar = int(input("Começar por: "))
    numTerminar = int(input("Terminar em: "))
    while numTerminar<numComecar:
        print("O final é menor que o inicial! mude isto!")
        numTerminar = int(input("Terminar em: "))
    print()
    print("Vou montar a tabuada de {0} começando por {1} e terminando em {2}:".format(numTabuada, numComecar, numTerminar))
    for i in range(numComecar, numTerminar+1):
        print("{0} x {1} = {2}".format(numTabuada, i, numTabuada*i))
func()'''

#Exercicio 37

'''def func(numCodigo, listaCodigo, numAltura, listaAltura, numPeso, listaPeso):
    totalCodigo = 0; totalAltura = 0; totalPeso = 0
    print('--------- PROGRAMA DE ACADEMIA ---------\n')
    while True:
        numCodigo = float(input('Codigo: ')); listaCodigo += [numCodigo]
        if int(numCodigo)==0:
            break
        numAltura = float(input('Altura: ')); listaAltura += [numAltura]
        numPeso = float(input('Peso: ')); listaPeso += [numPeso]
        print()
    listaCodigo.sort(); listaAltura.sort(); listaPeso.sort()
    for i in range(len(listaAltura)):
        totalCodigo += listaCodigo[i]
        totalAltura += listaAltura[i]
        totalPeso += listaPeso[i]
    print(
        f"A altura máxima foi {listaAltura[-1]}, mínima de {listaAltura[0]} e a média é de {totalAltura/len(listaAltura)}\n"
        f'O peso máximo foi de {listaPeso[-1]}, mínimo de {listaPeso[0]} e a média é de {totalPeso/len(listaPeso)}'
        )
func(0.0,[],0.0,[],0.0,[])'''

#Exercicio 38

'''def func():
    print('Calculadora de salário')
    salario = float(input("Digite seu salário em 1995: "))
    aumentoBase = 1.5
    salarioAno = 0
    ano = 1995
    for i in range(1, 2022-1996+1+1):
        salarioAno = ((salario*aumentoBase)/100)+salario
        salario = salarioAno
        aumentoBase *= 2
        ano+=1
    print(f"O salario dele hoje em %i é de %.2f" %(ano,salario))
func()'''

#Exercicio 39

'''def func():
    print("PROGRAMA DE DOIS VALORES")
    dictAluno = {}
    numAluno = 0
    numAltura = 0.0
    maximoAluno = []
    minimoAluno = []
    for i in range(1, 3):
        print(f'-------------- {i}º Aluno --------------')
        numAluno = int(input('Digite o numero deste aluno: '))
        numAltura = float(input('Digite a altura deste aluno: '))
        dictAluno.update({i:[numAluno, numAltura]}) 
    for i in range(1, len(dictAluno)+1):
        listaAluno = dictAluno[i]
        if i==1:
            maximoAluno = listaAluno 
            minimoAluno = listaAluno
        elif listaAluno[1] > maximoAluno[1]:
            maximoAluno = listaAluno
        elif listaAluno[1] == maximoAluno[1]:
            pass
        elif listaAluno[1] < minimoAluno[1]:
            minimoAluno = listaAluno
    print(f'O numero do aluno mais alto da sala é: {maximoAluno[0]}, sua altura é {maximoAluno[1]}\n'
    f'O numero do aluno mais baixo da sala é: {minimoAluno[0]}, sua altura é {minimoAluno[1]}\n')
func()'''

#Exercicio 40

'''def func():
    print("Programa de verdade")
    dictNum = {}
    numCodigo = 0
    numVeiculos = 0
    numAcidentes = 0
    listaNum = []
    numMaximo = []
    numMinimo = []
    listaMediaVeiculos = []
    listaMediaAcidentes = []
    numMediaVeiculos = 0
    numMediaAcidentes = 0
    for i in range(1,3):
        print(f'-------------- {i}º CIDADE --------------')
        numCodigo = int(input("Digite o cóodigo da cidade: "))
        numVeiculos = int(input("Digite quantos veículos a passeio tinha em 1999: "))
        numAcidentes = int(input("Digite o numero de acidentes desta cidade em 1999: "))
        dictNum.update({i:[numCodigo, numVeiculos, numAcidentes]})
    print('')
    for i in range(1, len(dictNum)+1):
        listaNum = dictNum[i]
        if i==1:
            numMaximo  = listaNum
            numMinimo = listaNum
            listaMediaVeiculos += [listaNum[1]]
            if listaNum[2]<2000:
                listaMediaAcidentes +=  [listaNum[2]]
        elif listaNum[1]>numMaximo[1]:
            numMaximo = listaNum
            listaMediaVeiculos += [listaNum[1]]
            if listaNum[2]<2000:
                listaMediaAcidentes +=  [listaNum[2]]
        elif listaNum[1]==numMaximo[1]:
            listaMediaVeiculos += [listaNum[1]]
            pass
            if listaNum[2]<2000:
                listaMediaAcidentes += [listaNum[2]]
        elif listaNum[1] < numMinimo[1]:
            listaMediaVeiculos += [listaNum[1]]
            numMinimo = listaNum
            if listaNum[2]<2000:
                listaMediaAcidentes += [listaNum[2]]
    for i in range(0, len(listaMediaVeiculos)):
        numMediaVeiculos += listaMediaVeiculos[i]
    print(f'O codigo da cidade que tem o maior índice é {numMaximo[0]}, com exatos {numMaximo[2]} de acidentes\n'
    f'O codigo da cidade que tem o menor índice é {numMinimo[0]}, com exatos {numMinimo[2]} de acidentes\n'
    f'A média de veículos nas cidades são de: {numMediaVeiculos/len(listaMediaVeiculos)}\n')
    if len(listaMediaAcidentes)>0:
        for i in range(len(listaMediaAcidentes)):
            numMediaAcidentes += listaMediaAcidentes[i]
        print(f'A média de acidentes em cidades com menos de 2000 mil veículos em circulação é de: {numMediaAcidentes/len(listaMediaAcidentes)}')
    else:
        print('Não tem nenhuma cidade com menos de 2000 mil veículos em circulação.')
func()'''

#Exericio 41

'''def func(valorDivida):
    print('Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela')
    print(f'R$ {valorDivida}        0           1\n'
    f'R$ {valorDivida}\n' 
    f'R$ {((valorDivida*10)/100)+valorDivida}       {((valorDivida*10)/100)+valorDivida-valorDivida}             3')      
    print(f'R$ {(((valorDivida*10)/100)+valorDivida)/3}\n'
    f'R$ {((valorDivida*15)/100)+valorDivida}       {((valorDivida*15)/100)+valorDivida-valorDivida}          6\n'
    f'R$ {(((valorDivida*15)/100)+valorDivida)/3}')
    print(f'R$ {((valorDivida*20)/100)+valorDivida}       {((valorDivida*20)/100)+valorDivida-valorDivida}            9\n'
    f'R$ {(((valorDivida*20)/100)+valorDivida)/3}\n'
    f'R$ {((valorDivida*25)/100)+valorDivida}       {((valorDivida*25)/100)+valorDivida-valorDivida}            12\n'
    f'R$ {(((valorDivida*20)/100)+valorDivida)/3}\n')
func(int(input("Digite o valor da dívida: ")))'''

#Exercicio 42

'''def func(listaNum):
    intervalo25 = 0
    intervalo50 = 0
    intervalo75 = 0
    intervalo100 = 0
    while True: 
        listaNum += [int(input("Digite o número: "))]
        if listaNum[-1]<0:
            break
    for i in range(len(listaNum)):
        if listaNum[i] >= 0 and listaNum[i] <= 25:
            intervalo25+=1
        elif listaNum[i] >= 26 and listaNum[i] <= 50:
            intervalo50 +=1
        elif listaNum[i] >= 51 and listaNum[i] <= 75:
            intervalo75 +=1
        elif listaNum[i] >= 76 and listaNum[i] <= 100:
            intervalo100 +=1
    print(f'{intervalo25} numeros estão entre o intervalo 0-25\n'
    f'{intervalo50} numeros estão entre o intervalo 26-50\n'
    f'{intervalo75} numeros estão entre o intervalo 51-75\n'
    f'{intervalo100} numeros estão entre o intervalo 76-100\n')
func([])'''

#Exercicio 43

'''from tabulate import tabulate
def func():
    listaCarda = [['Cachorro Quente', 100, 'R$ 1,20'],
    ['Bauru Simples', 101, 'R$ 1,30'],
    ['Bauru com Ovo', 102, 'R$ 1,50'],
    ['Hambúrguer', 103, 'R$ 1,20'],
    ['Cheeseburguer', 104, 'R$ 1,30'],
    ['Refrigerante', 105, 'R$ 1,00']]
    dictCarda = {100: 1.20, 101: 1.30, 102: 1.50, 103: 1.20, 104: 1.30, 105: 1.00}
    print('------------------- CARDAPIO LANCHONETE -------------------\n')
    print(tabulate(listaCarda, headers=['Especificação', 'Código', 'Preço']))
    print()
    print("Quando acabar de pedir, digite 0 no código")
    numPedido = 0; quantPedido = 0; a = []; listaNomes = []; listaValor = []; total = 0
    while True:
        numPedido = int(input("Digite o código do seu pedido: "))
        if numPedido == 0:
            break
        quantPedido = int(input("Digite a quantidade de unidade deste pedido: "))
        for i in range(len(listaCarda)):
            a = listaCarda[i]
            if a[1]==numPedido:
                listaNomes += [a[0]]
                break
            else:
                pass
        listaValor += [dictCarda[numPedido]*quantPedido]
    for i in range(len(listaValor)):
        total += listaValor[i]
    print()
    for i in range(len(listaValor)):
        print(f"O valor total do pedido (%s) é %.2f" %(listaNomes[i], listaValor[i]))
    print()
    print("O total é de: ", total)

        
func()'''

#Exercicio 44

'''from tabulate import tabulate
def func():
    print("------------ Eleição presidencial ------------")
    listaCandidatos = [['1 - ', 'Vinicius'], ['2 - ', 'João'], ['3 - ', 'Maria'], ['4 - ', 'Bolsonaro'],
    ['5 - ', 'Lula'], ['6 - ', 'Voto em Nulo'], ['7 - ', 'Voto em Branco']]
    listaVotos = []; a = 0; b = []; c = 0; listaFinal = []
    print(tabulate(listaCandidatos, headers=('Numero de voto', 'Nome do eleitor')))
    print()
    while True:
        a+=1
        listaVotos += [int(input(f'{a}º Eleitor, seu voto: '))]
        if listaVotos[-1]==0:
            break
    listaVotos.remove(0)
    for i in range(len(listaCandidatos)):
        b = listaCandidatos[i]
        c += 1
        listaFinal += [[b[1], listaVotos.count(c)]]
    print()
    print(tabulate(listaFinal, headers=('Candidatos', 'Total de Votos')))
    print()
    print(f'A porcentagem de votos nulos sobre o total de votos foi de {(listaVotos.count(6)*100)/len(listaVotos)}\n'
    f'A porcentagem de votos Brancos sobre o total de votos foi de {(listaVotos.count(7)*100)/len(listaVotos)}')
func()'''

#Exericio 45

'''import os
os.system('cls') or None
def func():
    print("--------------- Programa para avaliações bimestrais ---------------")
    dictGabarito = {}; respostasAlunos = []; listaRespostas = []; a = 0; b = []; listaAcertos = []
    listaMaximoAcertos = []; listaMinimoAcertos = []; d = 0; e = 0;listaMedia = []; numMedia = 0
    for i in range(10):
        print("--------------- PROFESSOR ---------------")
        dictGabarito.update({i: input(f'Digite a resposta da questão {i+1}: ')})
        os.system('cls') or None
    while True:
        a += 1
        for i in range(1,11):
            print(f"--------------- ALUNO {a} ---------------")
            respostasAlunos += [input(f'Alternativa certa da Questão {i}: ')]
            os.system('cls') or None
        listaRespostas += [respostasAlunos]
        respostasAlunos = []
        d+=1
        usarSistema = input("Mais algum aluno vai utlizar o sistema (S/N)?\n")
        if usarSistema=='s':
            pass
        else:
            break
    for i in range(len(listaRespostas)):
        b = listaRespostas[i]
        for c in range(len(b)):
            if b[c]==dictGabarito[c]:
                e += 1
        listaAcertos += [[i, e]]
    for i in range(len(listaAcertos)):
        b = listaAcertos[i]
        if i==0:
            listaMaximoAcertos = listaMinimoAcertos = b
        elif b[1]>listaMaximoAcertos[1]:
            listaMaximoAcertos = b
        elif b[1]==listaMaximoAcertos[1]:
            pass
        elif b[1]<listaMinimoAcertos[1]:
            listaMinimoAcertos = b
    for i in range(len(listaAcertos)):
        listaMedia = listaAcertos[i]
        numMedia += listaMedia[1]
    os.system('cls') or None
    print(f'O maior acerto foi {listaMaximoAcertos[1]}\n'
    f'O menor acerto foi {listaMinimoAcertos[1]}\n'
    f'O sistema foi utilizado por {d} pessoas!\n'
    f'A nota média da turma foi de {numMedia/len(listaAcertos)}')
func()'''

#Exercicio 46

'''import os
os.system('cls') or None
def func():
    while True:
        nome = input("Digite seu nome: ") 
        if nome == '':
            break
        listaSalto = []
        for i in range(1,6):
            #os.system('cls') or None
            listaSalto += [float(input(f'Digite o {i}º salto: '))]
            #os.system('cls') or None
        laranja = listaSalto; laranja.sort(); listaSalto.pop(0); listaSalto.pop(-1)
        print(f'Melhor salto: %.2f m' %laranja[-1])
        print(f'Pior salto:  %.2f m' %laranja[0])
        print(f'Média dos demais saltos: %.2f' %((listaSalto[0] + listaSalto[1] + listaSalto[2])/3))
        print(f'Resultado Final: ')
        print(f'{nome}: %.2f m' %((listaSalto[0] + listaSalto[1] + listaSalto[2])/3)); print()
        
func()'''

#Exercicio 47

'''import os
from statistics import median
os.system('cls') or None
def func():
    nome = input(f"Digite seu nome: ")
    listaNotas = []; media = 0.0
    for i in range(1,8):
        os.system('cls') or None
        listaNotas += [float(input(f'Digite a nota do {i}º jurado: '))]
        os.system('cls') or None
    listaNotas.sort()
    for i in range(1,6):
        media += listaNotas[i]/i
    print(f'Resultado final: \n'
    f'Atleta: {nome}\n'
    f'Melhor nota: %.2f\n' 
    f'Pior nota: %.2f\n'
    f'Média: %.2f' %(listaNotas[-1], listaNotas[0], media))
func()'''

#Exercicio 48

'''import os
os.system('cls') or None
def func():
    numero = input('') 
    #Voce pode colocar nas aspas qualquer frase caso queira imprimir algo, eu preferi deixar sem.
    numero = list(numero)
    for i in range(len(numero)):
        numero[i] = int(numero[i])
    for i in range(-1, -(len(numero)+1), -1):
        print(numero[i], end='')
func()'''

#Exercicio 49

'''import os
os.system('cls') or None
def func():
    n = int(input('Digite o valor do enésimo termo: '))
    print('S = ', end='')
    a = 0; listaValor = []; soma = 0
    for i in range(1, n+1):
        if i==1:
            print(f'{i}/{i} + ', end='')
            listaValor += [i/(i+a)]
        elif i==n:
            a += 1
            print(f'{i}/{i+a}', end=' = ')
            listaValor += [i/(i+a)]
            for y in range(len(listaValor)):
                soma += listaValor[y]
            print(f'%.2f.' %soma)
        else:
            a += 1
            print(f'{i}/{i+a} + ', end='')
            listaValor += [i/(i+a)]
func()'''

'''#Exercicio 50

import os
os.system('cls') or None
def func():
    n = int(input("Digite o enésimo termo: "))
    print(f'H = ', end='') 
    listaValores = []; a = 0; soma = 0
    for i in range(1, n+1):
        if i==1:
            print(f'1 + ', end='')
            listaValores += [i]
        elif i==n:
            print(f'1/{i} = ', end='')
            listaValores += [1/i]
            for a in range(len(listaValores)):
                soma += listaValores[a]
            print(f'%.2f' %soma)
        else:
            print(f'1/{i} + ', end='')
            listaValores += [1/i]
func()'''

#Exercicio 51

'''import os
os.system('cls') or None
def func():
    n = int(input('Digite o valor do enésimo termo: '))
    print('S = ', end='')
    a = 0; listaValor = []; soma = 0
    for i in range(1, n+1):
        if i==1:
            print(f'{i}/{i} + ', end='')
            listaValor += [i/(i+a)]
        elif i==n:
            a += 1
            print(f'{i}/{i+a}', end=' = ')
            listaValor += [i/(i+a)]
            for y in range(len(listaValor)):
                soma += listaValor[y]
            print(f'%.2f.' %soma)
        else:
            a += 1
            print(f'{i}/{i+a} + ', end='')
            listaValor += [i/(i+a)]
func()'''

#Lista de Exercícios 4 - listas

#Exercicio 1

'''import os
def func():
    listaVetor = []
    for i in range(5):
        listaVetor += [input(f'Digite o número do numero {i+1}: ')]
        os.system('cls') or None
        if i==4:
            for a in range(len(listaVetor)):
                if a<4:
                    print(f'{listaVetor[a]}', end=', ')
                if a==4:
                    print(f'{listaVetor[a]}', end='')
func()'''

#Exercicio 2

'''import os
def func():
    listaVetor = []
    for i in range(10):
        listaVetor += [input(f'Digite o número do numero {i+1}: ')]
        os.system('cls') or None
        if i==9:
            for a in range(-1, -11, -1):
                if a>-9:
                    print(f'{listaVetor[a]}', end=', ')
                if a==-10:
                    print(f'{listaVetor[a]}', end='')
func()'''

#Exercicio 3

'''from tabulate import tabulate
import os
def notas():
    listaNotas = []; a = []; valorTotal = 0
    for i in range(4):
        listaNotas += [[f'{i+1}º Nota - ', input(f'Digite a {i+1}º nota: ')]]
        os.system('cls') or None
    print(tabulate(listaNotas, headers=('Bimestre', 'Notas')))
    print()
    for  i in range(len(listaNotas)):
        a = listaNotas[i]
        valorTotal += float(a[1])
    print(f'O valor da média é {valorTotal/len(listaNotas)}')
notas()'''

#Exercicio 4

'''import os
def vetor():
    lista = []; listaVogais = ['a','e','i','o','u']; a =''; contConsoantes = 0
    for i in range(10):
        lista += [input(f'Digite o {i+1}º vetor: ')]
        os.system('cls') or None
    for i in range(len(lista)):
        a = lista[i]
        contConsoantes += len(a)
        for e in listaVogais:
            if e in a:
                contConsoantes -= len(a)
    print(f'Foram lidas {contConsoantes} consoantes!')
vetor()  '''

#Exercicio 5

'''import os
os.system('cls') or None
def vetor():
    listaVetor = []; vetorPar = []; vetorImpar = []
    for i in range(20):
        listaVetor += [int(input(f'Digite o {i+1}º numero: '))]
        os.system('cls') or None
        if listaVetor[-1]%2==0:
            vetorPar += [listaVetor[-1]]
        else:
            vetorImpar += [listaVetor[-1]]
        if i==19:
            print(f'Lista de todos os numeros inteiros digitados abaixo: ')
            for a in range(len(listaVetor)):
                if a<len(listaVetor)-1:
                    print(f'{listaVetor[a]}', end=', ')
                else:
                    print(f'{listaVetor[a]}', end='\n')
            print(f'Lista de todos os numeros pares digitados abaixo: ')
            for a in range(len(vetorPar)):
                if a<len(vetorPar)-1:
                    print(f'{vetorPar[a]}', end=', ')
                else:
                    print(f'{vetorPar[a]}', end='\n')
            print(f'Lista de todos os numeros ímpares digitados abaixo: ')
            for a in range(len(vetorImpar)):
                if a<len(vetorImpar)-1:
                    print(f'{vetorImpar[a]}', end=', ')
                else:
                    print(f'{vetorImpar[a]}', end='')
vetor()'''

#Exercicio 6

'''import os
os.system("cls") or None
def alunos():
    listaNotas = []; mediaNotas = {}; media = 0.0; imprimidos = 0
    for i in range(10):
        print(f'-------------- {i+1}ª Aluno --------------')
        for a in range(4):
            listaNotas += [float(input(f'Digite a {a+1}º nota deste aluno: '))]
            if a==3:
                for e in range(len(listaNotas)):
                    media += listaNotas[e]
                media = media/len(listaNotas) 
        os.system("cls") or None
        mediaNotas.update({i+1: media})
        os.system("cls") or None; media = 0.0
    media = []
    for i in range(1,len(mediaNotas)+1):
        media = mediaNotas[i]
        if media>=7:
            imprimidos += 1
    print(f'Tem {imprimidos} alunos com a media maior ou igual a 7')
alunos()'''

#Exercicio 7

'''def vetor():
    lista = []
    for i in range(5):
        lista += [int(input(f'Digite o {i+1}º numero: '))]
    print('Os Numeros são: ')
    for i in range(len(lista)):
        if i<len(lista)-1:
            print(f'{lista[i]}', end=', ')
        else:
            print(f'{lista[i]}', end='\n')
    print(f'O resultado da adição é: {lista[0] + lista[1] + lista[2] + lista[3]}')
    print(f'O resultado da multiplicação é: {lista[0] * lista[1] * lista[2] * lista[3]}')
vetor()'''

#Exercicio 8
'''import os
os.system("cls") or None
def vetor():
    idade, altura = [], []
    for i in range(5):
        print(f'--------------- {i+1}º Pessoa ---------------')
        idade += [int(input("Digite sua iade: "))]
        altura += [float(input("Digite sua altura: "))]
    for i in range(5):
        print(f"A {5-i}º tem {idade[4-i]} de idade e {altura[4-i]} de altura!")
vetor()'''

#Exercicio 9

'''import os 
os.system('cls') or None
def vetor():
    a = []; soma = 0
    for i in range(10):
        a += [int(input(f"Digite o {i+1}º numero do vetor: "))]
        soma += a[i]**2
    print(f"A soma dos quadrados dos elementos é: {soma}")
vetor()'''

#Exercicio 10
'''import os
os.system("cls") or None
def vetor():
    vetorA, vetorB = [], []
    print('----------- Vetor 1 -----------')
    for i in range(10):
        vetorA += [int(input(f"Digite o {i+1}º numero deste vetor:  "))]
        if i==9:
            os.system('cls') or None
            print('----------- Vetor 2 -----------')
            for a in range(10):
                vetorB += [int(input(f"Digite o {a+1} numero deste vetor: "))]
    os.system('cls') or None
    print('A junção dos dois vetores resultou neste novo vetor:')
    for i in range(20):
        if i>=0 and i<9:
            print(f'{vetorA[i]},', end=' ')
        elif i>=9 and i<19:
            print(f'{vetorB[i-10]},', end=' ')
        elif i==19:
            print(f'{vetorB[i-10]}.', end='')
vetor()'''

#Exercicio 11

'''import os
os.system("cls") or None
def vetor():
    vetorA, vetorB, vetorC = [], [], []
    print('----------- Vetor 1 -----------')
    for i in range(10):
        vetorA += [int(input(f"Digite o {i+1}º numero deste vetor:  "))]
    os.system('cls') or None 
    print('----------- Vetor 2 -----------')
    for i in range(10):
        vetorB += [int(input(f"Digite o {i+1} numero deste vetor: "))]
    os.system('cls') or None
    print('----------- Vetor 3 -----------')
    for i in range(10):
        vetorC += [int(input(f"Digite o {i+1} numero deste vetor: "))]
    os.system('cls') or None
    print('A junção dos dois vetores resultou neste novo vetor:')
    for i in range(30):
        if i>=0 and i<9:
            print(f'{vetorA[i]},', end=' ')
        elif i>=9 and i<19:
            print(f'{vetorB[i-10]},', end=' ')
        elif i>=19 and i<=28:
            print(f'{vetorB[i-20]},', end=' ')
        elif i==29:
            print(f'{vetorB[i-20]}.', end='')
vetor()'''

#Exercicio 12

import os
os.system('clear') or None
def vetor():
    idade, altura = [], []
    for i in range(5):
        print(f'--------------- {i+1}º Aluno ---------------')
        idade += [int(input("Digite sua iade: "))]
        altura += [float(input("Digite sua altura: "))]
    for i in range(5):

vetor()

            





    

        

    
        


            
    
    



        
        
    
    
        
        










        

           

            



    


















