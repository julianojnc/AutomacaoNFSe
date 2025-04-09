import pyautogui
import pyperclip
import time
from core.arquivo_chaves import arquivo
from core.validador_chave import validar_chave

# Função para capturar todas as NFSe
def captura_nfse():
    time.sleep(2)
    # Copiando todos os dados das NFSe
    pyautogui.hotkey('ctrl', 'c')
    todas_nfse = pyperclip.paste()

    # Passando para a função arquivo todas as NFSe e recebendo a quantidade das mesmas
    quantidade = arquivo(todas_nfse)
    # Clique para baixo para selecionar a primeira nota da lista
    pyautogui.press('down')

    i = 0
    # Loop responsável por verificar nota por nota
    while i < quantidade:
        time.sleep(1)
        # Copia a chave
        pyautogui.hotkey('ctrl', 'c')
        # Fecha a mensagem de copiado com sucesso
        pyautogui.press('esc')
        # Valor copiado em uma variavel
        chave = pyperclip.paste().strip()

        from core.verificadores.nfse import nfse_cancelada
        isCancelada = nfse_cancelada()

        # Passando o valor copiado para a função validar_chave
        validar_chave(chave, isCancelada)

        time.sleep(1)
        # Clica para baixo para selecionar a próxima nota
        pyautogui.press('down')

        i += 1 

    # # Finalizando o loop o timer será executado novamente
    # from core.esp_tempo import tempo
    # tempo()