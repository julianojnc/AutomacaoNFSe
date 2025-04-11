import os
import json

# Gera os arquivos de configuração do sistema em c:
def criar_estrutura_inicial():
    pasta_principal = r'C:\ParametrosNFSe'
    pasta_chaves = os.path.join(pasta_principal, 'Chaves')
    arquivo_json = os.path.join(pasta_principal, 'dados_automacao.json')
    arquivo_txt = os.path.join(pasta_principal, 'chaves-nfse.txt')

    # Criar pasta principal e arquivos se não existirem
    if not os.path.exists(pasta_principal):
        os.makedirs(pasta_principal)
        print(f'Pasta "{pasta_principal}" criada com sucesso.')

    if not os.path.exists(arquivo_json):
        with open(arquivo_json, 'w', encoding='utf-8') as f:
            json.dump({}, f, indent=4)
        print(f'Arquivo JSON "{arquivo_json}" criado com sucesso.')

    if not os.path.exists(arquivo_txt):
        with open(arquivo_txt, 'w', encoding='utf-8') as f:
            f.write('')
        print(f'Arquivo TXT "{arquivo_txt}" criado com sucesso.')

    # Criar pasta "Chaves" se não existir
    if not os.path.exists(pasta_chaves):
        os.makedirs(pasta_chaves)
        print(f'Pasta "{pasta_chaves}" criada com sucesso.')
