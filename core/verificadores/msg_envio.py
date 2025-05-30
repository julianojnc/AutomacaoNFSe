import pyautogui
import logging

def msg_envio():
    resultado = None
    # Verifica o retorno das mensagens ao enviar o email
    while resultado is None:
        try:
            # Verifica Existência de mensagem Erro ao Enviar Email
            if pyautogui.locateOnScreen('core/imgs/ErroEnviarEmail.png'):
                resultado = "erro"
                pyautogui.press('esc')
                pyautogui.click(1191,117)
            else:
                logging.info("Imagem ErroEnviarEmail não encontrada")
        except:
            try:
                # Verifica a existência de mensagem Envio com Sucesso
                if pyautogui.locateOnScreen('core/imgs/EmailEnviado.png'):
                    resultado = "sucesso"
                    pyautogui.press('esc')
                else:
                    logging.info("Imagem EmailEnviado não encontrada")
            except:
                logging.info('Aguardando mensagem...')
        
    return resultado