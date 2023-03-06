import random, os  

esconde = random.randrange (0,50)

dificuldade = int(input(" 1-suave \n 2-mediano \n 3-lendario \n R: "))
acertou = False

if dificuldade == 1:
    tentativas = 15
elif dificuldade == 2:
    tentativas = 10
else:
    tentativas = 5

for x in range (0, tentativas) :
    print("Você tem " + str(x + 1) + " de " + str(tentativas) + " tentativas")

    nt = int (input("Sugira um numero: "))
    if nt > esconde:
        print("Esta mais a esquerda")
    elif nt < esconde: 
        print("Esta mais para a direita")
    else: 
        acertou = True
        break

if acertou == False:
    print("Você acabou perdendo, ele está na posição " + str(esconde))
else:
    print("Finalmente achou!")