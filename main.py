from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# Import string
import string 
import random

# ---------------------------- Cores ----------------------------
corP = "#444466" # Cor preta
corB = "#feffff" # Cor branca
cor3 = "#f05a43" # Cor vermela

janela = Tk()
janela.title('Gerador de senhas')
janela.geometry('295x330')
janela.configure(bg = corP)

estilo = ttk.Style(janela)
estilo.theme_use('clam')

# Definição do frame de cima (largura, altura , etc.)
frame_cima = Frame(janela, width=295, height=50, bg=corP, pady=0, padx=0, relief='flat')
frame_cima.grid(row=0, column=0, sticky=NSEW)

# Definição do frame de baixo (largura, altura , etc.)
frame_baixo = Frame(janela, width=295, height=310, bg=corP, pady=0, padx=0, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NSEW)


#---------------------------- Desenvolvendo frame cima ----------------------------
app_nome = Label(frame_cima, text='GERADOR DE SENHAS', width=20, height=1, padx=0, relief='flat', anchor='nw', font=('Ivy 16 bold'), bg=corP, fg=corB)
app_nome.place(x=25, y=2)

app_linha = Label(frame_cima, text='', width=295, height=1, padx=0, relief='flat', anchor='nw', font=('Ivy 1'), bg=cor3, fg=corB)
app_linha.place(x=0, y=35)


#----------------------------Função gerar senha ----------------------------
def criar_senha():
    alfabeto_maior = string.ascii_uppercase
    alfabeto_menor = string.ascii_lowercase
    numeros = '123456789'

    global combinar
    combinar = ""

    #---- Condição para Maiúsculo ----
    if estado_1.get() == alfabeto_maior:
        combinar = combinar +  alfabeto_maior
    
    else:
        pass

    #---- Condição para Minúsculo ----
    if estado_2.get() == alfabeto_menor:
        combinar = combinar + alfabeto_menor
    
    else:
        pass

    #---- Condição para Números ----
    if estado_3.get() == numeros:
        combinar = combinar +numeros
    
    else:
        pass



    comprimento = int(spin.get())
    senha = "".join(random.sample(combinar, comprimento ))

    app_senha['text'] = senha


#---------------------------- Desenvolvendo frame baixo ----------------------------
app_senha = Label(frame_baixo, text='- - -', width=21, height=2, padx=0, relief='solid', anchor='center', font=('Ivy 12 bold'), bg=corP, fg=corB)
app_senha.grid(row=0, column=0, columnspan=1, sticky=NSEW, padx=3, pady=10)

app_info = Label(frame_baixo, text='numero de caracteres da senha', height=1, padx=0, relief='flat', anchor='nw', font=('Ivy 10 bold'), bg=corP, fg=corB)
app_info.grid(row=1, column=0,columnspan=2, sticky=NSEW, padx=2, pady=5)

var = IntVar()
var.set(8)
spin = Spinbox(frame_baixo, from_=0, to=20, width=5, textvariable=var)
spin.grid(row=2, column=0, columnspan=2, sticky=NW, padx=5, pady=8)

alfabeto_maior = string.ascii_uppercase
alfabeto_menor = string.ascii_lowercase
numeros = '123456789'

frame_caracteres = Frame(frame_baixo, width=295, height=210, bg=corP, pady=0, padx=0, relief='flat')
frame_caracteres.grid(row=3, column=0, sticky=NSEW, columnspan=3)


#---------------------------- Letras Maiúsculas ----------------------------
estado_1 = StringVar()
estado_1.set(False)
check_1 = Checkbutton(frame_caracteres, width=1, var=estado_1, onvalue=alfabeto_maior, offvalue='off', relief='flat', bg=corP)
check_1.grid(row=0, column=0, sticky=NW, padx=2, pady=5)
app_info = Label(frame_caracteres, text='ABC letras maiusculas', height=1, padx=0, relief='flat', anchor='nw', font=('Ivy 10 bold'), bg=corP, fg=corB)
app_info.grid(row=0, column=1, sticky=NW, padx=2, pady=5)


#---------------------------- Letras minúsculas ----------------------------
estado_2 = StringVar()
estado_2.set(False)
check_2 = Checkbutton(frame_caracteres, width=1, var=estado_2, onvalue=alfabeto_menor, offvalue='off', relief='flat', bg=corP)
check_2.grid(row=1, column=0, sticky=NW, padx=2, pady=5)
app_info = Label(frame_caracteres, text='abc letras minusculas', height=1, padx=0, relief='flat', anchor='nw', font=('Ivy 10 bold'), bg=corP, fg=corB)
app_info.grid(row=1, column=1, sticky=NW, padx=2, pady=5)


#---------------------------- Números ----------------------------
estado_3 = StringVar()
estado_3.set(False)
check_3 = Checkbutton(frame_caracteres, width=1, var=estado_3, onvalue=numeros, offvalue='off', relief='flat', bg=corP)
check_3.grid(row=2, column=0, sticky=NW, padx=2, pady=5)
app_info = Label(frame_caracteres, text='123 numeros', height=1, padx=0, relief='flat', anchor='nw', font=('Ivy 10 bold'), bg=corP, fg=corB)
app_info.grid(row=2, column=1, sticky=NW, padx=2, pady=5)


#---------------------------- Botão ----------------------------
botao_gerar_senha = Button(frame_caracteres,command=criar_senha, text='Gerar Senha',width=34, height=1, relief='flat',overrelief='solid', anchor='center', font=('Ivy 10 bold'), bg=cor3, fg=corB)
botao_gerar_senha.grid(row=5, column=0, sticky=NSEW, padx=5, pady=11, columnspan=5)





janela.mainloop()
