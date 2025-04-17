import os
import shutil
import logging
from datetime import datetime

def mover_notas_canceladas():
    # Caminhos importantes
    caminho_chaves = r"C:\ParametrosNFSe\chaves-nfse.txt"
    caminho_backup_base = r"\\facom\FACOM-SEDE\PUBLICA\CPD\BackupsNFSe"
    
    # Lista das 7 pastas principais
    pastas_principais = ["3D", "Aura", "Camburi", "CasaAcqua", "Facom", "Flexu", "Matrix"]
    
    # Obtém a data atual no formato DIA-MÊS-ANO
    data_atual = datetime.now().strftime("%d-%m-%Y")
    ano = datetime.now().strftime("%Y")
    mes = datetime.now().strftime("%m")
    
    # Verifica se o arquivo de chaves existe
    if not os.path.exists(caminho_chaves):
        logging.error(f"Arquivo de chaves não encontrado: {caminho_chaves}")
        return
    
    # Lê o arquivo de chaves
    with open(caminho_chaves, 'r') as arquivo:
        linhas = arquivo.readlines()
    
    # Organiza as chaves canceladas por pasta
    chaves_canceladas_por_pasta = {pasta: [] for pasta in pastas_principais}
    
    for linha in linhas:
        linha = linha.strip()
        if linha.endswith("-CANCELADA"):
            # Extrai o nome da pasta e a chave pura
            for pasta in pastas_principais:
                if linha.startswith(f"{pasta} OK-"):
                    chave_pura = linha.replace(f"{pasta} OK-", "").replace("-CANCELADA", "")
                    chaves_canceladas_por_pasta[pasta].append(chave_pura)
                    break
    
    total_movidos = 0
    
    # Processa cada pasta separadamente
    for pasta in pastas_principais:
        chaves_canceladas = chaves_canceladas_por_pasta[pasta]
        
        if not chaves_canceladas:
            logging.info(f"[{pasta}] Nenhuma nota cancelada encontrada.")
            continue
        
        # Monta o caminho completo do backup do dia para esta pasta
        caminho_backup_dia = os.path.join(caminho_backup_base, pasta, ano, mes, data_atual)
        
        # Verifica se o backup do dia existe para esta pasta
        if not os.path.exists(caminho_backup_dia):
            logging.warning(f"[{pasta}] Pasta de backup do dia não encontrada: {caminho_backup_dia}")
            continue
        
        # Cria a pasta Canceladas se não existir
        caminho_canceladas = os.path.join(caminho_backup_dia, "Canceladas")
        os.makedirs(caminho_canceladas, exist_ok=True)
        logging.info(f"[{pasta}] Pasta 'Canceladas' criada em: {caminho_canceladas}")
        
        # Move os arquivos correspondentes às chaves canceladas
        movidos_pasta = 0
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
                        logging.info(f"[{pasta}] MOVENDO {arquivo} -> Canceladas/")
                        movidos_pasta += 1
                    except Exception as e:
                        logging.error(f"[{pasta}] Erro ao mover {arquivo}: {e}")
        
        total_movidos += movidos_pasta
        logging.info(f"[{pasta}] Total de arquivos movidos: {movidos_pasta}")
    
    logging.info(f"\n[RESULTADO FINAL] Total geral de arquivos movidos para 'Canceladas': {total_movidos}")

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('mover_canceladas.log'),
            logging.StreamHandler()
        ]
    )
    
    logging.info("\n" + "="*50)
    logging.info("PROCESSANDO NOTAS CANCELADAS".center(50))
    logging.info("="*50 + "\n")
    mover_notas_canceladas()