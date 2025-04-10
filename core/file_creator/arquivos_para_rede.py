import os
import shutil
from datetime import datetime

def enviar_arquivos_para_rede():
    # Caminhos de origem e destino
    origem = os.path.join(os.path.expanduser("~"), "Documents", "NFSE")
    destino_base = r"\\facom\FACOM-SEDE\PUBLICA\CPD\BackupsNFSe"
    
    # Obtém a data atual
    data_atual = datetime.now()
    ano = data_atual.strftime("%Y")
    mes = data_atual.strftime("%m")
    dia_mes_ano = data_atual.strftime("%d-%m-%Y")  # Formato DIA-MÊS-ANO
    
    # Cria o caminho completo: BackupsNFSe/ANO/MÊS/DIA-MÊS-ANO
    destino_final = os.path.join(destino_base, ano, mes, dia_mes_ano)

    # Verifica se a pasta de origem existe
    if not os.path.exists(origem):
        print(f'[ERRO] Pasta de origem não encontrada: "{origem}"')
        return

    try:
        # Cria a estrutura de pastas (ano/mês/dia-mês-ano) se não existir
        os.makedirs(destino_final, exist_ok=True)
        print(f'[INFO] Pasta de destino criada: "{destino_final}"')
    except PermissionError:
        print(f'[ERRO] Sem permissão para criar pasta em "{destino_final}"')
        return
    except Exception as e:
        print(f'[ERRO] Falha ao acessar rede: {e}')
        return

    # Copia os arquivos para o destino
    arquivos_copiados = []
    for arquivo in os.listdir(origem):
        caminho_origem = os.path.join(origem, arquivo)
        caminho_destino = os.path.join(destino_final, arquivo)

        if os.path.isfile(caminho_origem):
            try:
                shutil.copy2(caminho_origem, caminho_destino)
                arquivos_copiados.append(arquivo)
                print(f'[OK] Copiado: {arquivo}')
            except Exception as e:
                print(f'[ERRO] Falha ao copiar {arquivo}: {e}')

    # Relatório final
    print('\n' + '='*50)
    if arquivos_copiados:
        print(f'\n[RESULTADO] Backup concluído com sucesso!')
        print(f'Destino: {destino_final}')
        print(f'Total de arquivos copiados: {len(arquivos_copiados)}')
    else:
        print('[AVISO] Nenhum arquivo foi copiado')
    print('='*50)

if __name__ == "__main__":
    print('\n' + '='*50)
    print('INICIANDO BACKUP DE ARQUIVOS NFSe'.center(50))
    print('='*50 + '\n')
    enviar_arquivos_para_rede()