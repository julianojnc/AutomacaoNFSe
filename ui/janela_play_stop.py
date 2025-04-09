from tkinter import *
import threading
import time
from core.verificadores.inicial import verificacao_inicial
from ui.janela_config import JanelaConfig
from core.esp_tempo import tempo
from ui.status_manager import StatusManager

class JanelaPlayStop:
    def __init__(self, master, status_manager):
        self.master = master
        self.status_manager = status_manager
        self.master.title("NFSe - Controle")
        self.master.attributes('-topmost', True)
        self.master.resizable(False, False)
        
        self.parar_execucao = False
        self.thread = None
        self.em_execucao = False
        
        self.criar_widgets()
        self.master.protocol("WM_DELETE_WINDOW", self.ao_fechar)
        self.status_manager.update_status("Pronto para Inciar o Sistema")
    
    def criar_widgets(self):
        # Botões
        self.btn_iniciar = Button(self.master, text="▶️ Iniciar", width=10, 
                                font=12, command=self.iniciar)
        self.btn_iniciar.grid(column=0, row=0, padx=10, pady=10)
        
        self.btn_parar = Button(self.master, text="⏹️ Parar", width=10, 
                              font=12, command=self.parar, state=DISABLED)
        self.btn_parar.grid(column=1, row=0, padx=10, pady=10)

        self.btn_config = Button(self.master, text="⚙️ Config", width=10, 
                              font=12, command=self.abrir_config)
        self.btn_config.grid(column=1, row=1, padx=10, pady=10)
    
    def tarefa_demorada(self):
        while not self.parar_execucao and self.em_execucao:
            print("Executando tarefa...")
            verificacao_inicial()
            tempo()
            
            for i in range(10):  # Verifica a cada 0.1s se deve parar
                if self.parar_execucao or not self.em_execucao:
                    break
                time.sleep(0.1)
        
        print("Tarefa finalizada!")
        self.master.after(0, self.atualizar_ui_parado)
    
    def iniciar(self):
        if self.em_execucao:
            return
            
        self.em_execucao = True
        self.parar_execucao = False
        self.btn_iniciar.config(text="▶️ Executando", bg='green', state=DISABLED)
        self.btn_config.config(state=DISABLED)
        self.btn_parar.config(text="⏹️ Parar", bg='white', state=NORMAL)
        self.status_manager.update_status("Executando...")
        
        self.thread = threading.Thread(target=self.tarefa_demorada)
        self.thread.daemon = True
        self.thread.start()
    
    def parar(self):
        self.parar_execucao = True
        self.btn_parar.config(text="⏹️ Parando...", bg='red', state=DISABLED)
        self.btn_config.config(state=DISABLED)
        self.status_manager.update_status("Parando o Sistema, espere finalizar o loop!")

    def abrir_config(self):
        # Cria uma nova janela de configuração
        janela_config = Toplevel(self.master)
        JanelaConfig(janela_config)
        # Centraliza a janela
        self.centralizar_janela(janela_config)
    
    def centralizar_janela(self, janela):
        janela.update_idletasks()
        width = janela.winfo_width()
        height = janela.winfo_height()
        x = (janela.winfo_screenwidth() // 2) - (width // 2)
        y = (janela.winfo_screenheight() // 2) - (height // 2)
        janela.geometry(f'+{x}+{y}')
    
    def atualizar_ui_parado(self):
        self.em_execucao = False
        self.btn_iniciar.config(text="▶️ Iniciar", bg='white', state=NORMAL)
        self.btn_config.config(state=NORMAL)
        self.btn_parar.config(text="⏹️ Parado", bg='white', state=DISABLED)
        self.status_manager.update_status("Pronto para Inciar o Sistema")
    
    def ao_fechar(self):
        self.parar_execucao = True
        if self.thread and self.thread.is_alive():
            self.thread.join(timeout=1)
        self.master.destroy()

# Inicia a aplicação
if __name__ == "__main__":
    JanelaPlayStop()
    