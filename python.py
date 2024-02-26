import random
def jogo_adivinhacao():
    numero_secreto=random.randint(1,10)
    tentativas = 0
    max_tentativas= 5

    print("Bem-vindo ao jogo de adivinhação!")
    print("Tente adivinhar o número entre 1 e 100")

    while tentativas < max_tentativas:
        tentativa=int(input("Digite o seu palpite"))

        if tentativa < numero_secreto:
         print("O número secreto é maior.")

        elif tentativa > numero_secreto:
         print("O número secreto é menor.")
        else:
         print(f"Parabens!Voce acertou o numero secreto, que era{numero_secreto}.")
         break
        tentativa+=1
        print(f"Voce tem{max_tentativas-tentativas} tentativas restantes")
    else:
     print(f"Voce excedeu o numero maximo de tentativas o numero secreto era{numero_secreto}")
             
jogo_adivinhacao()