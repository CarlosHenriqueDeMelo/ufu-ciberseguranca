from enum import Enum

class TipoAtivo(Enum):
    notebook = 1
    celular = 2
    computador = 3
    internet_publica = 4
    internet_privada = 5

class SeveridadeVuln(Enum):
    baixa = 1
    media = 2
    alta = 3
    critica = 4

class StatusVuln(Enum):
    aberta = 1
    tratamento = 2
    corrigida = 3
    aceita_como_risco = 4
