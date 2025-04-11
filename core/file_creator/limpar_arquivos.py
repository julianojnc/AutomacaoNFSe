import os
import datetime

def limpar_nfse_no_horario():
    # Caminhos dos arquivos e pastas
    caminho_pasta_nfse = r"C:\Users\juliano.nascimento\Documents\NFSE"
    caminho_chaves = r"C:\ParametrosNFSe\chaves-nfse.txt"
    
    # Verifica se está no horário 00:00 - 01:00
    hora_atual = datetime.datetime.now().time()
    horario_limpeza = (datetime.time(9, 0) <= hora_atual <= datetime.time(10, 0))
    
    if horario_limpeza:
        print("Horário válido (00:00-01:00). Iniciando limpeza...")
        
        # Limpa a pasta NFSE excluindo os arquivos dentro da mesma
        if os.path.exists(caminho_pasta_nfse):
            for arquivo in os.listdir(caminho_pasta_nfse):
                caminho_arquivo = os.path.join(caminho_pasta_nfse, arquivo)
                try:
                    if os.path.isfile(caminho_arquivo):
                        os.remove(caminho_arquivo)
                        print(f"Arquivo removido: {caminho_arquivo}")
                except Exception as e:
                    print(f"Erro ao remover {caminho_arquivo}: {e}")
        else:
            print(f"Pasta não encontrada: {caminho_pasta_nfse}")
        
        # Limpa o conteúdo do arquivo chaves-nfse.txt
        if os.path.exists(caminho_chaves):
            try:
                with open(caminho_chaves, "w", encoding="utf-8") as arquivo:
                    arquivo.write("")  # Esvazia o arquivo
                print(f"Conteúdo do arquivo {caminho_chaves} foi limpo.")
            except Exception as e:
                print(f"Erro ao limpar {caminho_chaves}: {e}")
        else:
            print(f"Arquivo não encontrado: {caminho_chaves}")
    else:
        print("Fora do horário de limpeza (00:00-01:00). Nada foi alterado.")

if __name__ == "__main__":
    limpar_nfse_no_horario()  # Executa uma vez