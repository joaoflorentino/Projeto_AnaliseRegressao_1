# ******************************************
# Projeto de programa para Análise de Regressão
# Desenvolvedor  João Florentino
# ******************************************

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Imports 
from operator import ne
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
        self.janela = Tk()
        self.janela.title('JF - Análise de Regressão')
        #janela.geometry('1000x800')
        caminho = 'Fig/brasaoUFSC.ico'
        # janela.iconbitmap( caminho)
    
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
        '''Fução que cria e ordema os widgets na janela principal'''
        #Recebendo o grafico e a equação da classe plortarGrafico
        #equation, fig = pg.graficoPontos()
        ## Criando figura nova 
        figura = plt.figure(figsize=(8,4), dpi=100)
        figura.set_size_inches(6, 4)
        fig =  figura.add_subplot(111)

        ###    WIDGETS  ##########
        # Janela do Grafico
        self.frame_grafico = Frame(self.janela)
        canvasbar = FigureCanvasTkAgg(figura, master=self.frame_grafico)
        canvasbar.draw()
        canvasbar.get_tk_widget().pack(side='left')

        # Janela Usuário +++++++++++++
        # Frame 1

        self.frame_usuario = Frame(self.janela, height = 50, width=100 , bg='gray')
        self.frameLogo = Frame(self.frame_usuario, height= 20, width=100)
        self.frame_escala = Frame(self.frame_usuario, bg="#9ef7cb")

        cami2 = '/media/joaoflorentino/J_FLORENTINO/[00] Python 2022/UFSC/Lab_Fisica_Grafs/Projeto_AnaliseRegressao_1/Fig/LogoJoao-2019pq.png'
        logo = PhotoImage(file= cami2)
        labLogo = Label(self.frame_usuario, image=logo)
        # Escrita explicativa das entradas
       
        campo_X  =  Label(self.frame_usuario, text='Entrada valores coordenadas X:')
        explic1 = Label(self.frame_usuario, text='** Entrar com os valores separados por espaço, tanto em X como em Y', fg='red')
        self.entrada_X = Entry(self.frame_usuario, width=55)
        campo_Y = Label(self.frame_usuario, text='Entrada valores coordenadas Y:')
        self.entrada_Y = Entry(self.frame_usuario, width=55)
        # Frame 2
        
        escala = Label(self.frame_escala, text='Definir escala dos eixos X e Y:', fg='blue')
        escalaxTex = Label(self.frame_escala,text='min X:', width=6)
        escalaValX = Entry(self.frame_escala,width=6)


        
        ##  BUTOES 
        cmd_EnterX = Button(self.frame_usuario, text='Enter X', command=  self.entradaX)
        cmd_EnterY = Button(self.frame_usuario, text='Enter Y', command= self.entradaY)

    
    
        #********  LAYOUT  ********************************
        # *-*-*-*-*-* FRAMES -*-*-*-*-*-*-*-*-*--*-*-*-*-*-*
        #self.janela.pack()
        self.frame_grafico.pack(side='top')
        self.frame_usuario.pack(side='right')
        self.frameLogo.pack(side='right')
        #self.frame_escala.pack(side='bottom')

        #-=-=-=-=-=-= Botoes,  Textos  e  Entrys  =-=-=-=-=-=-=-=-
        # Pertencem ao Frame 1
        labLogo.pack(side='right', anchor='ne')
        campo_X.pack(side='left')
        explic1.pack(side='left')
        #self.entrada_X.pack(side='bottom')
       # cmd_EnterX.pack(side='bottom')
       # campo_Y.pack(side='bottom')
        #self.entrada_Y.pack(side='bottom')
        #cmd_EnterY.pack(side='bottom')
        # Pertencem ao Fram 2
        #escala.pack(side='bottom')
        #escalaxTex.pack(side='bottom')
        #escalaValX.pack(side='right')

        campo_X.focus() ## Comando para o cursor ficar ja pronto neste campo aguardando entrada

        
        self.janela.mainloop()

t1 = Telatk()
t1.scremm()
print(t1.entradaX)
print(t1.entradaY)




