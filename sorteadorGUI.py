import tkinter as tk
from tkinter import ttk, messagebox
import random

def selecionar_questoes(numero_total, numero_selecionado):
    indices_selecionados = random.sample(range(1, numero_total + 1), numero_selecionado)
    indices_selecionados.sort()
    return indices_selecionados

def executar_sorteador():
    try:
        numero_total_de_questoes = int(entrada_total_questoes.get())
        numero_de_questoes_selecionadas = int(entrada_questoes_selecionadas.get())

        questoes_selecionadas = selecionar_questoes(numero_total_de_questoes, numero_de_questoes_selecionadas)

        messagebox.showinfo("Questões Selecionadas", f"Questões selecionadas: {questoes_selecionadas}")

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira números inteiros válidos.")

# Configuração da GUI
root = tk.Tk()
root.title("Sorteador de Questões")

# Labels e Entradas
label_total_questoes = ttk.Label(root, text="Número total de questões:")
entrada_total_questoes = ttk.Entry(root)

label_questoes_selecionadas = ttk.Label(root, text="Número de questões a serem selecionadas:")
entrada_questoes_selecionadas = ttk.Entry(root)

# Botão para executar o sorteio
botao_sortear = ttk.Button(root, text="Sortear!", command=executar_sorteador)

# Layout usando o método grid
label_total_questoes.grid(row=0, column=0, sticky="e")
entrada_total_questoes.grid(row=0, column=1)
label_questoes_selecionadas.grid(row=1, column=0, sticky="e")
entrada_questoes_selecionadas.grid(row=1, column=1)
botao_sortear.grid(row=2, columnspan=2)

# Iniciar o loop da interface gráfica
root.mainloop()
