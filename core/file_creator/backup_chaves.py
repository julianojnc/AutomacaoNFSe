import os
import logging
from datetime import datetime

# Cria um novo arquivo txt dentro da pasta Chaves em C:/ParametrosNFSe
def fazer_backup_diario():
    pasta_principal = r'C:\ParametrosNFSe'
    arquivo_txt = os.path.join(pasta_principal, 'chaves-nfse.txt')  # Arquivo original
    pasta_chaves = os.path.join(pasta_principal, 'Chaves')          # Pasta de backups

    # Verifica se o arquivo original existe e tem conteúdo
    if not os.path.exists(arquivo_txt) or os.path.getsize(arquivo_txt) == 0:
        logging.info('Arquivo "chaves-nfse.txt" não existe ou está vazio. Nenhum backup foi criado.')
        return

    # Lê o conteúdo atual do arquivo
    with open(arquivo_txt, 'r', encoding='utf-8') as f:
        conteudo_atual = f.read()

    data_hoje = datetime.now().strftime('%Y-%m-%d')
    nome_copia = f'chave-{data_hoje}.txt'
    caminho_copia = os.path.join(pasta_chaves, nome_copia)

    # Se não existir um backup de hoje cria um novo
    if not os.path.exists(caminho_copia):
        with open(caminho_copia, 'w', encoding='utf-8') as f:
            f.write(conteudo_atual)
        logging.info(f'Novo backup criado: "{nome_copia}" em "{pasta_chaves}".')
    else:
        # Se já existir um backup de hoje compara o conteúdo
        with open(caminho_copia, 'r', encoding='utf-8') as f:
            conteudo_backup = f.read()

        if conteudo_atual == conteudo_backup:
            logging.info(f'O backup de hoje já está atualizado. Nenhuma alteração necessária.')
        else:
            # Se for diferente, atualiza o backup do dia
            with open(caminho_copia, 'w', encoding='utf-8') as f:
                f.write(conteudo_atual)
            logging.info(f'Backup atualizado: "{nome_copia}" em "{pasta_chaves}".')

# Exemplo de uso:
if __name__ == "__main__":
    fazer_backup_diario()