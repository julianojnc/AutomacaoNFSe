from tkinter import *
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
import json
from pathlib import Path
from itertools import cycle

def ler_dados_certificados():
    caminho_json = Path('C:/ParametrosNFSe/dados_automacao.json')
    certificados = {
        "3D": "dt-venc-cert-dig-3d",
        "Aura": "dt-venc-cert-dig-aura",
        "Camburi": "dt-venc-cert-dig-camburi",
        "CasaAcqua": "dt-venc-cert-dig-casaacqua",
        "Facom": "dt-venc-cert-dig-facom",
        "Flexu": "dt-venc-cert-dig-flexu",
        "Matrix": "dt-venc-cert-dig-matrix"
    }
    
    try:
        with open(caminho_json, 'r') as arquivo:
            dados = json.load(arquivo)
            return {nome: dados.get(chave, '2025-04-08') for nome, chave in certificados.items()}
    except (FileNotFoundError, json.JSONDecodeError):
        return {nome: '2025-04-08' for nome in certificados.keys()}

class JanelaCertificados:
    def __init__(self, master):
        self.master = master
        self.master.title("Vencimento de Certificados Digitais")
        self.master.attributes('-topmost', True)
        self.master.resizable(False, False)
        
        self.certificados = {}
        self.ultimos_dados = None
        
        self.criar_widgets()
        self.atualizar_todos_certificados()
        self.iniciar_verificacao_periodica()
    
    def criar_widgets(self):
        # Título
        Label(self.master, text="Status dos Certificados Digitais", 
             font=('Arial', 12, 'bold')).grid(row=0, column=0, columnspan=2, pady=1)
        
        # Frame principal com scrollbar
        self.canvas = Canvas(self.master)
        self.frame_status = Frame(self.canvas)
        
        self.frame_status.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )
        
        self.canvas.create_window((0, 0), window=self.frame_status, anchor="nw")
        self.canvas.configure(yscrollcommand=self)
        
        self.canvas.grid(row=1, column=0, sticky="nsew")
        
        # Botão de atualização
        btn_atualizar = Button(self.master, text="Atualizar", 
                             command=self.forcar_atualizacao)
        btn_atualizar.grid(row=2, column=0, columnspan=2, pady=5)
        
        # Configuração de grid para expansão
        self.master.grid_rowconfigure(1, weight=1)
        self.master.grid_columnconfigure(0, weight=1)
    
    def iniciar_verificacao_periodica(self):
        self.verificar_atualizacoes()
    
    def verificar_atualizacoes(self):
        dados_atuais = ler_dados_certificados()
        
        if dados_atuais != self.ultimos_dados:
            self.ultimos_dados = dados_atuais
            self.atualizar_todos_certificados()
        
        self.master.after(5000, self.verificar_atualizacoes)
    
    def forcar_atualizacao(self):
        dados_atuais = ler_dados_certificados()
        self.ultimos_dados = dados_atuais
        self.atualizar_todos_certificados()
    
    def atualizar_todos_certificados(self):
        color_text = ("white", "red")
        color_bg = ("red", "black")

        def flash_color(self, color_txt, color_bg):
            self.config(foreground = next(color_txt))
            self.config(bg = next(color_bg))
            self.after(500, flash_color, self, color_txt, color_bg)

        # Limpa o frame anterior
        for widget in self.frame_status.winfo_children():
            widget.destroy()
        
        dados = ler_dados_certificados()
        data_atual = date.today()
        
        for i, (nome, data_str) in enumerate(dados.items()):
            try:
                data_venc = datetime.strptime(data_str, '%Y-%m-%d').date()
                dias = (data_venc - data_atual).days
                
                # Frame para cada certificado
                frame_cert = Frame(self.frame_status, bd=1, relief=GROOVE, padx=5, pady=5)
                frame_cert.pack(fill=X, padx=5, pady=2)
                
                # Nome do certificado
                Label(frame_cert, text=nome, font=('Arial', 10, 'bold'), 
                     width=9, anchor='w').pack(side=LEFT)
                
                # Data de vencimento
                Label(frame_cert, text=data_venc.strftime('%d/%m/%Y'), 
                     font=('Arial', 10), width=7).pack(side=LEFT)
                
                # Dias restantes
                lbl_dias = Label(frame_cert, text=f"{dias} dias", 
                               font=('Arial', 10, 'bold'), width=8)
                lbl_dias.pack(side=LEFT)
                
                # Status
                if dias < 0:
                    lbl_status = Label(frame_cert, text="VENCIDO", 
                                     font=('Arial', 10, 'bold'),  width=7, fg='red')
                    lbl_dias.config(fg='red')
                    flash_color(lbl_status, cycle(color_text), cycle(color_bg))

                elif dias <= 7:
                    lbl_status = Label(frame_cert, text="URGENTE", 
                                     font=('Arial', 10, 'bold'), width=7, fg='red')
                    lbl_dias.config(fg='red')
                    flash_color(lbl_status, cycle(color_text), cycle(color_bg))

                elif dias <= 31:
                    lbl_status = Label(frame_cert, text="ATENÇÃO", 
                                     font=('Arial', 10, 'bold'), width=7, fg='orange')
                    lbl_dias.config(fg='orange')

                    color_text = ("white", "orange")
                    color_bg = ("orange", "black")
                    flash_color(lbl_status, cycle(color_text), cycle(color_bg))

                else:
                    lbl_status = Label(frame_cert, text="OK", 
                                     font=('Arial', 10, 'bold'), width=7, fg='green')
                    lbl_dias.config(fg='green')
                
                lbl_status.pack(side=LEFT, padx=(10,0))
                
            except ValueError:
                # Caso a data seja inválida
                frame_cert = Frame(self.frame_status, bd=1, relief=GROOVE, padx=5, pady=5)
                frame_cert.pack(fill=X, padx=5, pady=2)
                
                Label(frame_cert, text=nome, font=('Arial', 10, 'bold'), 
                     width=10, anchor='w').pack(side=LEFT)
                Label(frame_cert, text="Data inválida", fg='red').pack(side=LEFT)

if __name__ == "__main__":
    root = Tk()
    app = JanelaCertificados(root)
    root.mainloop()