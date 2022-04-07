# ******************************************
# Projeto de programa para Análise de Regressão
# Desenvolvedor  João Florentino
# ******************************************

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Imports 
from tkinter import *

from sympy import true

janela = Tk()
janela.title('Entrada do Programa de analise de regreção')
janela.geometry('350x200')
janela.resizable(True, True)
janela.configure(bg='#4287f5')
#Frames
frame_1 = Frame(janela, bg='#4287f5')
frame_1.place(relx=0.01, rely=0.5, relheight=0.48, relwidth=0.96)

frame_2 = Frame(janela, bg='#4287f5')
frame_2.place(relx=0, rely = 0.5, relheight=0.48, relwidth=0.96)
## Widgets  ##
fig = PhotoImage(file='Fig/AssinaturaPython-2022-Small.png')
figuraLogo = Label(frame_1, image=fig)
figuraLogo.place(relx=0.05, rely=0.02)


text_1 = Label(frame_2, text=' Programa de Graficos ', font=('Uroob', 20,'bold'), fg='#32363b', bg='#4287f5')
text_1.place(relx=0.07, rely=0.05 )

text_2 = Label(frame_2,text='Análise de Regressão', font=('Arial', 18,'bold'), fg='#8f1a35', bg='#4287f5')
text_2.place(relx=0.15,rely=0.40)




janela.mainloop()
