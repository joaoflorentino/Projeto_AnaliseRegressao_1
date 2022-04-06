 #******************************************
# Projeto de programa para Análise de Regressão
# Desenvolvedor  João Florentino
# ******************************************

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Imports 
import numpy as np
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#_-_-_-_-_-_-_-_-_--_-_-_-_-_-
# Classes

class Plotargrafico:
    def __init__(self, X, Y, minX, maxX, minY, maxY, ttgraf, eiX, eiY ) -> None:
        ''' Classe que recebe os dados gerados no experimento para 
        montagem do grafico. Retorna figura com grafico '''
        self.coodenadasX = X # recebe uma lista com os valores de X
        self.coodenadasY = Y # recebe uma lista com os valores de Y
        self.mx = minX  # recebe o valor minimo de X
        self.Mx = maxX # recebe o valor maximo de x
        self.my = minY # recebe o valor minimo de y
        self.My = maxY # recebe o valor maximo de  y
        self.tt = ttgraf # recebe o titulo do grafico
        self.eix = eiX # recebe o titulo do eixo x com unidade
        self.eiy = eiY  # recebe o valor do eixo y com  unidade 
        # iniciaplotagem 
        self.graficoPontos()

    def graficoPontos(self):
        ''' Função que gera dois graficos um de pontos X x Y e uma reta no 
        SkitLearning da regressão destes pontos'''
        ################ FORMATA O GRAFICO #################
        plt.style.use('ggplot') # estilo ggplot
        plt.plot(self.coodenadasX,self.coodenadasY,'X') # plota os pontos da lista de dados

        plt.title(self.tt,fontsize=10, fontweight='bold')
        plt.axis([self.mx, self.Mx, self.my, self.My]) # [xmin, xmax, ymin, ymax]  #Define o tamanho dos eixos
        #plt.xticks(range(0,0.0010 , 0.00001)) #Muda a escala de divisões do eixo X usando o range de 0 a 100 de 10 em 10
        plt.ylabel(self.eiy, fontsize=9,  fontweight='bold')
        plt.xlabel(self.eix, fontsize=9, fontweight='bold')
        plt.grid(color='r', linestyle='dotted', linewidth=1)

        ##  Skitlearning faz a Regressão Linear aqui 
        # Roda o modelo
        self.X = np.array(self.coodenadasX).reshape(-1,1)  # cria um array X para skitlearnin      # Escreve a equação os coeficientes da equação no terminal
        #print('linear model coeff (w): {}' .format(linreg.coef_))
        #print('linear model intercept (b): {:.3f}' .format(linreg.intercept_))g
        self.Y = np.array(self.coodenadasY) # cria um array Y para skitlearning
        linreg = LinearRegression().fit(self.X, self.Y) # Cria o modelo de regressão Linear 

        self.equacao = (f'Y = {linreg.intercept_} + {linreg.coef_} X')
        #print(f' Equação ->  Y = {linreg.intercept_} + {linreg.coef_} X')

        # Plota o grafico da regressão com os coeficientes achados acima 
        plt.plot(self.coodenadasX, linreg.coef_ * self.coodenadasX + linreg.intercept_, color='g')

        # apresentas os dois graficos ( os pontos e a reta de regressão)
        self.fig = plt.gcf().canvas  # salva a figura gerada na variável fig
        ##  TERMINO DO GRAFICO JOAO *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        return (self.fig)

if __name__ ==  '__main__': 
    k1 = [1, 0.9698, 0.8830, 0.75, 0.5868, 0.4132, 0.25, 0.1170, 0.0301, 0]
    k2 = [1, 0.91, 0.88, 0.75, 0.59, 0.41, 0.25, 0.12, 0.03, 0]
    mx = 0
    Mx=1.2
    my= 0
    My= 1.2
    tt = 'Telescopio de Kepler'
    ex = 'Abertura (mm)'
    ey= 'Ganho (admensional)'


    gr = Plotargrafico(k1,k2,mx,Mx,my,My,tt,ex,ey)

    plot = gr.graficoPontos()
   # print(eq)
    plt.show()

