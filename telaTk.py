# ******************************************
# Projeto de programa para Análise de Regressão
# Desenvolvedor  João Florentino
# ******************************************

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Imports 

from tkinter import *
# Importação para colocar o grafico dentro da janela do tkinter
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from plotarGrafico import  Plotargrafico
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

##  GUI

class Telatk():
    def __init__(self) -> None:
        '''Classe que gera a GUI onde o usuário entra os dados do grafico
        visualisa o grafico e com botoes interage com o resultado'''
        self.janela = Tk()
        self.telaScreem()
        self.framesScreem()
        self.screemGrafico()
        self.poeLogo()
        self.enterUser()
        ## Conservação da Janela Tkinter
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
        #self.figrafico = F
        self.figura = plt.figure(figsize=(5,5),  dpi=100)
        self.canvasbar = FigureCanvasTkAgg(self.figura, master=self.frame1)
        self.figrafico =  self.figura.add_subplot(111)
        self.canvasbar.get_tk_widget().place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.97)
        self.toobar = NavigationToolbar2Tk(self.canvasbar, self.frame1)
        self.canvasbar._tkcanvas.place(relx=0.00, rely=0.00, relwidth=0.98, relheight=0.97)
        #self.canvasbar.draw()  Passa da para linha  218 para jogar nova figura no Frame 1

    def poeLogo(self):
        self.cami1 = 'Fig/AssinaturaPython-2022-Small.png'
        self.logo1 = PhotoImage(file=self.cami1)
        self.labLogo1 = Label(self.frame2, image=self.logo1,bg='#f0f7f2')
        self.labLogo1.place(relx=0.01, rely=0.01)
        self.cami2 = 'Fig/LogoJoao-2019pq.png'
        self.logo2 = PhotoImage(file= self.cami2)
        self.labLogo2 = Label(self.frame2, image=self.logo2)
        self.labLogo2.place(relx=0.83,rely=0.01)
    
    def enterUser (self):
        '''Função que dispoe as entradas de usuário para gerar grafico'''
        self.campo_X  =  Label(self.frame2, text='Entrada valores coordenadas X:', font=('verdana', 10),bg='#f0f7f2')
        self.campo_X.place(relx=0.01, rely=0.28)
        self.explic1 = Label(self.frame2, text='** Entrar valores separados por espaço, tanto em X e Y', font=('Arial', 9, 'bold'),fg='red', bg='#f0f7f2')
        self.explic1.place(relx=0.01, rely=0.32)
        self.entrada_X = Entry(self.frame2, width=48)
        self.entrada_X.place(relx=0.01, rely=0.36)
        self.entrada_X.focus() ## Comando para o cursor ficar ja pronto neste campo aguardando entrada
        self.cmd_EnterX = Button(self.frame2, text='Enter X', command=  self.entradaX)
        self.cmd_EnterX.place(relx=0.78, rely=0.41)
        self.campo_Y = Label(self.frame2, text='Entrada valores coordenadas Y:', font=('verdana', 10),bg='#f0f7f2')
        self.campo_Y.place(relx=0.01, rely=0.46)
        self.entrada_Y = Entry(self.frame2, width=48)
        self.entrada_Y.place(relx=0.01, rely=0.50)
        self.cmd_EnterY = Button(self.frame2, text='Enter Y', command= self.entradaY)
        self.cmd_EnterY.place(relx=0.78,rely=0.55)
        # Definição da escala
        self.escala = Label(self.frame2, text='Definir escala dos eixos X e Y:', font=('verdana', 10), fg='blue',bg='#f0f7f2')
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
        # Entrada dos titulos e nomes de eixos
        self.texTitulos = Label(self.frame2, text= 'Entrada de Titulos e Eixos:', bg='#f0f7f2')
        self.texTitulos.place(relx=0.01, rely=0.72)
        self.titex = Label(self.frame2, text='Título: ', bg='#f0f7f2')
        self.titex.place(relx=0.01, rely=0.76)
        self.campt = Entry(self.frame2, width=42)
        self.campt.place(relx=0.12, rely=0.76)
        self.eixoX = Label(self.frame2, text='Eixo X: ', bg='#f0f7f2')
        self.eixoX.place(relx=0.01, rely=0.81)
        self.eixoXt = Entry(self.frame2, width=42)
        self.eixoXt.place(relx=0.12, rely=0.81)
        self.eixoy = Label(self.frame2, text='Eixo Y: ', bg='#f0f7f2')
        self.eixoy.place(relx=0.01, rely=0.86)
        self.eixoYt = Entry(self.frame2, width=42)
        self.eixoYt.place(relx=0.12, rely=0.86)
        self.cmd_Eixos = Button(self.frame2, text='Titulos', command= self.geraTextosGraf)
        self.cmd_Eixos.place(relx=0.79,rely=0.91)
        ## Botao Final Gerdor do grafico
        self.cmd_Grafico = Button(self.frame2, text='Gerar Grafico',bd=3, bg='#f7ef59', command= self.geraOGraf)
        self.cmd_Grafico.place(relx=0.01,rely=0.92)
        ## Botão chamar grafico interativo para salvar figura
        self.cmd_GraficoInterativo = Button(self.frame2, text='Graf Interativo',bd=3, bg='#f0b207', command= self.chamaInterativo)
        self.cmd_GraficoInterativo.place(relx=0.35,rely=0.92)

        ##  =-=-=-=-=-=-= FUNCOES BOTOES =-=-=-=-=-=-=-=-=-==-=-=-=-=-=
        #Entrada de valores experimento
    def  entradaX(self):
        ''' Cria a lista de dados para ser passado para Classe de 
        criação dos graficos '''
        self.kx = (self.entrada_X.get()).split()
        self.entrada_X.delete(0,END) # Depois de pegar os valores apaga o camppo Entry
        #print(self.kx)
        self.x = []
        for item in self.kx:
            self.x.append(float(item))
        print(self.x)
        return (self.x)
        ####################################
    def entradaY(self):
        ''' Cria a lista de dados para ser passado para Classe de 
        criação dos graficos '''
        self.ky = (self.entrada_Y.get()).split()
        self.entrada_Y.delete(0,END) # Depois de pegar os valores apaga o camppo Entry
        #print(self.ky)
        self.y = []
        for item in self.ky:
            self.y.append(float(item))
        print(self.y)
        return (self.y)

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

    def geraTextosGraf(self):
        '''Fução que gera carrega os titulo do Gráfico e 
        dos eixos e Retorona para Classe plotaGrafico'''
        self.titulo= self.campt .get()
        self.titeixoX = self.eixoXt.get()
        self.titeixoY = self.eixoYt.get()
        # Depois de pegar os valores apaga o camppo Entry
        self.campt .delete(0,END) 
        self.eixoXt.delete(0,END) 
        self.eixoYt.delete(0,END)
        print(f'Titulo Do Grafico= {self.titulo}')
        print(f'Titulo Eixo x = {self.titeixoX}')
        print(f'Titulo Eixo y = {self.titeixoY}')
        return (self.titulo, self.titeixoX, self.titeixoY)

    def geraOGraf(self):
        '''Função que gera o grafico dentro do cavas e traz a equação 
        linearizada do projeto'''
        self.coodenadasX = self.x # recebe uma lista com os valores de X
        self.coodenadasY = self.y # recebe uma lista com os valores de Y
        self.mx = self.minX # recebe o valor minimo de X
        self.Mx = self.maxX # recebe o valor maximo de x
        self.my = self.minY # recebe o valor minimo de y
        self.My = self.maxY # recebe o valor maximo de  y
        self.tt = self.titulo # recebe o titulo do grafico
        self.eix = self.titeixoX # recebe o titulo do eixo x com unidade
        self.eiy = self.titeixoY  # recebe o valor do eixo y com  unidade 
        ## Chama a classe plotarGrafico
        self.figrafico= Plotargrafico(self.coodenadasX, self.coodenadasY, self.mx,self.Mx, self.my, self.My, self.tt, self.eix, self.eiy)
        self.canvasbar.draw()
    
    def chamaInterativo(self):
            plt.show()
        ##########################################
    


t1 = Telatk()




