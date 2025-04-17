import os
import shutil
import logging
from datetime import datetime
from core.file_creator.verificar_nfse_canceladas import mover_notas_canceladas

def enviar_arquivos_para_rede():
    # Caminhos bases
    origem_base = os.path.join(os.path.expanduser("~"), "Documents", "NFSE")
    destino_base = r"\\facom\FACOM-SEDE\PUBLICA\CPD\BackupsNFSe"
    
    # Obtém a data atual
    data_atual = datetime.now()
    ano = data_atual.strftime("%Y")
    mes = data_atual.strftime("%m")
    dia_mes_ano = data_atual.strftime("%d-%m-%Y")  # Formato DIA-MÊS-ANO

    # Lista das sub pastas
    pastas_principais = [
        "3D", "Aura", "Camburi", "CasaAcqua", 
        "Facom", "Flexu", "Matrix"
    ]

    total_arquivos_copiados = 0

    # Para cada subpasta dentro de pasta
    for pasta in pastas_principais:
        origem = os.path.join(origem_base, pasta)
        
        # Verifica se a pasta de origem existe
        if not os.path.exists(origem):
            logging.warning(f'Pasta de origem não encontrada: "{origem}"')
            continue

        # Verifica se a pasta está vazia
        if not os.listdir(origem):
            logging.info(f'[{pasta}] Pasta vazia - nenhuma ação necessária')
            continue

        # Cria o caminho completo: BackupsNFSe/PastaPrincipal/ANO/MÊS/DIA-MÊS-ANO
        destino_final = os.path.join(destino_base, pasta, ano, mes, dia_mes_ano)

        try:
            # Cria a estrutura de pastas apenas se houver arquivos para copiar
            os.makedirs(destino_final, exist_ok=True)
            logging.info(f'Pasta de destino criada: "{destino_final}"')
        except PermissionError:
            logging.error(f'Sem permissão para criar pasta em "{destino_final}"')
            continue
        except Exception as e:
            logging.error(f'Falha ao acessar rede para pasta {pasta}: {e}')
            continue

        # Copia os arquivos para o destino
        arquivos_copiados = []
        for arquivo in os.listdir(origem):
            caminho_origem = os.path.join(origem, arquivo)
            caminho_destino = os.path.join(destino_final, arquivo)

            if os.path.isfile(caminho_origem):
                try:
                    shutil.copy2(caminho_origem, caminho_destino)
                    arquivos_copiados.append(arquivo)
                    logging.info(f'[OK] Copiado {pasta}/{arquivo}')
                except Exception as e:
                    logging.error(f'Falha ao copiar {pasta}/{arquivo}: {e}')

        total_arquivos_copiados += len(arquivos_copiados)
        
        # Log por pasta
        if arquivos_copiados:
            logging.info(f'[{pasta}] Arquivos copiados: {len(arquivos_copiados)}')
        else:
            logging.info(f'[{pasta}] Nenhum arquivo copiado (pasta vazia após verificação)')

    # Relatório final
    logging.info('\n' + '='*50)
    if total_arquivos_copiados > 0:
        logging.info(f'\n[RESULTADO FINAL] Backup concluído!')
        logging.info(f'Total geral de arquivos copiados: {total_arquivos_copiados}')
    else:
        logging.info('[AVISO] Nenhum arquivo foi copiado em nenhuma pasta')
    logging.info('='*50)

    mover_notas_canceladas()

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('backup_nfse.log'),
            logging.StreamHandler()
        ]
    )
    
    logging.info('\n' + '='*50)
    logging.info('INICIANDO BACKUP DE ARQUIVOS NFSe'.center(50))
    logging.info('='*50 + '\n')
    enviar_arquivos_para_rede()