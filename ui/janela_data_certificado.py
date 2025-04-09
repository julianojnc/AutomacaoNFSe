from tkinter import *
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
import json
from pathlib import Path

def ler_data_vencimento():
    caminho_json = Path('C:/PrametrosAutomacaoNfse/dados_automacao.json')
    
    try:
        with open(caminho_json, 'r') as arquivo:
            dados = json.load(arquivo)
            return dados.get('dt-venc-cert-dig')  # Retorna a data do JSON
    except (FileNotFoundError, json.JSONDecodeError):
        return '2025-04-08'  # Valor padrão se o arquivo não existir ou for inválido

class JanelaDataVencimento:
    def __init__(self, master, data_vencimento=None):
        self.master = master
        self.master.title("Vencimento Certificado")
        self.master.attributes('-topmost', True)
        self.master.resizable(False, False)

        if data_vencimento is None:
            data_vencimento = ler_data_vencimento()
        
        self.data_venc = datetime.strptime(data_vencimento, '%Y-%m-%d').date()
        
        self.criar_widgets()
        self.atualizar_status()
    
    def criar_widgets(self):
        # Título
        Label(self.master, text="Status do Certificado Digital", 
             font=('Arial', 14, 'bold')).grid(row=0, column=0, pady=5)
        
        # Frame principal
        self.frame_status = Frame(self.master)
        self.frame_status.grid(row=1, column=0, padx=10, pady=5)
        
        # Botão de atualização
        btn_atualizar = Button(self.master, text="Atualizar", 
                             command=self.atualizar_status)
        btn_atualizar.grid(row=2, column=0, pady=5)
    
    def atualizar_status(self):
        # Limpa o frame anterior
        for widget in self.frame_status.winfo_children():
            widget.destroy()
        
        data_atual = date.today()
        delta = relativedelta(self.data_venc, data_atual)
        dias = (self.data_venc - data_atual).days
        
        # Mostra sempre os dias restantes
        Label(self.frame_status, text=f"Dias restantes: {dias}",
             font=('Arial', 12), fg='blue').pack(anchor='w')
        
        # Adiciona mensagem de status conforme a situação
        if dias < 0:
            Label(self.frame_status, text="CERTIFICADO VENCIDO!",
                 font=('Arial', 12, 'bold'), fg='red').pack(anchor='w')
        elif dias <= 31:  # Considera 1 mês como 31 dias
            if delta.months == 1 and delta.days >= 0:
                Label(self.frame_status, text="ALERTA: 1 mês para o vencimento!",
                     font=('Arial', 12, 'bold'), fg='red').pack(anchor='w')
            else:
                Label(self.frame_status, text=f"ATENÇÃO: Faltam {dias} dias!",
                     font=('Arial', 12, 'bold'), fg='red').pack(anchor='w')

# Inicia a aplicação
if __name__ == "__main__":
    # Pode alterar a data passando como parâmetro:
    # JanelaDataVencimento('2025-06-30')
    JanelaDataVencimento()