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
        self.janela = Tk()
        self.telaScreem()
        self.framesScreem()
        self.screemGrafico()
        self.poeLogo()
        self.enterUser()
        
        
        self.janela.mainloop()
    
    def telaScreem (self):
        '''Função que define o formato geral da tela '''
        caminho = 'Fig/brasaoUFSC.ico'
        # self.janela.iconbitmap( caminho)
        self.janela.title('JF - Análise de Regressão')
        self.janela.configure(bg='#943143')
        self.janela.geometry('1000x500')
        self.janela.resizable(True, True)  # Permite a janela ser aumentada ou diminuida tanto em x quanto em  y
        self.janela.maxsize(width=1200, height=700)  # Define o tamanho maximo da tela
        self.janela.minsize(width= 800, height= 300)

    def framesScreem (self):
        '''Função que define o tamnho e a posição dos frames'''
        # FRAME 2
        self.frame1 = Frame(self.janela, bd=4 ,bg='#f0f7f2', highlightbackground='#610923', highlightthickness=3)
        self.frame1.place(relx=0.01, rely=0.02, relwidth=0.65, relheight=0.96)
        #O codigo acima define uma area responsiva para o frame 1 e o tamnho responsivo dele 
        # FRAME 2
        self.frame2 = Frame(self.janela, bd=4 ,bg='#f0f7f2', highlightbackground='#610923', highlightthickness=3)
        self.frame2.place(relx=0.62, rely=0.02, relwidth=0.37, relheight=0.96)
        #O codigo acima define uma area responsiva para o frame 1 e o tamnho responsivo dele 
    
    def screemGrafico(self):
        '''Função que posiciona o grafico dentro do frame1'''
        figura = plt.figure(figsize=(8,4), dpi=100)
        figura.set_size_inches(6, 4)
        fig =  figura.add_subplot(111)
        canvasbar = FigureCanvasTkAgg(figura, master=self.frame1)
        canvasbar.draw()
        canvasbar.get_tk_widget().place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.97)
    
    def poeLogo(self):
        cami2 = '/media/joaoflorentino/J_FLORENTINO/[00] Python 2022/UFSC/Lab_Fisica_Grafs/Projeto_AnaliseRegressao_1/Fig/LogoJoao-2019pq.png'
        logo = PhotoImage(file= cami2)
        labLogo = Label(self.frame2, image=logo)
        labLogo.place(relx=0.65,rely=0.01, relwidth=0.35, relheight=0.25)
    
    def enterUser (self):
        '''Função que dispoe as entradas de usuário para gerar grafico'''
        self.campo_X  =  Label(self.frame2, text='Entrada valores coordenadas X:')
        self.campo_X.place(relx=0.01, rely=0.28)
        self.explic1 = Label(self.frame2, text='** Entrar valores separados por espaço, tanto em X como em Y', fg='red')
        self.explic1.place(relx=0.01, rely=0.32)
        self.entrada_X = Entry(self.frame2, width=48)
        self.entrada_X.place(relx=0.01, rely=0.36)
        self.entrada_X.focus() ## Comando para o cursor ficar ja pronto neste campo aguardando entrada
        self.cmd_EnterX = Button(self.frame2, text='Enter X', command=  self.entradaX)
        self.cmd_EnterX.place(relx=0.78, rely=0.41)



        """
        campo_Y = Label(self.frame_usuario, text='Entrada valores coordenadas Y:')
        self.entrada_Y = Entry(self.frame_usuario, width=55)
        escala = Label(self.frame_escala, text='Definir escala dos eixos X e Y:', fg='blue')
        escalaxTex = Label(self.frame_escala,text='min X:', width=6)
        escalaValX = Entry(self.frame_escala,width=6)
        


        
        ##  BUTOES 
        
        cmd_EnterY = Button(self.frame_usuario, text='Enter Y', command= self.entradaY)
"""











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
        

        ###    WIDGETS  ##########
        
        # Janela Usuário +++++++++++++
        # Frame 1

        self.frame_usuario = Frame(self.janela, height = 50, width=100 , bg='gray')
        self.frameLogo = Frame(self.frame_usuario, height= 20, width=100)
        self.frame_escala = Frame(self.frame_usuario, bg="#9ef7cb")

        
        # Escrita explicativa das entradas
       
        

    
    
        #********  LAYOUT  ********************************
        # *-*-*-*-*-* FRAMES -*-*-*-*-*-*-*-*-*--*-*-*-*-*-*
        #self.janela.pack()
        self.frame_grafico.pack(side='top')
        self.frame_usuario.pack(side='right')
        self.frameLogo.pack(side='right')
        #self.frame_escala.pack(side='bottom')

        #-=-=-=-=-=-= Botoes,  Textos  e  Entrys  =-=-=-=-=-=-=-=-
        # Pertencem ao Frame 1
        

        

        
        

t1 = Telatk()




