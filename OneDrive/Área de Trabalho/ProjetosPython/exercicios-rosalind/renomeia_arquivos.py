import os

def renomear_arquivos(diretorio, regra_renomeacao):

    arquivos = os.listdir(diretorio)
    for arquivo in arquivos:
        # Ignora subdiretórios
        if os.path.isfile(os.path.join(diretorio, arquivo)):
            novo_nome = regra_renomeacao(arquivo)
            caminho_antigo = os.path.join(diretorio, arquivo)
            caminho_novo = os.path.join(diretorio, novo_nome)

            os.rename(caminho_antigo, caminho_novo)
            print(f'Renomeado: {arquivo} -> {novo_nome}')


def adicionar_underline(nome_arquivo):
    lista = nome_arquivo.split(' ')
    return '_'.join(lista)

# Encontrando o diretório atual
current_directory = os.getcwd()
print(current_directory)

renomear_arquivos(current_directory, adicionar_underline)
