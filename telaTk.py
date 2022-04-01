# ******************************************
# Projeto de programa para Análise de Regressão
# Desenvolvedor  João Florentino
# ******************************************

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Imports 
from pyparsing import restOfLine
import plotarGrafico as pg
from tkinter import *
# Importação para colocar o grafico dentro da janela do tkinter
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

##  GUI

class Telatk:
    def __init__(self) -> None:
        '''Classe que gera a GUI onde o usuário entra os dados do grafico
        visualisa o grafico e com botoes interage com o resultado'''
        janela = Tk()
        janela.title('JF - Análise de Regressão')
       # janela.geometry('1000x800')
        caminho = 'Fig/brasaoUFSC.ico'
        # janela.iconbitmap( caminho)

        #Recebendo o grafico e a equação da classe plortarGrafico
        #equation, fig = pg.graficoPontos()
        ## Criando figura nova 
        figura = plt.figure(figsize=(8,4), dpi=100)
        figura.set_size_inches(6, 4)
        fig =  figura.add_subplot(111)

        #widgets
        # Janela do Grafico
        frame_grafico = Frame(janela)
        canvasbar = FigureCanvasTkAgg(figura, master=frame_grafico)
        canvasbar.draw()
        canvasbar.get_tk_widget().grid(row=1, column=0)

        # inserir o logo 
        frame_usuario = Frame(janela)
        cami2 = '/media/joaoflorentino/J_FLORENTINO/[00] Python 2022/UFSC/Lab_Fisica_Grafs/Projeto_AnaliseRegressao_1/Fig/LogoJoao-2019pq.png'
        logo = PhotoImage(file= cami2)
        labLogo = Label(frame_usuario, image=logo)

        # Escrita explicativa das entradas



        #   layout
        frame_grafico.grid(row=0, column=0)
        frame_usuario.grid(row=0, column=1)
        labLogo.pack(anchor=NW, side='top')

        janela.mainloop()

t1 = Telatk()


