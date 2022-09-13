#Exercicio 1 do desafio

import sys
def comparaTamanhoSapatos():
    tamanhoIsabela = sys.stdin.readline(); tamanhoLuisa = sys.stdin.readline() 
    tamanhoIsabela = tamanhoIsabela.replace('\n', ''); tamanhoLuisa = tamanhoLuisa.replace('\n', '')
    
    if int(tamanhoIsabela)>int(tamanhoLuisa):
        sys.stdout.write('Isabela calça mais')
    elif int(tamanhoIsabela)<int(tamanhoLuisa):
        sys.stdout.write('Luisa calça mais')
    elif int(tamanhoIsabela)==int(tamanhoLuisa):
        sys.stdout.write('Isabela e Luisa calçam o mesmo tamanho de sapato')
comparaTamanhoSapatos()

#Exericio 2 do desafio

'''import sys
def tripleTheChances(chances):
    chances = chances.replace('\n', '')
    chances = chances.split(" ")
    for i in range(len(chances)):
        sys.stdout.write(str(int(chances[i])*3))
        print('')
tripleTheChances(sys.stdin.readline())'''
#Exercicio 3 do desafio

'''import sys
def vezesLetraAprece():
    frase = sys.stdin.readline()
    letra = sys.stdin.readline()
    frase = frase.replace('\n', "")
    letra = letra.replace('\n', "")
    if frase.count(letra)>0:
        sys.stdout.write(frase)
        print()
        sys.stdout.write(str(frase.count(letra)))
    else:
        sys.stdout.write(str(frase.count(letra)))
vezesLetraAprece()'''