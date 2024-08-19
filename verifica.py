print("Verificador de idade para jovens")

idade = int(input("Entre com a idade para verificação\n"))

if idade < 16:
    print("Você é de menor, ainda não pode entrar!")
elif idade <= 17:
    print("Você é emancipado")
elif idade > 18: 
    print("Você é maior de idade e pode entrar")
else: 
    print("Idade não encontrada!")