from tkinter import *

class JanelaStatus:
    def __init__(self, master, status_manager):
        self.master = master
        self.status_manager = status_manager
        self.master.title("Status do Sistema")
        self.master.geometry("250x50")
        self.master.attributes('-topmost', True)
        self.master.resizable(False, False)
        
        self.label_status = Label(self.master, wraplength='250', text="", fg='blue', font=('Arial', 15, 'bold'))
        self.label_status.pack(pady=20)
        
        # Registra esta janela como observadora
        self.status_manager.add_observer(self.atualizar_status)
        self.atualizar_status(self.status_manager.status)
    
    def atualizar_status(self, status):
        self.label_status.config(text=status)
        # Muda a cor conforme o status
        if "Executando..." in status:
            self.label_status.config(fg='green')
        elif "Parando o Sistema, espere finalizar o loop!" in status:
            self.label_status.config(fg='red')
        elif "Pronto para Inciar o Sistema" in status:
            self.label_status.config(fg='blue')