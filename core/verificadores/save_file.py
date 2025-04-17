import pyautogui
import logging
import time
pyautogui.PAUSE = 0.5

# Procura a existência do botão para documentos e faz o processo para salvar na pasta NFSe
def documents(cnpj_name):
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
                pasta_nfse(cnpj_name)

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
                    pasta_nfse(cnpj_name)

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
                        pasta_nfse(cnpj_name)

                        # Retorna um valor para finalizar o loop
                        resultado = 'nfseselect'
                    else:
                        logging.info("Imagem NFSeGray não encontrada")
                except:
                    print('Aguardando mensagem...')

# Selecioando a pasta onde será salvo os arquivos e separando por cnpj
def pasta_nfse(cnpj_name):

    # Loop para a verificação da pasta
    location = None

    # Enquanto location não tiver valor será executado novamente
    while location is None:
        try:
            # Se a localização da imagem com o mesmo nome do primeiro item da lista não for vazio
            # Será chamada a função selecionando_pasta que recebe o parametro cnpj_name e o primeiro item da lista
            # elif e else continua a mesma lógica só que para os demais itens da lista
            if pyautogui.locateOnScreen(f'core/imgs/NFSeBlue.png'):
                pyautogui.click(pyautogui.locateOnScreen(f'core/imgs/NFSeBlue.png'))
                pyautogui.write(cnpj_name)
                time.sleep(1)
                pyautogui.press('enter')                
                time.sleep(1)
                pyautogui.press('enter')
                location = 'encontrado'

        except Exception as e:
            logging.info('Procurando Pasta NFSe...',e)                

# Procura a existência do botão para exportação dos arquivos e após chama a função para salvar em documentos
def save_file(isCancelada, cnpj_name):
        
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
            documents(cnpj_name)
        except Exception as e:
            logging.info('Procurando Botão Exportar XML e PDF... ',e)