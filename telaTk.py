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
        self.janela.configure(bg='#0b7a0b')
        self.janela.geometry('1000x500')
        self.janela.resizable(False, False)  # Permite a janela ser aumentada ou diminuida tanto em x quanto em  y
        self.janela.maxsize(width=1200, height=700)  # Define o tamanho maximo da tela se acima for True
        self.janela.minsize(width= 950, height= 450) # Define o tamanho minimo da tela se acima for True

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
        labLogo = Label(self.frame2, image=logo, bg=None)
        labLogo.place(relx=0.63,rely=0.01, relwidth=0.35, relheight=0.25)
    
    def enterUser (self):
        '''Função que dispoe as entradas de usuário para gerar grafico'''
        self.campo_X  =  Label(self.frame2, text='Entrada valores coordenadas X:',bg='#f0f7f2')
        self.campo_X.place(relx=0.01, rely=0.28)
        self.explic1 = Label(self.frame2, text='** Entrar valores separados por espaço, tanto em X como em Y', fg='red', bg='#f0f7f2')
        self.explic1.place(relx=0.01, rely=0.32)
        self.entrada_X = Entry(self.frame2, width=48)
        self.entrada_X.place(relx=0.01, rely=0.36)
        self.entrada_X.focus() ## Comando para o cursor ficar ja pronto neste campo aguardando entrada
        self.cmd_EnterX = Button(self.frame2, text='Enter X', command=  self.entradaX)
        self.cmd_EnterX.place(relx=0.78, rely=0.41)
        self.campo_Y = Label(self.frame2, text='Entrada valores coordenadas Y:',bg='#f0f7f2')
        self.campo_Y.place(relx=0.01, rely=0.46)
        self.entrada_Y = Entry(self.frame2, width=48)
        self.entrada_Y.place(relx=0.01, rely=0.50)
        self.cmd_EnterY = Button(self.frame2, text='Enter Y', command= self.entradaY)
        self.cmd_EnterY.place(relx=0.78,rely=0.55)
        # Definição da escala
        self.escala = Label(self.frame2, text='Definir escala dos eixos X e Y:', fg='blue',bg='#f0f7f2')
        self.escala.place(relx=0.01, rely=0.60)
        #Escala X
        self.escalaxTex = Label(self.frame2,text='min X:',bg='#f0f7f2')
        self.escalaxTex.place(relx=0.01, rely=0.64)
        self.escalaValX = Entry(self.frame2,width=5)
        self.escalaValX.place(relx= 0.12, rely=0.64)
        self.escalaxTexM = Label(self.frame2,text='max X:',bg='#f0f7f2')
        self.escalaxTexM.place(relx=0.25, rely=0.64)
        self.escalaValXMx = Entry(self.frame2,width=5)
        self.escalaValXMx.place(relx= 0.36, rely=0.64)
        #Escala y
        self.escalaxTex = Label(self.frame2,text='min Y:',bg='#f0f7f2')
        self.escalaxTex.place(relx=0.52, rely=0.64)
        self.escalaValY = Entry(self.frame2,width=5)
        self.escalaValY.place(relx= 0.62, rely=0.64)
        self.escalaxTexM = Label(self.frame2,text='max Y:',bg='#f0f7f2')
        self.escalaxTexM.place(relx=0.75, rely=0.64)
        self.escalaValMY = Entry(self.frame2,width=5)
        self.escalaValMY.place(relx= 0.86, rely=0.64)
        self.cmd_EnterY = Button(self.frame2, text='Escala', command= self.defineScala)
        self.cmd_EnterY.place(relx=0.78,rely=0.69)

      ## CRIAR AQUI O CAMPO PARA TITULO DO GRAFICO 
      ## NOME DOS EIXOS  X  E Y  E UNIDADES

        ##  =-=-=-=-=-=-= FUNCOES BOTOES =-=-=-=-=-=-=-=-=-==-=-=-=-=-=
        #Entrada de valores experimento
    def  entradaX(self):
        ''' Cria a lista de dados para ser passado para Classe de 
        criação dos graficos '''
        self.kx = (self.entrada_X.get()).split()
        self.entrada_X.delete(0,END) # Depois de pegar os valores apaga o camppo Entry
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
        self.entrada_Y.delete(0,END) # Depois de pegar os valores apaga o camppo Entry
        print(self.ky)
        y = []
        for item in self.ky:
            y.append(float(item))
        print(y)
        return (y)

    def defineScala(self):
        '''Função que converte str em float e Retorna os valores
        da escala do grafico'''
        self.mx = self.escalaValX.get()
        self.Mx = self.escalaValXMx.get()
        self.my = self.escalaValY.get()
        self.My = self.escalaValMY.get()
        # Depois de pegar os valores apaga o camppo Entry
        self.escalaValX.delete(0,END) 
        self.escalaValXMx.delete(0,END) 
        self.escalaValY.delete(0,END)
        self.escalaValMY.delete(0,END)  

        # Conversão para Float
        self.minX = float (self.mx)
        self.maxX = float(self.Mx)
        self.minY = float(self.my)
        self.maxY = float(self.My)
        print( f' min x = {self.minX}, max x = {self.maxX},  min y = {self.minY},  max y =  {self.maxY}' )
        return (self.minX, self.maxX,self.minY,self.maxY)
        ##########################################
        
        


t1 = Telatk()




