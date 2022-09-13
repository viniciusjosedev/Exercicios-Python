#TODOS OS GABARITOS DA ESTRUTURA SEQUENCIAL DO https://wiki.python.org.br/EstruturaSequencial !

#1ª Exercício
# Faça um Programa que mostre a mensagem "Alo mundo" na tela.

'''print("Olá Mundo")'''

#2ª Exercício
# Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].

'''num = int(input("Digite um Número: "))
print ("O Número Foi: %s" %num)'''

#3ª Exercício
# Faça um Programa que peça dois números e imprima a soma.

'''num1 = int(input("Digite o 1ª Número: "))
num2 = int(input("Digite o 2ª Número: "))
print ("A Soma dos Dois Números foi: %s" %(num1 + num2))'''

#4ª Exercício
# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

'''print ("----CAUCULADORA DE MEDIAS----")
media1 = float(input("Digite a 1ª Nota: "))
media2 = float(input("Digite a 2ª Nota: "))
media3 = float(input("Digite a 3ª Nota: "))
media4 = float(input("Digite a 4ª Nota: "))
print ()
print("A sua Média Foi: %f" %float(((media1 + media2 + media3 + media4)/4)))'''

#5ª Exercício
# Faça um Programa que converta metros para centímetros.

'''print ("----Conversor de Metros para Centimetros----")
print ()
metros = float(input("Digite o Valor em Metros: "))
print ()
print ("O Valor em Cm é: %.1f" %float(metros*100))'''

#6ª Exercício
# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

'''print ("Calculadora de áreas Circulares")
print ()
raio = float(input("Digite o Raio da Circuferência: "))
print()
print ("A área da Circuferência é(elevado ao quadrado): %.2f" %((raio**2)*3.14))'''

#7ª Exercício
# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

'''print ("Calculadora de Áreas Quadradas Perfeitas")
print()
area = float(input("Digite o Valor da Medida do Quadrado: "))
print()
print ("O resultado da área é: %.2f" %(area**2))'''

#8ª Exercício
#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.

'''print ("----CALCULADORA DE RENDA MENSAL")
print()
recebo = float(input("Quanto Você Ganha Por Hora?: "))
hora = float(input("Quanto Horas de Trabalho Por Mês: "))
print()
print ("Seu Salário Mensal é de : %.2f" %(recebo*hora))'''

#9ª Exercicio
#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).

'''print ("----CONVERSOR DE FARENHEIT----")
print ()
farenheit = float(input("Digite um Valor em Farenheit: "))
print("O Valor em Graus é: %.2f" %(5*(farenheit-32)/9))'''

#10ª Exercício
# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

'''print ("----CONVERSOR DE GRAUS----")
print ()
graus = float(input("Digite um Valor em Graus: "))
print("O Valor em Farenheit é: %s" %((graus*1.8)+32))'''

#11ª Exercício
# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
    # a. o produto do dobro do primeiro com metade do segundo
    # b. a soma do triplo do primeiro com o terceiro.
    # c. o terceiro elevado ao cubo.

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

#12ª e 13ª Exercício
# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# utilizando as seguintes fórmulas:
    # a. Para homens: (72.7*h) - 58
    # b. Para mulheres: (62.1*h) - 44.7

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

#14ª Exercício
# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos)
# deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e
# calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá
# pagar. Imprima os dados do programa com as mensagens adequadas.

'''peso = float(input("Digite o Peso Total da Sua Pesca (Em Quilos): "))
excesso = peso - 50
multa = excesso * 4
print ()
print ("O Peso da Pesca Foi: ", peso)
print ("O Excesso da Pesca foi: ", excesso)
print ("E a Multa Foi: ", multa)'''

#15ª Exercício
# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no
# referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos
# dê:
    # a. salário bruto.
    # b. quanto pagou ao INSS.
    # c. quanto pagou ao sindicato.
    # d. o salário líquido.
    # e. calcule os descontos e o salário líquido, conforme a tabela abaixo:
        # + Salário Bruto : R$
        # - IR (11%) : R$
        # - INSS (8%) : R$
        # - Sindicato ( 5%) : R$
        # = Salário Liquido : R$
#FALTA FAZER

# 16ª Exericicio
# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
# que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

'''area = float(input("Digite a o Tamanho em Metros² da área que deseja ser pintada: "))
contTintas = area/3
if (contTintas <= 18):
    print("Para este Espaço a necessida de litros de tinta é: %s, e o preço total é: R$18,00" %int(contTintas))
else:
    print("Para este espaço a necessidade de litros de tinta é: %.2f, e o preço é acima de %.2f" %(contTintas, contTintas*(int(contTintas/18))))'''

#17ª Exercício
# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

'''arquivo = float(input("Digite o Tamanho do Arquivo em MB: "))
conexao = float(input("Digite a Velocidade da Sua Internet: "))
print ()
print ("O tempo Aproximado Para o Termino deste Download é aproximadamente de: ", (arquivo/(conexao/0.125)))'''

# FIM DO GABARITO

            





    

        

    
        


            
    
    



        
        
    
    
        
        










        

           

            



    


















