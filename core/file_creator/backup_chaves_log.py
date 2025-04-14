import os
import shutil
import logging
from datetime import datetime

def fazer_backup_diario():
    # Configurações de caminhos
    pasta_principal = r'C:\ParametrosNFSe'
    arquivo_chaves = os.path.join(pasta_principal, 'chaves-nfse.txt')
    pasta_chaves = os.path.join(pasta_principal, 'Chaves')
    pasta_logs = os.path.join(pasta_principal, 'Logs')
    arquivo_log = os.path.join(pasta_logs, 'info.log')
    pasta_bkp_log = os.path.join(pasta_logs, 'BKP_LOG')
    
    # Data atual para nomear os backups
    data_hoje = datetime.now().strftime('%Y-%m-%d')
    
    # 1. Backup do arquivo chaves-nfse.txt
    if os.path.exists(arquivo_chaves) and os.path.getsize(arquivo_chaves) > 0:
        # Garante que a pasta Chaves existe
        os.makedirs(pasta_chaves, exist_ok=True)
        
        # Lê o conteúdo atual
        with open(arquivo_chaves, 'r', encoding='utf-8') as f:
            conteudo_atual = f.read()
        
        nome_copia_chaves = f'chave-{data_hoje}.txt'
        caminho_copia_chaves = os.path.join(pasta_chaves, nome_copia_chaves)
        
        # Verifica se precisa atualizar o backup
        if not os.path.exists(caminho_copia_chaves) or \
           conteudo_atual != open(caminho_copia_chaves, 'r', encoding='utf-8').read():
            with open(caminho_copia_chaves, 'w', encoding='utf-8') as f:
                f.write(conteudo_atual)
            logging.info(f'Backup de chaves atualizado: {nome_copia_chaves}')
    
    # 2. Backup do arquivo info.log
    if os.path.exists(arquivo_log) and os.path.getsize(arquivo_log) > 0:
        # Garante que a pasta BKP_LOG existe
        os.makedirs(pasta_bkp_log, exist_ok=True)
        
        nome_copia_log = f'info-{data_hoje}.log'
        caminho_copia_log = os.path.join(pasta_bkp_log, nome_copia_log)
        
        # Se já existe um backup de hoje, adiciona um sufixo com horário
        if os.path.exists(caminho_copia_log):
            hora_atual = datetime.now().strftime('%H-%M-%S')
            nome_copia_log = f'info-{data_hoje}_{hora_atual}.log'
            caminho_copia_log = os.path.join(pasta_bkp_log, nome_copia_log)
        
        # Faz a cópia do arquivo de log
        shutil.copy2(arquivo_log, caminho_copia_log)
        logging.info(f'Backup de log criado: {nome_copia_log}')
        
        # Limpa o arquivo de log original após o backup
        open(arquivo_log, 'w').close()

if __name__ == "__main__":
    # Configuração básica do logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(os.path.join(r'C:\ParametrosNFSe\Logs', 'info.log')),
            logging.StreamHandler()
        ]
    )
    
    try:
        fazer_backup_diario()
    except Exception as e:
        logging.error(f'Erro durante o backup: {str(e)}')