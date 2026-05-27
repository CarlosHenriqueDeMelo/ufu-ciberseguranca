import tkinter as tk
from database import *
from enums import *

inicializar_arquivos()
inicializar_vulnerabilidades()

janela = tk.Tk()
janela.title("Sistema de Inventário TI")
janela.geometry("400x300")

def abrir_cadastrar():
    janela_cadastro = tk.Toplevel(janela)
    janela_cadastro.title("Cadastrar Ativo")
    janela_cadastro.geometry("350x360")

    tk.Label(janela_cadastro, text="ID:").pack()
    campo_id = tk.Entry(janela_cadastro)
    campo_id.pack()

    tk.Label(janela_cadastro, text="Nome:").pack()
    campo_nome = tk.Entry(janela_cadastro)
    campo_nome.pack()

    tk.Label(janela_cadastro, text="Responsável:").pack()
    campo_responsavel = tk.Entry(janela_cadastro)
    campo_responsavel.pack()

    tk.Label(janela_cadastro, text="Setor:").pack()
    campo_setor = tk.Entry(janela_cadastro)
    campo_setor.pack()

    tk.Label(janela_cadastro, text="Tipo:").pack()
    tipo_var = tk.StringVar()
    tipo_var.set(TipoAtivo.notebook.name)

    opcoes_tipo = [tipo.name for tipo in TipoAtivo]

    menu_tipo = tk.OptionMenu(
        janela_cadastro,
        tipo_var,
        *opcoes_tipo
    )
    menu_tipo.pack()
    def salvar():
        try:
            id = int(campo_id.get())

            if buscar_ativo(id) is not None:
                tk.Label(janela_cadastro, text="ID já cadastrado!", fg="red").pack()
                return

            nome = campo_nome.get().strip()
            responsavel = campo_responsavel.get().strip()
            setor = campo_setor.get().strip()
            tipo = tipo_var.get()

            # verifica se algum campo está vazio
            if not nome or not responsavel or not setor:
                tk.Label(janela_cadastro, text="Preencha todos os campos!", fg="red").pack()
                return

            salvar_ativos(id, nome, responsavel, setor, tipo)
            janela_cadastro.destroy()

        except ValueError:
            tk.Label(janela_cadastro, text="Digite um ID válido!", fg="red").pack()
        
    tk.Button(janela_cadastro, text="Salvar", command=salvar).pack(pady=10)
    
def abrir_buscar():
    janela_buscar = tk.Toplevel(janela)
    janela_buscar.title("Buscar Ativo")
    janela_buscar.geometry("350x350")
    
    tk.Label(janela_buscar, text="Digite o ID ou Nome:").pack()
    campo_busca = tk.Entry(janela_buscar)
    campo_busca.pack()
    
    resultado = tk.Label(janela_buscar, text="")
    resultado.pack(pady=10)

    def buscar():
        busca = campo_busca.get()
        if busca.isdigit():
            ativo = buscar_ativo(int(busca))
        else:
            ativo = buscar_ativo_por_nome(busca)

        if ativo is None:
            resultado.config(text="Ativo não encontrado!")
        else:
            texto = f"""
            ID: {ativo['id']}
            Nome: {ativo['nome']}
            Responsável: {ativo['responsavel']}
            Setor: {ativo['setor']}
            Tipo: {ativo['tipo']}
            """
            resultado.config(text=texto)
    tk.Button(janela_buscar, text="Buscar", command=buscar).pack(pady=5) 
                 
def abrir_atualizar():
    janela_atualizar = tk.Toplevel(janela)
    janela_atualizar.title("Atualizar Ativo")
    janela_atualizar.geometry("350x450")

    tk.Label(janela_atualizar, text="Digite o ID:").pack()
    campo_id = tk.Entry(janela_atualizar)
    campo_id.pack()

    ativo_encontrado = None

    def buscar():
        nonlocal ativo_encontrado
        try:
            id_ativo = int(campo_id.get())
            ativo = buscar_ativo(id_ativo)
            if ativo is None:
                resultado.config(text="Ativo não encontrado!", fg="red")
                return
            ativo_encontrado = ativo
            campo_nome.delete(0, tk.END)
            campo_nome.insert(0, ativo["nome"])
            campo_responsavel.delete(0, tk.END)
            campo_responsavel.insert(0, ativo["responsavel"])
            campo_setor.delete(0, tk.END)
            campo_setor.insert(0, ativo["setor"])
            tipo_var.set(ativo["tipo"])
            resultado.config(text="Ativo carregado!", fg="green")
        except ValueError:
            resultado.config(text="Digite um ID válido!", fg="red")

    tk.Button(janela_atualizar, text="Buscar", command=buscar).pack(pady=5)

    resultado = tk.Label(janela_atualizar, text="")
    resultado.pack()

    tk.Label(janela_atualizar, text="Nome:").pack()
    campo_nome = tk.Entry(janela_atualizar)
    campo_nome.pack()

    tk.Label(janela_atualizar, text="Responsável:").pack()
    campo_responsavel = tk.Entry(janela_atualizar)
    campo_responsavel.pack()

    tk.Label(janela_atualizar, text="Setor:").pack()
    campo_setor = tk.Entry(janela_atualizar)
    campo_setor.pack()

    tk.Label(janela_atualizar, text="Tipo:").pack()
    tipo_var = tk.StringVar()
    tipo_var.set(TipoAtivo.notebook.name)
    opcoes_tipo = [tipo.name for tipo in TipoAtivo]
    menu_tipo = tk.OptionMenu(janela_atualizar, tipo_var, *opcoes_tipo)
    menu_tipo.pack()

    def salvar():
        try:
            id_ativo = int(campo_id.get())
            if ativo_encontrado is None:
                resultado.config(text="Busque um ativo primeiro!", fg="red")
                return
            nome = campo_nome.get().strip()
            responsavel = campo_responsavel.get().strip()
            setor = campo_setor.get().strip()
            tipo = tipo_var.get()
            if not nome or not responsavel or not setor:
                resultado.config(text="Preencha todos os campos!", fg="red")
                return
            atualizar_ativo(id_ativo, nome, responsavel, setor, tipo)
            resultado.config(text="Ativo atualizado com sucesso!", fg="green")
            janela_atualizar.after(1000, janela_atualizar.destroy)
        except ValueError:
            resultado.config(text="Digite um ID válido!", fg="red")

    tk.Button(janela_atualizar, text="Salvar Alterações", command=salvar).pack(pady=10)
      
