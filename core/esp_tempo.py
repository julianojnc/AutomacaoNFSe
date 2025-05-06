import time, sys
import pyautogui

# timer
def tempo():
    # Cronometro de 1 hora
    for i in range(0, 3600):
        sys.stdout.write("\r{}".format(i))
        sys.stdout.flush()
        time.sleep(1)
    
    # Depois de uma hora clicar no botao buscar na sefaz
    pyautogui.click(pyautogui.locateOnScreen('core/imgs/BuscarSefaz.png'))
    pyautogui.moveTo(500,500)
