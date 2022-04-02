# ******************************************
# Projeto de programa para Análise de Regressão
# Desenvolvedor  João Florentino
# ******************************************

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Imports 
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
    
    #Entrada de valores experimento
    def  entradaX(self):
        ''' Cria a lista de dados para ser passado para Classe de 
        criação dos graficos '''
        self.kx = (self.entrada_X.get()).split()
        print(self.kx)
        x = []
        for item in self.kx:
            x.append(float(item))
        print(x)
        return (x)
        ####################################
    def entradaY(self):
        ''' Cria a lista de dados para ser passado para Classe de 
        criação dos graficos '''
        self.ky = (self.entrada_Y.get()).split()
        print(self.ky)
        y = []
        for item in self.ky:
            y.append(float(item))
        print(y)
        return (y)
        ####################################

    def scremm(self):
        janela = Tk()
        janela.title('JF - Análise de Regressão')
        #janela.geometry('1000x800')
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
        canvasbar.get_tk_widget().grid(row=0, column=0, sticky=W)

        # inserir o logo 
        frame_usuario = Frame(janela)
        cami2 = '/media/joaoflorentino/J_FLORENTINO/[00] Python 2022/UFSC/Lab_Fisica_Grafs/Projeto_AnaliseRegressao_1/Fig/LogoJoao-2019pq.png'
        logo = PhotoImage(file= cami2)
        labLogo = Label(frame_usuario, image=logo)

        # Escrita explicativa das entradas
        campo_X  =  Label(frame_usuario, text='Entrada valores coordenadas X:')
        self.entrada_X = Entry(frame_usuario)
        campo_Y = Label(frame_usuario, text='Entrada valores coordenadas Y:')
        self.entrada_Y = Entry(frame_usuario)

        


        ##  BUTOES 
        cmd_EnterX = Button(frame_usuario, text='Enter X', command=  self.entradaX)
        cmd_EnterY = Button(frame_usuario, text='Enter Y', command= self.entradaY)

        #Captura entradas do campo entrada 
        
        

        #   layout
        frame_grafico.grid(row=0, column=0, sticky=W)
        frame_usuario.grid(row=0, column=1, sticky=E+N)
        labLogo.grid(row=0, column=4, sticky=E+N)
        campo_X.grid(row=1, column=0, sticky=W)
        self.entrada_X.grid(row=2, column=0, sticky=W)
        cmd_EnterX.grid(row=3, column=0, sticky=E)
        campo_Y.grid(row=4, column=0, sticky=W)
        self.entrada_Y.grid(row=5, column=0, sticky=W)
        cmd_EnterY.grid(row=6, column=0, sticky=E)

        campo_X.focus() ## Comando para o cursor ficar ja pronto neste campo aguardando entrada

        
        janela.mainloop()

t1 = Telatk()
t1.scremm()
print(t1.entradaX)
print(t1.entradaY)




