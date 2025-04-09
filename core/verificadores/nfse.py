import time
import pyautogui

# Verifica a existencia de NFSe
def nfse():
    # Variável para o loop referente ao NFSe
    location_nfse = None
    i = 0
    # Enquanto i for menor que dois repita o loop
    while i < 1:
        # Tente encontrar NFSe e clicar duas vezes nele 
        try:
            location_nfse = pyautogui.locateOnScreen('core/imgs/NFSeListagem.png')
            time.sleep(1)
            pyautogui.click(pyautogui.locateOnScreen('core/imgs/NFSeListagem.png'))
            return location_nfse
        except Exception as e:
            print("Procurando NFSe's... ",e)
    
        return location_nfse
    i += 1

# Verificando a existência de NFSE's canceladas
def nfse_cancelada():
    # Variável para o loop referente ao NFSe canceladas
    location_nfse_cancelada = None
    i = 0
    # Enquanto i for menor que dois repita o loop
    while i < 1:
        try:
            location_nfse_cancelada = pyautogui.locateOnScreen('core/imgs/Cancelada.png')
        except Exception as e:
            print('Verificando se a nota está cancelada...',e)
        return location_nfse_cancelada

def verificar_nfse():
    # Verificando se os campos NFe e CTe estão abertos
    from core.verificadores.inicial import nfe, cte
    cte()
    nfe()

    # Amazenando o retorno da função
    location_nfse_return = nfse()

    # Se o retorno for vazio o timer será executado
    # Se não a captura das nfse será executada
    if location_nfse_return is None:
        from core.esp_tempo import tempo
        tempo()
    else:
        from core.utils.capturar_nfse import captura_nfse
        captura_nfse()
