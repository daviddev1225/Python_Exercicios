palpite = 0
numero = 9

while palpite < numero:
    print("Qual o numero correto? ")
    palpite = int(input())
    if palpite == numero:
        print("Parabens voce acertou!")
        break
    else:
        print("Voce errou!")
print(bool(palpite))