import time
import pyautogui
import logging
pyautogui.PAUSE = 0.3

# Verifica a existencia de Emitidos por Terceiros
def aba_emitidos_terceiros():
    resultado = None
    # Verifica se Emitido por terceiro não está selecionado
    while resultado is None:
        try:
            # Verifica Existência de Emitido por terceiros e clica nele
            if pyautogui.locateOnScreen('core/imgs/EmitidoPorTerceiros.png'):
                resultado = 'EmitidoTerceiro'
                pyautogui.click('core/imgs/EmitidoPorTerceiros.png')
            else:
                logging.info("Imagem EmitidoPorTerceiros não encontrada.")
        except:
            try:
                # Verifica Existência de Emitido por terceiros já selecionado e clica nele
                if pyautogui.locateOnScreen('core/imgs/EmitidoPorTerceirosSelecionado.png'):
                    resultado = 'EmitidoTerceiroSelecionado'
                    pyautogui.click('core/imgs/EmitidoPorTerceirosSelecionado.png')
                else:
                    logging.info("Imagem EmitidoPorTerceirosSelecionado não encontrada.")
            except:
                try:
                    # Verifica Existência de fechar mensagem da sefaz e clica nele
                    if pyautogui.locateOnScreen('core/imgs/CloseMsgBusca.png'):
                        resultado = 'FecharMsgBusca'
                        pyautogui.click('core/imgs/CloseMsgBusca.png')
                    else:
                        logging.info("Imagem CloseMsgBusca não encontrada.")
                except:
                    logging.info('Procurando fechar mensagem de busca da sefaz...')

# Verifica a existencia de TIPO
def tipo():
    # Verifica se Tipo já não está selecionado
    location_tipo_selecionado = None
    i = 0
    while i < 1:
        try:
            location_tipo_selecionado = pyautogui.locateOnScreen('core/imgs/TipoSelecionado.png')
            time.sleep(0.5)
        except Exception as e:
            logging.info('Procurando Tipo Aberto... ',e)
        i += 1
    
    if location_tipo_selecionado == None:
        # Variável para o loop referente ao TIPO
        location_tipo = None
        # Enquanto TIPO não estiver na tela o loop é executado infinitamente
        while (location_tipo == None):
            # Tente encontrar TIPO e clicar nele
            try:
                location_tipo = pyautogui.locateOnScreen('core/imgs/Tipo.png')
                time.sleep(0.5)
                pyautogui.click(pyautogui.locateOnScreen('core/imgs/Tipo.png'))
            except Exception as e:
                logging.info('Procurando Tipo... ',e)

# Verifica a existencia de CTe
def cte():
    # Verifica se CTe já não está aberto
    location_cte_open = None
    i = 0
    while i < 1:
        try:
            location_cte_open = pyautogui.locateOnScreen('core/imgs/CTeListagemOpen.png')
            time.sleep(0.5)
        except Exception as e:
            logging.info("Procurando CTe's Abertas... ",e)
        i += 1

    if location_cte_open != None:
        # Variável para o loop referente ao CTe
        location_cte = None
        i = 0
        # Enquanto i for menor que dois repita o loop
        while i < 1:
            # Tente encontrar CTe e clicar duas vezes nele 
            try:
                location_cte = pyautogui.locateOnScreen('core/imgs/CTeListagem.png')
                time.sleep(0.5)
                pyautogui.doubleClick(pyautogui.locateOnScreen('core/imgs/CTeListagem.png'))
            except Exception as e:
                logging.info("Procurando CTe's... ",e)
            return location_cte
        i += 1

# Verifica a existencia de NFe
def nfe():
    # Verifica se NFe já não está aberto
    location_nfe_open = None
    i = 0
    while i < 1:
        try:
            location_nfe_open = pyautogui.locateOnScreen('core/imgs/NFeListagemOpen.png')
            time.sleep(0.5)
        except Exception as e:
            logging.info("Procurando NFe's Abertas... ",e)
        i += 1

    if location_nfe_open != None:
        # Variável para o loop referente ao NFe
        location_nfe = None
        i = 0
        # Enquanto i for menor que dois repita o loop
        while i < 1:
            # Tente encontrar NFe e clicar duas vezes nele 
            try:
                location_nfe = pyautogui.locateOnScreen('core/imgs/NFeListagem.png')
                time.sleep(0.5)
                pyautogui.doubleClick(pyautogui.locateOnScreen('core/imgs/NFeListagem.png'))
            except Exception as e:
                logging.info("Procurando NFe's... ",e)
            return location_nfe
        i += 1

def verificacao_inicial():

    aba_emitidos_terceiros()

    tipo()

    cte()
    
    nfe()
    
    # Verificar se tem NFSe's e começar o processo de envio por email validando as chaves
    from core.verificadores.nfse import verificar_nfse
    verificar_nfse()