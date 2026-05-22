import tkinter as tk
from database import *
from enums import *

inicializar_arquivos()
inicializar_vulnerabilidades()

janela = tk.Tk()
janela.title("Sistema de Inventário TI")
janela.geometry("400x300")

tk.Label(janela, text="Sistema de Inventário de TI", font=("Arial", 14)).pack(pady=10)

tk.Button(janela, text="Cadastrar Ativo", width=25).pack(pady=5)
tk.Button(janela, text="Buscar Ativo", width=25).pack(pady=5)
tk.Button(janela, text="Atualizar Ativo", width=25).pack(pady=5)
tk.Button(janela, text="Remover Ativo", width=25).pack(pady=5)
tk.Button(janela, text="Vulnerabilidades", width=25).pack(pady=5)

janela.mainloop()