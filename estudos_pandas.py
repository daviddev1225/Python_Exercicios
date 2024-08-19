import pandas as pd

precos = {'temperos': ["cominho", "oregano", "coloral", "louro"], 'valor': [2.50, 2.00, 3.50, 3.00]}

tabela = pd.DataFrame(precos)
print(tabela)