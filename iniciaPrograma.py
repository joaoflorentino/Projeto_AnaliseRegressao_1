# ******************************************
# Projeto de programa para Análise de Regressão
# Desenvolvedor  João Florentino
# ******************************************

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Imports 
from tkinter import *
from sympy import true

from telaTk import *

## Definicions *-*-*-*-*-*-*-*-*-

gama = Tk()
gama.title('Entrada do Programa de analise de regreção')
gama.geometry('500x300')
gama.resizable(True, True)
gama.configure(bg='#4287f5')
#Frames
frame_1 = Frame(gama, bg='#4287f5', highlightbackground='#1b84f5', highlightthickness=3)
frame_1.place(relx=0.01, rely=0.01,  relwidth=0.96, relheight=0.48)

frame_2 = Frame(gama, bg='#4287f5', highlightbackground='#1b84f5', highlightthickness=3)
frame_2.place(relx=0.01, rely = 0.5, relwidth=0.96, relheight=0.48)

## Widgets  ##
# -=--=-=-=-=-=-=-=-=-= Frame 1 =-=-=-=-=-=-=-=-=-
nome = Label(frame_1, text='Python 2022 Física', font=('zapf chancery', 23,'bold'), bg='#4287f5')
nome.place(relx=0.25, rely=0.45)
# Gera figura da logomarca Joao
pathe = 'Fig/AssinaturaPython-2022-Small.png'
fig = PhotoImage(file=pathe)
figuraLogo = Label(frame_1, image=fig, bg='#4287f5')
figuraLogo.place(relx=0.05, rely=0.02)

# -=-=-=-=-=-=-=-=-=-=-=- Fram 2 ==-=-=-=--=-=-=-=-=-
text_1 = Label(frame_2, text=' Programa de Graficos ', font=('gothic', 20,'bold'), fg='#32363b', bg='#4287f5')
text_1.place(relx=0.20, rely=0.05 )

text_2 = Label(frame_2,text='Análise de Regressão', font=('gothic', 18,'bold'), fg='#8f1a35', bg='#4287f5')
text_2.place(relx=0.28,rely=0.40)

#  Botão 

cmd_but = Button(frame_2, text='Iniciar', bg='#66eb42', command= Telatk )
cmd_but.place(relx=0.48, rely=0.75)

gama.mainloop()
