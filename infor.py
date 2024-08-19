import pandas as pd

infor = {
    'nome' : ["David", "Erick", "Rubens", "Eulina"],
    'idade' : [42, 41, 69, 79],
    'ocupacao' : ["porteiro", "programador", "plicial", "domestica"],
    'salario' : [2000, 1350, 3500, 2000]
}

dados = pd.DataFrame(infor, index=["filho1", "filho2", "pai", "mae"])
print(dados)