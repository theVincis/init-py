import random


print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

numero_secreto = random.randrange(1, 101)
total_de_tentativas = 0
pontos = 1000

print("Qual nível de dificuldade?")
print("(1)Fácil (2)Médio (3)Difícil")

nivel = int(input("Defina o nível: "))

if(nivel == 1):
    total_de_tentativas = 20
elif(nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

# print("número secreto: ", numero_secreto)

for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute = input("Digite o seu numero entre 1 e 100: ")
    print("Você digitou", chute)

    chute_int = int(chute)

    acertou = numero_secreto == chute_int
    chute_maior = chute_int > numero_secreto
    chute_menor = chute_int < numero_secreto

    if(chute_int < 1 or chute_int > 100):
        print("Digite um número entre 1 e 100")
        continue

    if(acertou):
        print("Você acertou e fez {} pontos!".format(pontos))
        break
    else:
        if(chute_maior):
            print("Você errou! O seu número foi MAIOR que o valor do número secreto")
        if (chute_menor):
            print("Você errou! O seu número foi MENOR que o valor do número secreto")
            pontos_perdidos = abs(numero_secreto - chute_int)
            pontos = pontos - pontos_perdidos
