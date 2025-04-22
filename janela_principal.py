from tkinter import Tk, Toplevel
from ui.janela_play_stop import JanelaPlayStop
from ui.janela_data_certificado import JanelaCertificados
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

        # Janela Play/Stop (controle)
        janela_ps = Toplevel(self.root)
        JanelaPlayStop(janela_ps, self.status_manager)
        janela_ps.geometry("220x80+0+580")

        # Janela de status
        janela_status = Toplevel(self.root)
        JanelaStatus(janela_status, self.status_manager)
        janela_status.geometry("220x100+0+445")

        # Janela Data Vencimento
        janela_dv = Toplevel(self.root)
        JanelaCertificados(janela_dv)
        janela_dv.geometry("310x350+1050+340")

if __name__ == "__main__":
    JanelaPrincipal()