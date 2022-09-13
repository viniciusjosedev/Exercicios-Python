'''while(True):
	a = int(input("Digite um numero: "))
	if(a%2==0):
		print("O numero é par")
		continuar = str(input("Quer continuar a brincadeira? s/n: "))
		if(continuar=="s"):
			continue
		else:
			break
	else:
		print("O numero é impar")
		continuar = str(input("Quer continuar a brincadeira? s/n: "))
		if(continuar=="s"):
			continue
		else:
			break'''


'''while(True):
    num = float(input("Digite um numero: "))
    result = "par" if num%2==0 else "impar"
    print("O numero digitado é ", result)
    continuar = str(input("Quer continuar a brincadeira? s/n: "))
    if continuar == "s": 
        continue
    else:
        break'''

'''num_int = 19
num_float = 19.5
num_texto = "dezenove"
print("minha idade é: %.5f, %.1f, %s" %(num_float, num_float, num_texto))
print("teste", num_int, num_float, num_texto)'''

'''import math
print(math.pi)'''

'''import math

def isPrime(n):
    start = 2;

    while start <= math.sqrt(n):
        if n % start < 1:
            return False;
        start += 1;

    return n > 1;'''

'''def fizzBuzz(n):
	# Write your code here
    for i in range(1,n+1):
        if(i%3==0 and i%5==0):
            print("FizzBuzz")
        elif(i%3==0 and i%5!=0):
            print("Fizz")
        elif(i%3!=0 and i%5==0):
            print("Buzz")
        else:
            print(i)
if __name__ == '__main__':
    n = int(input("a "))
    fizzBuzz(n)'''

'''#Brincando com conjuntos

#Listas
#OBS: Todo CONJUNTOO ORDENADO SEJA ELE LISTA, TUPLA, DICIONARIO SAO IDENTIFICADOS PELOS [].
#Conjunto de valores mútaveis e ordenados pelo índice. Identificados com []. Pode ter membros duplcados.
lista = ['pode colocar uma string', True, 1, 1.2]
print(lista)
print(type(lista))
print('-'*50)

#tuplas
#Conjunto de valores imutaveis e ordenados pelo índice. Identificados com (). Pode ter membros duplicados.
tupla = ('pode colocar uma string', True, 1, 1.2)
print(tupla)
print(type(tupla))
print('-'*50)

#Dicionarios
#Conjunto de valores mutáveis e ordenados pelos suas chaves. Identificados com {}. Não pode ter membros duplicados.
dicionario = {'nome': 'Vinicius José da Silva', "idade": 20}
print(dicionario)
print(type(dicionario))
print('-'*50)

#Set
#Conjunto de valores imutaveis e aleatórios. Identificados por {,}. Não pode ter membros duplicados.
conjunto = {'teste', True, 12, 1.4}
print(conjunto)
print(type(conjunto))
print("-"*50)'''

'''
def login(telefone, usuario = 'vinicius', senha = 123):
    print(usuario)
    print(senha)
    print(telefone)
login(21991550920, senha = 'marquinhos', usuario = 13)

claro que '''



'''def soma(x, y, z):
    return x*y*z, 5*x, y*z, 'teste', {'teste', 12}, True
a, b, c, d, e, f = soma(10,20,30)
tupla = soma(10,20,30)
print(a,b,c)
print(tupla)
print(tupla[4])
print(type(tupla[4]))'''





'''def teste(*lista,**dic):
    return(lista, dic)'''

#b = ['1', 12, True ]
#a = teste("teste", 123, True, 1.54, b)
#print(a)
#print(type(a))

#a = teste(nome = 'vinicius', sobrenome = 'Jose')
#print(a)
#print(type(a))

'''a = teste(12,4,5,6, nome='vinicius', sobrenome = 'Jose')
print(a)
print(type(a))'''

'''def lista(nome, sobrenome, idade):
    print(nome)
    print(sobrenome)
    print(idade)

#usuario = 'vinicius', 'jose', 19
usuariodic = {'sobrenome': 'jose', 'idade': 19, 'nome':'vinicius'}
#lista(usuario[0], usuario[1], usuario[2])
lista(*usuariodic)'''


'''def lista(a, b, c, d, e):
    print(a,b,c,d,e)'''
#l = 1,2,3,4,5

#n = {'d': 4, 'e': 5, 'a': 1, 'b': 2, 'c': 3  }

#n = 2,3,4,1,5
#n = [*n]
#n.sort()

#n = [1,5,4,2,3]
#n.sort()
#lista(**dict(zip(('a', 'b', 'c', 'd', 'e'), l)))
 
'''b = 3
def teste():
    a = 5
    def teste1():
        nonlocal a
        global b
        print(a)
        a+=2
        print(a)
        print("-"*50)
        print(b)
        b+=4
        print(b)
    teste1()
teste()'''

'''def fun():
    pass'''

'''def comparaTamanhoSapatos(tamanhoIsabela, tamanhoLuisa):
    if(tamanhoIsabela>tamanhoLuisa):
        print("Isabela calça mais")
    elif(tamanhoIsabela<tamanhoLuisa):
        print("Luisa calça mais")
    else:
        print("Isabela e Luisa calçam o mesmo tamanho de sapato")

comparaTamanhoSapatos(int(input("Digite o tamanho de sapato de Isabela: ")),int(input("Digite o tamanho de sapato de Luisa: ")))'''

'''import random
def multiplosPorTres(numAleatorio = random.randint(1,50)):
    for lista in list(range(1,numAleatorio+1)):
        if (lista%3==0):
            print(lista)
        else:
            print(lista*3)
multiplosPorTres()'''
#Coloque no argumento da função o limite da sequência aleatória, caso não coloque, o limite sera um intervalo de 1 até no maximo 51.


'''def contVogais(frase, letra):
    frase = frase.lower()
    letra = {}
    vogais = "aeiou"
    for i in vogais:
        if i in frase:
            letra[i] = frase.count(i)
    return letra
print(contVogais('teste', 'i'))'''

'''while True():
    while True():
        print("TESTE")'''
        
''' a = int(input("teste: "))
for i in range(1, 21):
    if a > 41:
        pass
    else:
        print(i)'''

#print("teste") and print("1")


'''lista = []
for i in range(5, 2, -1): 
    lista += [str(i)+' '+'.']
a = str(lista)
print(a.remove([]))'''

'''for i in range(False):
    print(i)'''

"""
Um funcionário de uma empresa recebe aumento salarial anualmente.
Sabe-se que:
Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao
dobro do percentual do ano anterior.
Faça um programa que determine o salário atual desse funcionário.
Após concluir isto, altere o programa permitindo que o usuário digite o salário
inicial do funcionário.
"""


caract=[]
vogais=["a","e","i","o","u"]
contvogal = 0
x = 1
while x <= 10:
    entrada = input("Caractere %d: " %x)
    x += 1
    caract.append(entrada)
    if entrada in vogais:
        contvogal += 1
print ("Consoantes: ",(len(caract))-contvogal)
   
'''
Como foi feito no video
letras = []
i = 1
while i <= 10:
    letras.append(input("Letra: "))
    i += 1
i = 0
cont = 0
while i <= 9:
    if letras[1] not in 'aeiou':
        cont += 1
    i += 1
print ("Foram lidos %d consoantes" %cont)
'''










