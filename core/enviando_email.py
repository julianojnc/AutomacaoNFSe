import pyautogui
import time
import json

pyautogui.PAUSE = 0.3

# Dados para envio de email lidos em um arquivo no c:
def arquivo_email():
    with open('C:/ParametrosNFSe/dados_automacao.json', 'r') as arquivo:
        dados = json.load(arquivo)
        arquivo.close()

        return dados

# Função de envio para o email clicando na nota selecionada no momento
def enviar_email(isCancelada, cnpj_name):
    # Dois cliques na nota selecionada no momento
    pyautogui.doubleClick(pyautogui.locateOnScreen('core/imgs/CampoParaClicarNFSe.png'))
    # Fecha o PopUp
    pyautogui.click(pyautogui.locateOnScreen('core/imgs/ClosePopUp.png'))
    time.sleep(2)
    
    # Data de Emissão da nota
    from core.verificadores.captura_data import capturar_data_nota
    data_emissao = capturar_data_nota()
    
    # Clica no botão de envio do email
    pyautogui.click(pyautogui.locateOnScreen('core/imgs/EnviarEmail.png'))

    # Salva o arquivo na NFSe dentro de documentos
    from core.verificadores.save_file import save_file
    save_file(isCancelada, cnpj_name)

    # Variável para armazenar o retorno da função arquivo_email
    assunto_email = arquivo_email()

    # Adiciona o Email que vai receber a nota
    pyautogui.click(476,192)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.write(assunto_email["email"])

    if isCancelada is not None:
        # Adiciona Assunto ao Email quando Cancelada a NFSe
        pyautogui.click(476,161)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.write(f"{cnpj_name} - {assunto_email["assunto-cancelada"]} - Emitida em: {data_emissao}")
    else:
        # Adiciona Assunto ao Email
        pyautogui.click(476,161)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.write(f"{cnpj_name} - {assunto_email["assunto"]} - Emitida em: {data_emissao}")

    # Clica no Botão para enviar
    pyautogui.click(pyautogui.locateOnScreen('core/imgs/EnviarEmailAgora.png'))
    
    from core.verificadores.msg_envio import msg_envio
    resultado = msg_envio()
    
    # Fecha a janela
    pyautogui.click(1179,120)

    return resultado