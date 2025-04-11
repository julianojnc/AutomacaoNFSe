from tkinter import *
import json
from pathlib import Path

class JanelaConfig:
    def __init__(self, master):
        self.master = master
        self.master.title("Configurações")
        self.master.geometry("400x200")
        self.master.resizable(False, False)
        
        self.caminho_json = Path('C:/ParametrosNFSe/dados_automacao.json')
        self.dados = self.carregar_configuracoes()
        
        self.criar_widgets()
    
    # Carrega os dados que estão dentro do json de configuração
    def carregar_configuracoes(self):
        try:
            with open(self.caminho_json, 'r') as arquivo:
                return json.load(arquivo)
        except (FileNotFoundError, json.JSONDecodeError):
            return {
                "email": "",
                "assunto": "",
                "assunto-cancelada": "",
                "dt-venc-cert-dig": ""
            }
    
    # Salva configurações alteradas
    def salvar_configuracoes(self):
        try:
            with open(self.caminho_json, 'w') as arquivo:
                json.dump(self.dados, arquivo, indent=4)
            return True
        except Exception as e:
            print(f"Erro ao salvar configurações: {e}")
            return False
    
    def criar_widgets(self):
        # Frame principal
        frame_principal = Frame(self.master, padx=10, pady=10)
        frame_principal.pack(fill=BOTH, expand=True)
        
        # Email
        Label(frame_principal, text="Email:").grid(row=0, column=0, sticky=W, pady=5)
        self.entry_email = Entry(frame_principal, width=40)
        self.entry_email.grid(row=0, column=1, pady=5)
        self.entry_email.insert(0, self.dados.get("email", ""))
        
        # Assunto normal
        Label(frame_principal, text="Assunto NFSe:").grid(row=1, column=0, sticky=W, pady=5)
        self.entry_assunto = Entry(frame_principal, width=40)
        self.entry_assunto.grid(row=1, column=1, pady=5)
        self.entry_assunto.insert(0, self.dados.get("assunto", ""))
        
        # Assunto cancelada
        Label(frame_principal, text="Assunto Cancelada:").grid(row=2, column=0, sticky=W, pady=5)
        self.entry_assunto_cancelada = Entry(frame_principal, width=40)
        self.entry_assunto_cancelada.grid(row=2, column=1, pady=5)
        self.entry_assunto_cancelada.insert(0, self.dados.get("assunto-cancelada", ""))
        
        # Data vencimento
        Label(frame_principal, text="Data Venc. Cert:").grid(row=3, column=0, sticky=W, pady=5)
        self.entry_data_venc = Entry(frame_principal, width=40)
        self.entry_data_venc.grid(row=3, column=1, pady=5)
        self.entry_data_venc.insert(0, self.dados.get("dt-venc-cert-dig", ""))
        
        # Botões
        frame_botoes = Frame(frame_principal)
        frame_botoes.grid(row=4, column=0, columnspan=2, pady=15)
        
        btn_salvar = Button(frame_botoes, text="Salvar", command=self.salvar)
        btn_salvar.pack(side=LEFT, padx=10)
        
        btn_cancelar = Button(frame_botoes, text="Cancelar", command=self.master.destroy)
        btn_cancelar.pack(side=LEFT, padx=10)
    
    def salvar(self):
        self.dados = {
            "email": self.entry_email.get(),
            "assunto": self.entry_assunto.get(),
            "assunto-cancelada": self.entry_assunto_cancelada.get(),
            "dt-venc-cert-dig": self.entry_data_venc.get()
        }
        
        if self.salvar_configuracoes():
            self.master.destroy()