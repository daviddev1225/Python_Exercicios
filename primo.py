def primo(numero):
    if numero > 1:
        for x in range(2, numero):
            if(numero % x) == 0:
                return "Esse numero nao e primo"
                break
            else:
                return "Esse numero e primo"
    else:
        return "Esse numero nao e primo, numero maior ou igual a 1"