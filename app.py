import pyautogui
from core.file_creator.creator import criar_estrutura_inicial
from janela_principal import JanelaPrincipal
pyautogui.PAUSE = 0.3

# Abrir Programa Fiscal.io
pyautogui.hotkey('win', 'r')
pyautogui.write('C:\Program Files (x86)\Fiscal.io\MonitorDFe\Monitor.exe')
pyautogui.press('enter')

criar_estrutura_inicial()
JanelaPrincipal()