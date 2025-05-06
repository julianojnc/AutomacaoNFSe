import pyautogui
import pyperclip
import logging
import time
import re
from datetime import datetime

def capturar_data_nota():
     # Verifica se botão xml está disponível na tela
    location_button_xml_open = None
    i = 0
    while i < 1:
        try:
            # Clica no botão xml quando aberto
            location_button_xml_open = pyautogui.locateOnScreen('core/imgs/ButtonXml.png')
            pyautogui.click(location_button_xml_open)
            time.sleep(0.5)
        except: 
            try:
                # Clica no botão xml quando fechado
                location_button_xml_open = pyautogui.locateOnScreen('core/imgs/ButtonXmlClose.png')
                pyautogui.click(location_button_xml_open)
            except Exception as e:
                logging.info("Procurando NFe's Abertas... ",e)
        i += 1
    
    # Move o mouse para abaixo do botão xml para poder fazer o scroll da tela
    pyautogui.moveTo(224,365)
    # Scroll da tela para aparecer o campo de data do xml
    pyautogui.scroll(-1500)
    time.sleep(1)
    # Clicado três vezes em cima do campo para poder copiar todos os dados referente a data de emissao
    pyautogui.click(pyautogui.doubleClick(pyautogui.locateOnScreen('core/imgs/DataEmissao.png')))
    # Copiado os dados
    pyautogui.hotkey('ctrl', 'c')
    # Passado para uma variavel os dados copiados
    data_emissao = pyperclip.paste()
    data_formatada = formatar_data(data_emissao)
    
    return data_formatada
    
# Formatando a data
def formatar_data(xml_string):
    try:
        # Encontra o padrão de data no XML
        match = re.search(r'<dhEmi>(\d{4}-\d{2}-\d{2})', xml_string)
        if match:
            data_iso = match.group(1)
            # Converte para objeto datetime e formata
            data_obj = datetime.strptime(data_iso, "%Y-%m-%d")
            return data_obj.strftime("%d/%m/%Y")
            
    except Exception as e:
        logging.error(f"Erro ao formatar data: {e}")
    
    return "Data não encontrada"