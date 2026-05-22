import csv
import os
# Escrever

def inicializar_arquivos():
    if not os.path.exists("ativos.csv"):
        with open("ativos.csv", "w") as arquivo:
            writer = csv.writer(arquivo)
            writer.writerow(["id", "nome", "responsavel", "setor", "localização", "tipo"])  # cabeçalho

def carregar_ativos():
    with open("ativos.csv", "r") as arquivo:
        ativos = {}
        reader = csv.DictReader(arquivo)
        for linha in reader:
           ativos[int(linha["id"])] = linha
        return ativos    
    

def salvar_ativos(id, nome, responsavel, setor, localizacao, tipo):
    with open("ativos.csv", "a") as arquivo:
        writer = csv.writer(arquivo) 
        writer.writerow([id, nome, responsavel, setor, localizacao, tipo])

def remover_ativos(id):
    ativos = carregar_ativos()
    ativos_filtrados = []
    for linha in ativos.values():
        if int(linha["id"]) != id:
            ativos_filtrados.append(linha)      
    with open("ativos.csv", "w") as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow(["id", "nome", "responsavel", "setor", "localizacao", "tipo"])
        for ativo in ativos_filtrados:
            writer.writerow([ativo["id"], ativo["nome"], ativo["responsavel"], ativo["setor"], ativo["localizacao"], ativo["tipo"]])

def atualizar_ativo(id, nome, responsavel, setor, localizacao, tipo):
    ativos = carregar_ativos()
    ativos_atualizado = []
    for linha in ativos.values():
        if int(linha["id"]) != id:
            ativos_atualizado.append(linha)
        else:
            ativos_atualizado.append({       # substitui pelos novos dados
            "id": id,
            "nome": nome,
            "responsavel": responsavel,
            "setor": setor,
            "localizacao": localizacao,
            "tipo": tipo
            })
    with open("ativos.csv", "w") as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow(["id", "nome", "responsavel", "setor", "localizacao", "tipo"])
        for ativo in ativos_atualizado:
            writer.writerow([ativo["id"], ativo["nome"], ativo["responsavel"], ativo["setor"], ativo["localizacao"], ativo["tipo"]])

def buscar_ativo(id):
    ativos = carregar_ativos()
    if id in ativos:
        return ativos[id]
    else:
        return None
    
def buscar_ativo_por_nome(nome):
    ativos = carregar_ativos()
    for ativo in ativos.values():
        if ativo["nome"] == nome:
            return ativo
    return None

def inicializar_vulnerabilidades():
    if not os.path.exists("vulnerabilidades.csv"):
        with open("vulnerabilidades.csv", "w") as arquivos:
            writer =csv.writer(arquivos)
            writer.writerow(["id_vuln", "id_ativo", "descricao", "categoria", "severidade", "status"])

def salvar_vulnerabilidade(id_vuln, id_ativo, descricao, categoria, severidade, status):
    with open("vulnerabilidades.csv", "a") as arquivo:
        writer = csv.writer(arquivo) 
        writer.writerow([id_vuln, id_ativo, descricao, categoria, severidade, status])

def carregar_vulnerabilidades(id_ativo):
    with open("vulnerabilidades.csv", "r") as arquivo:
        vulnerabilidades = {}
        reader = csv.DictReader(arquivo)
        for linha in reader:
            if int(linha["id_ativo"]) == id_ativo:
                vulnerabilidades[int(linha["id_vuln"])] = linha
        return vulnerabilidades    