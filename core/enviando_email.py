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
def enviar_email(isCancelada):
    # Dois cliques na nota selecionada no momento
    pyautogui.doubleClick(pyautogui.locateOnScreen('core/imgs/CampoParaClicarNFSe.png'))
    # Fecha o PopUp
    pyautogui.click(pyautogui.locateOnScreen('core/imgs/ClosePopUp.png'))

    # Salva o arquivo na NFSe dentro de documentos
    from core.verificadores.save_file import save_file
    save_file()

    time.sleep(2)
    # Clica no botão de envio do email
    pyautogui.click(pyautogui.locateOnScreen('core/imgs/EnviarEmail.png'))

    # Variável para armazenar o retorno da função arquivo_email
    assunto_email = arquivo_email()

    # Adiciona o Email que vai receber a nota
    pyautogui.click(476,192)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.write(assunto_email["email"])

    if isCancelada is not None:
        pyautogui.click(pyautogui.locateOnScreen('core/imgs/SelecionarArquivosEmail.png'))
        pyautogui.press('up')
        pyautogui.press('space')

        # Adiciona Assunto ao Email quando Cancelada a NFSe
        pyautogui.click(476,161)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.write(assunto_email["assunto-cancelada"])
    else:
        # Adiciona Assunto ao Email
        pyautogui.click(476,161)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.write(assunto_email["assunto"])

    # Clica no Botão para enviar
    pyautogui.click(pyautogui.locateOnScreen('core/imgs/EnviarEmailAgora.png'))
    
    from core.verificadores.msg_envio import msg_envio
    resultado = msg_envio()
    
    # Fecha a janela
    pyautogui.click(1179,120)

    return resultado