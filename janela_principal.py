from tkinter import Tk, Toplevel
from ui.janela_play_stop import JanelaPlayStop
from ui.janela_data_certificado import JanelaDataVencimento
from ui.janela_status import JanelaStatus
from ui.status_manager import StatusManager

class JanelaPrincipal:
    def __init__(self):
        # Janela principal (invisível)
        self.root = Tk()
        self.root.withdraw()

        # Cria o gerenciador de status compartilhado
        self.status_manager = StatusManager()
        
        # Inicia ambas as janelas
        self.iniciar_janelas()
        
        self.root.mainloop()
    
    def iniciar_janelas(self):

        # Janela Data Vencimento
        janela_dv = Toplevel(self.root)
        JanelaDataVencimento(janela_dv)
        janela_dv.geometry("280x100+1075+310")

        # Janela de status
        janela_status = Toplevel(self.root)
        JanelaStatus(janela_status, self.status_manager)
        janela_status.geometry("280x100+1075+445")

        # Janela Play/Stop (controle)
        janela_ps = Toplevel(self.root)
        JanelaPlayStop(janela_ps, self.status_manager)
        janela_ps.geometry("250x100+1090+580")

if __name__ == "__main__":
    JanelaPrincipal()