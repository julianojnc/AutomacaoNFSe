from core.enviando_email import enviar_email

# Valida Chaves se já foram enviadas por email ou não
# Valida se a nota foi cancelada ou não
def validar_chave(chave, isCancelada, cnpj_name):
    with open('C:/ParametrosNFSe/chaves-nfse.txt', 'r') as arquivo:
        linhas = arquivo.readlines()

    modificado = False
    enviar_email_flag = False
    resultado = None  # Inicializa para evitar erro se não entrar no if

    for i in range(len(linhas)):
        linha_original = linhas[i]
        linha = linha_original.strip()
        
        # Remove todos os prefixos/sufixos para comparar apenas a chave pura
        chave_pura = linha.replace(f"{cnpj_name} OK-", "").replace("-CANCELADA", "").strip()

        if chave_pura == chave:
            # Processamento de cancelamento
            if isCancelada is not None:
                if not linha.endswith("-CANCELADA"):
                    # Se ainda não foi marcada como cancelada
                    enviar_email_flag = True
                    linhas[i] = f"{cnpj_name} OK-{chave_pura}-CANCELADA\n"
                    modificado = True
            # Processamento normal
            else:
                if not linha.startswith(f"{cnpj_name} OK-") and not linha.endswith("-CANCELADA"):
                    # Se é uma chave nova (sem marcações)
                    enviar_email_flag = True
                    linhas[i] = f"{cnpj_name} OK-{chave_pura}\n"
                    modificado = True

    # Executa o envio de email se necessário
    if enviar_email_flag:
        resultado = enviar_email(isCancelada, cnpj_name)

    # Salva as alterações no arquivo apenas se não houve erro no envio do email
    if modificado and resultado != "erro":
        with open('C:/ParametrosNFSe/chaves-nfse.txt', 'w') as arquivo:
            arquivo.writelines(linhas)
