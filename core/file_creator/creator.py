import os
import json

# Gera os arquivos de configuração do sistema em c:
def criar_estrutura_inicial():
    pasta_principal = r'C:\ParametrosNFSe'
    pasta_chaves = os.path.join(pasta_principal, 'Chaves')
    pasta_log = os.path.join(pasta_principal, 'Logs')
    arquivo_json = os.path.join(pasta_principal, 'dados_automacao.json')
    arquivo_txt = os.path.join(pasta_principal, 'chaves-nfse.txt')

    # Criar pasta principal e arquivos se não existirem
    if not os.path.exists(pasta_principal):
        os.makedirs(pasta_principal)

    if not os.path.exists(pasta_log):
        os.makedirs(pasta_log)

    if not os.path.exists(arquivo_json):
        with open(arquivo_json, 'w', encoding='utf-8') as f:
            json.dump({
                "email": "",
                "assunto": "",
                "assunto-cancelada": "",
                "dt-venc-cert-dig": "2025-08-04"
            }, f, indent=4)

    if not os.path.exists(arquivo_txt):
        with open(arquivo_txt, 'w', encoding='utf-8') as f:
            f.write('')

    # Criar pasta "Chaves" se não existir
    if not os.path.exists(pasta_chaves):
        os.makedirs(pasta_chaves)
