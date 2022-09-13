#Exercicio a parte
#Exercicio 1
'''for a in range(1,101):
    print(a)'''

#Exercicio 2

'''while(True):
    a,b,c = int(input("Digite o inicio da contagem: ")), int(input("Digite o Fim da contagem: ")) + 1, int(input("Digite o intervalo da contagem: "))
    for contagem in range(a,b,c):
        print(contagem)
    continuar = input("Deseja continuar? (s/n): ")
    if(continuar=="s"):
        continue
    elif("n"==continuar):
        break
    else:
        break    '''

#Exercicio 3
'''for a in range(10,0,-1):
    print(a)'''

#Exercicio 4
'''for a in range(1,101):
    if(a%2==0):
        print(a)'''

#Exercicio 5
'''cont = 0
for a in range(0,101):
    if(a%2==0):
        cont+=1
print(cont)'''

#Exercicio 6

'''def func():
    cont = []
    for i in range(1, 101):
        for n in range(1, i+1):
            cont += [i if i%n==0 else ()]
            continue
    for a in range(101):
        if cont.count(a)==2:
            print(a)
        else:
            pass
func()'''


#Exercicio 7

'''def func(num):
    if num>0:
        cont = []
        listaPrimos = []
        for i in range(1, num+1):
            for n in range(1, i+1):
                cont += [i if i%n==0 else ()]
                continue
        for a in range(1, num+1):
            if cont.count(a)==2:
                listaPrimos += [a]
            else:
                pass
        print(listaPrimos)     
func(int(input("Digite o limite para a lista de numeros primos: ")))'''

#Exercicio 8

'''def func():
    comeco, final, numIgnorados = int(input("Digite o começo do intervalo: ")), int(input("Digite o final do intervalo: ")), input("Digite os numeros que serão ignorados:  ")
    listaNum = numIgnorados.split(" ")
    for i in range(comeco, final+1):
        if str(i) in listaNum:
            pass
        else:
            print(i)
func()'''

#Exercicio 9

'''def loop(chave = 0):
    while chave != 'q':
        print("estou em looping! ")
        chave = input("Digite uma letra: ")
    else:
        pass
loop()'''

print(print("teste"),"1")







        
        
    

    
                
            
                



