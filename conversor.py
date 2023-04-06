import customtkinter as ctk
from PIL import Image, ImageTk
import json
import requests


def enviar():
    """
    Recebe a entrada da Entrybox e Combobox, pesquisa as moedas requisitadas,
    converte o valor e insere numa Label para mostrar ao usuario.
    """
    valor = float(entrada.get())
    de_moeda = moeda_de.get()
    para_moeda = moeda_para.get()

    cambio = requests.get('https://api.exchangerate-api.com/v4/latest/{}'.format(de_moeda))
    valores = json.loads(cambio.text)
    for i, y in valores['rates'].items():
        if i == para_moeda:
            conversao = valor * float(y)
            saida.configure(text=str(conversao))


def listar():
    """
    Recolhe todas as moedas e insere na lista moedas.
    """
    listagem = requests.get('https://api.exchangerate-api.com/v4/latest/BRL')
    dados = json.loads(listagem.text)
    for i in dados['rates']:
        moedas.append(i)


moedas = []
janela = ctk.CTk()
janela.title("Conversor de moedas")
janela.geometry("500x500")
janela.resizable(False, False)
janela.config(bg="green")

img = Image.open('moeda.png')#insira o caminho para a imagem
img = img.resize((130,130))
img = ImageTk.PhotoImage(img)

topo = ctk.CTkLabel(janela, text="Conversor de moedas", font=('Times', 40),
                     height=90, width=500, bg_color='green', text_color='black')
topo.pack()

imagem = ctk.CTkLabel(janela, image=img, text="", bg_color="green")
imagem.place(x=180, y=70)

listar()
moeda_de = ctk.CTkComboBox(janela, width=120, justify='center', bg_color='green',
                            font=('Arial', 12), values=moedas)
moeda_de.place(x=20, y=320)


entrada = ctk.CTkEntry(janela, width=120, bg_color='green')
entrada.place(x=20, y=380)

moeda_para = ctk.CTkComboBox(janela, width=120, justify='center', bg_color='green',
                              font=('Arial', 12), values=moedas)
moeda_para.place(x=360, y=320)

saida = ctk.CTkLabel(janela, text='', width=120, bg_color='white', font=('', 12), text_color='black')
saida.place(x=360, y=380)

botao = ctk.CTkButton(janela, text="Converter", width=10, font=('Times', 20),
                       fg_color='black', bg_color='green', command=enviar)
botao.place(x=205, y=320)

janela.mainloop()

