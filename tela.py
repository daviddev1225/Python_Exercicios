from tkinter import *

janela = Tk()
janela.title("Ola!")
texto = Label(janela, text="Um programa criado por David")
texto.grid(column=0, row=0, padx=20, pady=30)
botao = Button(janela, text="Quit", command=janela.destroy)
botao.grid(column=0, row=1)
janela.mainloop()