def remover_ativo():
    janela_remover = tk.Toplevel(janela)
    janela_remover.title("Remover Ativo")
    janela_remover.geometry("350x350")

    tk.Label(
        janela_remover,
        text="Digite o ID:"
    ).pack()

    campo_removerID = tk.Entry(janela_remover)
    campo_removerID.pack()

    resultado = tk.Label(
        janela_remover,
        text=""
    )
    resultado.pack()

    def remover():
        try:
            id = int(campo_removerID.get())
            ativo = buscar_ativo(id)

            if ativo is None:
                resultado.config(
                    text="Ativo não encontrado"
                )
            else:
                remover_ativos(id)

                resultado.config(
                    text="Ativo removido!",
                    fg="green"
                )

                janela_remover.after(
                    1000,
                    janela_remover.destroy
                )

        except ValueError:
            resultado.config(
                text="Digite um ID válido!"
            )

    tk.Button(
        janela_remover,
        text="Remover",
        command=remover
    ).pack(pady=10)
    
def abrir_vulns():
    janela_vuln = tk.Toplevel(janela)
    janela_vuln.title("Vulnerabilidades")
    janela_vuln.geometry("350x350")
    
    def abrir_adicionar_vuln():
        janela_vuln = tk.Toplevel(janela)
        janela_vuln.title("Adicionar Vulnerabilidade")
        janela_vuln.geometry("350x350")
        
        tk.Label(janela_vuln, text="ID do Ativo:").pack()
        campo_ID = tk.Entry(janela_vuln)
        campo_ID.pack()
        
        tk.Label(janela_vuln, text="Descrição:").pack()
        campo_desc = tk.Entry(janela_vuln)
        campo_desc.pack()
        
        tk.Label(janela_vuln, text="Categoria:").pack()
        campo_categoria = tk.Entry(janela_vuln)
        campo_categoria.pack()
        
        tk.Label(janela_vuln, text="Severidade:").pack()
        campo_severidade = tk.Entry(janela_vuln)
        campo_severidade.pack()
        
        tk.Label(janela_vuln, text="Status:").pack()
        campo_status = tk.Entry(janela_vuln)
        campo_status.pack()
        
        def salvar():
            try:
                id_ativo = int(campo_ID.get())

                desc = campo_desc.get()
                categoria = campo_categoria.get()
                severidade = campo_severidade.get()
                status = campo_status.get()

                salvar_vulnerabilidade(
                    id_ativo,
                    desc,
                    categoria,
                    severidade,
                    status
                )

                janela_vuln.destroy()

            except ValueError:
                tk.Label(
                    janela_vuln,
                    text="Digite IDs válidos!",
                    fg="red"
                ).pack()
                
        tk.Button(janela_vuln, text="Salvar", command=salvar).pack(pady=10)
                
    tk.Button(janela_vuln, text="Adicionar Vulnerabilidade", width=25, command=abrir_adicionar_vuln).pack(pady=5)
            
            
    def abrir_visualizar_vuln():
        janela_buscar_vuln = tk.Toplevel(janela)
        janela_buscar_vuln.title("Visualizar Vulnerabilidades")
        janela_buscar_vuln.geometry("350x400")

        tk.Label(janela_buscar_vuln, text="Digite o ID do Ativo:").pack()
        campo_busca_vuln = tk.Entry(janela_buscar_vuln)
        campo_busca_vuln.pack()

        resultado = tk.Label(janela_buscar_vuln, text="")
        resultado.pack(pady=10)

        def buscar_vuln():
            id_ativo = int(campo_busca_vuln.get())
            vulns = carregar_vulnerabilidades(id_ativo)
            if not vulns:
                resultado.config(text="Nenhuma vulnerabilidade encontrada.")
            else:
                texto = ""
                for v in vulns.values():
                    texto += f"\nDescrição: {v['descricao']}\nSeveridade: {v['severidade']}\nStatus: {v['status']}\n"
                resultado.config(text=texto)

        tk.Button(janela_buscar_vuln, text="Buscar", command=buscar_vuln).pack(pady=5)
    tk.Button(janela_vuln, text="Visualizar Vulnerabilidades", width=25, command=abrir_visualizar_vuln).pack(pady=5)
        
tk.Label(janela, text="Sistema de Inventário de TI", font=("Arial", 14)).pack(pady=10)

tk.Button(janela, text="Cadastrar Ativo", width=25, command=abrir_cadastrar).pack(pady=5)
tk.Button(janela, text="Buscar Ativo", width=25, command=abrir_buscar).pack(pady=5)
tk.Button(janela, text="Atualizar Ativo", width=25, command=abrir_atualizar).pack(pady=5)
tk.Button(janela, text="Remover Ativo", width=25, command=remover_ativo).pack(pady=5)
tk.Button(janela, text="Vulnerabilidades", width=25, command=abrir_vulns).pack(pady=5)

    #ARRUMAR ID (NN PODE USAR O MESMO ID)
    #ARRUMAR ATUALIZAR ATIVO
janela.mainloop()