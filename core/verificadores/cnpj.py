import pyautogui
import logging
from core.verificadores.inicial import verificacao_inicial

# cnpj recebe o nome da empresa e adiciona ao nome do arquivo que deve ser clicado
def cnpj(cnpj_name):
    try:
        # Tenta encontrar e clicar na imagem referente a empresa passada como parametro
        location = pyautogui.locateOnScreen(f'core/imgs/{cnpj_name}.png')
        if location:
            pyautogui.click(location)
            # Verificação inicial dispara os demais códigos do sistema
            verificacao_inicial(cnpj_name)
            return f"Encontrado e clicado: {cnpj_name}"
    except:
        # Caso a empresa já esteja selecionada é feita essa verificação
        # A mudança é somente o nome do arquivo referente a empresa
        try:
            location = pyautogui.locateOnScreen(f'core/imgs/{cnpj_name}Blue.png')
            if location:
                pyautogui.click(location)
                verificacao_inicial(cnpj_name)
                return f"Encontrado e clicado: {cnpj_name}"
        except Exception as e:
            logging.error(f"Erro ao procurar {cnpj_name}: {e}")
        return None  # Retorna None se não encontrar ou se der erro

# Buscar Cnpj e clicar no mesmo
def busca_cnpj():
    # Nome das empresas
    cnpjs = ["3D", "Aura", "Camburi", "CasaAcqua", "Facom", "Flexu", "Matrix"]
    # Para cada cnpj da lista é executada a função cnpj passando o nome da empresa
    for cnpj_name in cnpjs:
        resultado = cnpj(cnpj_name)
        logging.info(resultado if resultado else f"{cnpj_name} não encontrado.")
