import pyautogui
import logging
import time
pyautogui.PAUSE = 0.5

# Procura a existência do botão para documentos e faz o processo para salvar na pasta NFSe
def documents():
    resultado = None
    # Verifica o retorno de documento
    while resultado is None:
        try:
            # Verifica Existência de Documentos na tela
            if pyautogui.locateOnScreen('core/imgs/Documents.png'):
                # Clica sobre Documentos, após digita N para selecionar a pasta NFSE
                # Após Enter para salvar e Enter novamente para fechar a mensagem de sucesso
                pyautogui.click(pyautogui.locateOnScreen('core/imgs/Documents.png'))
                pyautogui.press('n')
                pyautogui.press('enter')
                time.sleep(1)
                pyautogui.press('enter')

                # Retorna um valor para finalizar o loop
                resultado = 'doc'
            else:
                logging.info("Imagem Documents não encontrada")
        except:
            try:
                # Verifica a existência de Documentos já selecionado
                if pyautogui.locateOnScreen('core/imgs/DocumentsGray.png'):
                    # Clica sobre Documentos, após digita N para selecionar a pasta NFSE
                    # Após Enter para salvar e Enter novamente para fechar a mensagem de sucesso
                    pyautogui.click(pyautogui.locateOnScreen('core/imgs/DocumentsGray.png'))
                    pyautogui.press('n')
                    pyautogui.press('enter')
                    time.sleep(1)
                    pyautogui.press('enter')

                    # Retorna um valor para finalizar o loop
                    resultado = 'docselect'
                else:
                    logging.info("Imagem DocumentsGray não encontrada")
            except:
                try:
                # Verifica a existência de NFSe já selecionado
                    if pyautogui.locateOnScreen('core/imgs/NFSeGray.png'):
                        # Clica sobre NFSe após Enter para salvar e Enter novamente para fechar a mensagem de sucesso
                        pyautogui.click(pyautogui.locateOnScreen('core/imgs/NFSeGray.png'))
                        pyautogui.press('enter')
                        time.sleep(1)
                        pyautogui.press('enter')

                        # Retorna um valor para finalizar o loop
                        resultado = 'nfseselect'
                    else:
                        logging.info("Imagem NFSeGray não encontrada")
                except:
                    print('Aguardando mensagem...')

# Procura a existência do botão para exportação dos arquivos e após chama a função para salvar em documentos
def save_file(isCancelada):
        
    if isCancelada is not None:
        pyautogui.click(pyautogui.locateOnScreen('core/imgs/SelecionarArquivosEmail.png'))
        pyautogui.press('down')
        pyautogui.press('up')
        pyautogui.press('space')

    # Verifica se Exportar Xml e PDF estão na tela
    location_xml_pdf = None
    # Enquanto XML/PDF não estiver na tela o loop é executado infinitamente
    while (location_xml_pdf == None):
        # Tente encontrar XML/PDF e clicar nele
        try:
            location_xml_pdf = pyautogui.locateOnScreen('core/imgs/ExportarXmlPdf.png')
            time.sleep(0.5)
            # Clica sobre o botão
            pyautogui.click(pyautogui.locateOnScreen('core/imgs/ExportarXmlPdf.png'))
            # Chama a função documents para salvar o arquivo na pasta
            documents()
        except Exception as e:
            logging.info('Procurando Botão Exportar XML e PDF... ',e)