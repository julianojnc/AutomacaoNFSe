import os
import json

def file_creator():
    # Definir os caminhos
    pasta = r'C:\ParametrosNFSe'
    arquivo_json = os.path.join(pasta, 'dados_automacao.json')
    arquivo_txt = os.path.join(pasta, 'chaves-nfse.txt')

    # Verificar se a pasta não existe e criá-la
    if not os.path.exists(pasta):
        os.makedirs(pasta)
        print(f'Pasta "{pasta}" criada com sucesso.')

    # Verificar e criar o arquivo JSON se não existir
    if not os.path.exists(arquivo_json):
        dados_iniciais = {
            "email": "",
            "assunto": "",
            "assunto-cancelada": "",
            "dt-venc-cert-dig": ""
        }  # Dados iniciais vazios ou padrão
        with open(arquivo_json, 'w', encoding='utf-8') as f:
            json.dump(dados_iniciais, f, indent=4)
        print(f'Arquivo JSON "{arquivo_json}" criado com sucesso.')

    # Verificar e criar o arquivo TXT se não existir
    if not os.path.exists(arquivo_txt):
        with open(arquivo_txt, 'w', encoding='utf-8') as f:
            f.write('')  # Conteúdo inicial vazio ou padrão
        print(f'Arquivo TXT "{arquivo_txt}" criado com sucesso.')

    print('Verificação concluída.')