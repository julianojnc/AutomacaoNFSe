from tkinter import *
import threading
import time
from core.verificadores.inicial import verificacao_inicial
from core.esp_tempo import tempo

# Função que executa o loop para que o codigo fique sempre rodando
def tarefa_demorada():
    while not parar_execucao:
        print("Executando tarefa...")
        verificacao_inicial()
        tempo()
        time.sleep(1)
    print("Tarefa interrompida!")
    btn_parar.config(text="⏹️Parado", background='green')
    texto_status.config(text="Tarefa Interrompida!", foreground='green')

def parar():
    global parar_execucao
    parar_execucao = True
    btn_iniciar.config(text="▶️Iniciar", background='white')
    btn_parar.config(text="⏹️Parando...", background='red')
    texto_status.config(text="Espere o loop ser finalizado.", foreground='red')
    print("Solicitação de parada recebida.")

def iniciar():
    global parar_execucao, thread
    parar_execucao = False  # Permite que a thread execute novamente
    btn_iniciar.config(text="▶️Iniciado", background='green')
    btn_parar.config(text="⏹️Parar", background='white')
    texto_status.config(text="Programa em Execução!", foreground='green')
    # Cria uma NOVA thread (a anterior foi finalizada)
    thread = threading.Thread(target=tarefa_demorada)
    thread.daemon = True
    thread.start()
    print("Tarefa iniciada!")

# Configuração da janela
janela = Tk()
janela.title("NFSe")
janela.geometry("250x80+1100+610")

# Configurações de fixação
janela.attributes('-topmost', True)  # Sempre no topo
janela.resizable(False, False)       # Não redimensionável

parar_execucao = False
thread = None  # Inicializa a variável thread

# Botão para iniciar
btn_iniciar = Button(janela, text="▶️Iniciar", width=10, font=(12), command=iniciar)
btn_iniciar.grid(column=0, row=0, padx=10, pady=10)

# Botão para parar
btn_parar = Button(janela, text="⏹️Parar", width=10, font=(12), command=parar)
btn_parar.grid(column=1, row=0, padx=10, pady=10)

texto_status = Label(janela, text="Inicialize o programa!", font=(12), foreground='blue')
texto_status.grid(column=0, row=1, columnspan=2, padx=5, pady=0)

janela.mainloop()