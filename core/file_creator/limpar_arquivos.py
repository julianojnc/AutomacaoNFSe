import os
import datetime
import logging

def limpar_nfse_log_no_horario():
    # Caminhos dos arquivos e pastas
    caminho_pasta_nfse = r"C:\Users\juliano.nascimento\Documents\NFSE"
    caminho_chaves = r"C:\ParametrosNFSe\chaves-nfse.txt"
    caminho_log = r"C:\ParametrosNFSe\Logs\info.log"  # Novo caminho para o log
    
    # Verifica se está no horário 00:00 - 01:00
    hora_atual = datetime.datetime.now().time()
    horario_limpeza = (datetime.time(0, 0) <= hora_atual <= datetime.time(1, 0))
    
    if horario_limpeza:
        logging.info("Horário válido (00:00-01:00). Iniciando limpeza...")
        
        # Limpa a pasta NFSE (arquivos XML/DANFE)
        if os.path.exists(caminho_pasta_nfse):
            for arquivo in os.listdir(caminho_pasta_nfse):
                caminho_arquivo = os.path.join(caminho_pasta_nfse, arquivo)
                try:
                    if os.path.isfile(caminho_arquivo):
                        os.remove(caminho_arquivo)
                        logging.info(f"Arquivo removido: {caminho_arquivo}")
                except Exception as e:
                    logging.error(f"Erro ao remover {caminho_arquivo}: {e}")
        else:
            logging.error(f"Pasta não encontrada: {caminho_pasta_nfse}")
        
        # Limpa o arquivo de chaves
        if os.path.exists(caminho_chaves):
            try:
                with open(caminho_chaves, "w", encoding="utf-8") as arquivo:
                    arquivo.write("")  # Esvazia o arquivo
                logging.info(f"Conteúdo do arquivo {caminho_chaves} foi limpo.")
            except Exception as e:
                logging.error(f"Erro ao limpar {caminho_chaves}: {e}")
        else:
            logging.error(f"Arquivo não encontrado: {caminho_chaves}")
            
        # Limpa o arquivo de log
        if os.path.exists(caminho_log):
            try:
                with open(caminho_log, "w", encoding="utf-8") as arquivo:
                    arquivo.write("")  # Esvazia o arquivo de log
                logging.info(f"Conteúdo do arquivo {caminho_log} foi limpo.")
            except Exception as e:
                logging.error(f"Erro ao limpar {caminho_log}: {e}")
        else:
            logging.warning(f"Arquivo de log não encontrado: {caminho_log}")
            
    else:
        logging.info("Fora do horário permitido (00:00-01:00). Nenhum arquivo foi removido.")

if __name__ == "__main__":
    # Configura o logging para escrever no arquivo e mostrar no console
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(r"C:\ParametrosNFSe\Logs\info.log"),
            logging.StreamHandler()
        ]
    )
    
    limpar_nfse_log_no_horario()