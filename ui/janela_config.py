from tkinter import *
import json
import logging
from pathlib import Path

class JanelaConfig:
    def __init__(self, master):
        self.master = master
        self.master.title("Configurações")
        self.master.geometry("450x400")
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
                "dt-venc-cert-dig-3d": "",
                "dt-venc-cert-dig-aura": "",
                "dt-venc-cert-dig-camburi": "",
                "dt-venc-cert-dig-casaacqua": "",
                "dt-venc-cert-dig-facom": "",
                "dt-venc-cert-dig-flexu": "",
                "dt-venc-cert-dig-matrix": ""
            }
    
    # Salva configurações alteradas
    def salvar_configuracoes(self):
        try:
            with open(self.caminho_json, 'w') as arquivo:
                json.dump(self.dados, arquivo, indent=4)
            return True
        except Exception as e:
            logging.error(f"Erro ao salvar configurações: {e}")
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
        
        # Data vencimento 3D
        Label(frame_principal, text="Data Venc. Cert. 3D:").grid(row=3, column=0, sticky=W, pady=5)
        self.entry_data_venc_3D = Entry(frame_principal, width=40)
        self.entry_data_venc_3D.grid(row=3, column=1, pady=5)
        self.entry_data_venc_3D.insert(0, self.dados.get("dt-venc-cert-dig-3d", ""))

        # Data vencimento Aura
        Label(frame_principal, text="Data Venc. Cert. Aura:").grid(row=4, column=0, sticky=W, pady=5)
        self.entry_data_venc_Aura = Entry(frame_principal, width=40)
        self.entry_data_venc_Aura.grid(row=4, column=1, pady=5)
        self.entry_data_venc_Aura.insert(0, self.dados.get("dt-venc-cert-dig-aura", ""))
        
        # Data vencimento Camburi
        Label(frame_principal, text="Data Venc. Cert. Camburi:").grid(row=5, column=0, sticky=W, pady=5)
        self.entry_data_venc_Camburi = Entry(frame_principal, width=40)
        self.entry_data_venc_Camburi.grid(row=5, column=1, pady=5)
        self.entry_data_venc_Camburi.insert(0, self.dados.get("dt-venc-cert-dig-camburi", ""))

        # Data vencimento CasaAcqua
        Label(frame_principal, text="Data Venc. Cert. CasaAcqua:").grid(row=6, column=0, sticky=W, pady=5)
        self.entry_data_venc_CasaAcqua = Entry(frame_principal, width=40)
        self.entry_data_venc_CasaAcqua.grid(row=6, column=1, pady=5)
        self.entry_data_venc_CasaAcqua.insert(0, self.dados.get("dt-venc-cert-dig-casaacqua", ""))

        # Data vencimento Facom
        Label(frame_principal, text="Data Venc. Cert. Facom:").grid(row=7, column=0, sticky=W, pady=5)
        self.entry_data_venc_Facom = Entry(frame_principal, width=40)
        self.entry_data_venc_Facom.grid(row=7, column=1, pady=5)
        self.entry_data_venc_Facom.insert(0, self.dados.get("dt-venc-cert-dig-facom", ""))

        # Data vencimento Flexu
        Label(frame_principal, text="Data Venc. Cert. Flexu:").grid(row=8, column=0, sticky=W, pady=5)
        self.entry_data_venc_Flexu = Entry(frame_principal, width=40)
        self.entry_data_venc_Flexu.grid(row=8, column=1, pady=5)
        self.entry_data_venc_Flexu.insert(0, self.dados.get("dt-venc-cert-dig-flexu", ""))

        # Data vencimento Matrix
        Label(frame_principal, text="Data Venc. Cert. Matrix:").grid(row=9, column=0, sticky=W, pady=5)
        self.entry_data_venc_Matrix = Entry(frame_principal, width=40)
        self.entry_data_venc_Matrix.grid(row=9, column=1, pady=5)
        self.entry_data_venc_Matrix.insert(0, self.dados.get("dt-venc-cert-dig-matrix", ""))

        # Botões
        frame_botoes = Frame(frame_principal)
        frame_botoes.grid(row=10, column=0, columnspan=2, pady=15)
        
        btn_salvar = Button(frame_botoes, text="Salvar", command=self.salvar)
        btn_salvar.pack(side=LEFT, padx=10)
        
        btn_cancelar = Button(frame_botoes, text="Cancelar", command=self.master.destroy)
        btn_cancelar.pack(side=LEFT, padx=10)
    
    def salvar(self):
        self.dados = {
            "email": self.entry_email.get(),
            "assunto": self.entry_assunto.get(),
            "assunto-cancelada": self.entry_assunto_cancelada.get(),
            "dt-venc-cert-dig-3d": self.entry_data_venc_3D.get(),
            "dt-venc-cert-dig-aura": self.entry_data_venc_Aura.get(),
            "dt-venc-cert-dig-camburi": self.entry_data_venc_Camburi.get(),
            "dt-venc-cert-dig-casaacqua": self.entry_data_venc_CasaAcqua.get(),
            "dt-venc-cert-dig-facom": self.entry_data_venc_Facom.get(),
            "dt-venc-cert-dig-flexu": self.entry_data_venc_Flexu.get(),
            "dt-venc-cert-dig-matrix": self.entry_data_venc_Matrix.get()
        }
        
        if self.salvar_configuracoes():
            self.master.destroy()