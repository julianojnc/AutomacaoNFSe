import re

# Salva as notas no arquivo
def arquivo(nfse):
    try:
        # Lê as chaves existentes, removendo todos os prefixos/sufixos
        with open('C:/ParametrosNFSe/chaves-nfse.txt', 'r') as f:
            chaves_existentes = set()
            for line in f:
                line = line.strip()
                # Remove OK- no início e -CANCELADA no final, se existirem
                chave_pura = line.replace("OK-", "").replace("-CANCELADA", "")
                chaves_existentes.add(chave_pura)
    except FileNotFoundError:
        chaves_existentes = set()

    # Extrai todas as chaves de 50 dígitos do texto
    chaves_novas = re.findall(r'\d{50}', nfse)
    
    # Filtra apenas chaves que não existem no arquivo (em qualquer formato)
    chaves_para_adicionar = [chave for chave in chaves_novas if chave not in chaves_existentes]
    
    # Adiciona as novas chaves no formato limpo (sem prefixos)
    if chaves_para_adicionar:
        with open('C:/ParametrosNFSe/chaves-nfse.txt', 'a') as arq:
            for chave in chaves_para_adicionar:
                arq.write(chave + '\n')  # Grava no formato original, sem prefixos
    
    return len(chaves_novas)