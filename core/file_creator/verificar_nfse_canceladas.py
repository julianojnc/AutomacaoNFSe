import os
import shutil
import logging
from datetime import datetime

def mover_notas_canceladas():
    # Caminhos importantes
    caminho_chaves = r"C:\ParametrosNFSe\chaves-nfse.txt"
    caminho_backup_base = r"\\facom\FACOM-SEDE\PUBLICA\CPD\BackupsNFSe"
    
    # Obtém a data atual no formato DIA-MÊS-ANO
    data_atual = datetime.now().strftime("%d-%m-%Y")
    
    # Monta o caminho completo do backup do dia
    ano = datetime.now().strftime("%Y")
    mes = datetime.now().strftime("%m")
    caminho_backup_dia = os.path.join(caminho_backup_base, ano, mes, data_atual)
    
    # Verifica se o arquivo de chaves existe
    if not os.path.exists(caminho_chaves):
        logging.error("Arquivo de chaves não encontrado:", caminho_chaves)
        return
    
    # Verifica se o backup do dia existe
    if not os.path.exists(caminho_backup_dia):
        logging.warning("Pasta de backup do dia não encontrada:", caminho_backup_dia)
        return
    
    # Lê o arquivo de chaves
    with open(caminho_chaves, 'r') as arquivo:
        linhas = arquivo.readlines()
    
    # Filtra apenas as chaves canceladas
    chaves_canceladas = []
    for linha in linhas:
        linha = linha.strip()
        if linha.endswith("-CANCELADA"):
            # Remove o prefixo "OK-" e o sufixo "-CANCELADA" para obter a chave pura
            chave_pura = linha.replace("OK-", "").replace("-CANCELADA", "")
            chaves_canceladas.append(chave_pura)
    
    # Se não houver chaves canceladas, encerra
    if not chaves_canceladas:
        logging.info("Nenhuma nota cancelada encontrada no arquivo de chaves.")
        return
    
    # Cria a pasta Canceladas se não existir
    caminho_canceladas = os.path.join(caminho_backup_dia, "Canceladas")
    os.makedirs(caminho_canceladas, exist_ok=True)
    logging.info(f"Pasta 'Canceladas' criada em: {caminho_canceladas}")
    
    # Move os arquivos correspondentes às chaves canceladas
    total_movidos = 0
    for chave in chaves_canceladas:
        # Procura por arquivos que contenham a chave no nome
        for arquivo in os.listdir(caminho_backup_dia):
            # Ignora a própria pasta Canceladas e diretórios
            if arquivo == "Canceladas" or os.path.isdir(os.path.join(caminho_backup_dia, arquivo)):
                continue
            
            if chave in arquivo:
                origem = os.path.join(caminho_backup_dia, arquivo)
                destino = os.path.join(caminho_canceladas, arquivo)
                
                try:
                    shutil.move(origem, destino)
                    logging.info(f"[MOVENDO] {arquivo} -> Canceladas/")
                    total_movidos += 1
                except Exception as e:
                    logging.error(f"Erro ao mover {arquivo}: {e}")
    
    logging.info(f"\n[RESULTADO] Total de arquivos movidos para 'Canceladas': {total_movidos}")

if __name__ == "__main__":
    logging.info("\n" + "="*50)
    logging.info("PROCESSANDO NOTAS CANCELADAS".center(50))
    logging.info("="*50 + "\n")
    mover_notas_canceladas()