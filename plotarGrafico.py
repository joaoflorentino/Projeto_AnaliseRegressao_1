 #******************************************
# Projeto de programa para Análise de Regressão
# Desenvolvedor  João Florentino
# ******************************************

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Imports 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression

#_-_-_-_-_-_-_-_-_--_-_-_-_-_-
# Classes

class Plotargrafico:
    def __init__(self, X, Y) -> None:
        ''' Classe que recebe os dados gerados no experimento para 
        montagem do grafico. Retorna figura com grafico '''
        self.coodenadasX = X # recebe uma lista com os valores de X
        self.coodenadasY = Y # recebe uma lista com os valores de Y
    def graficoPontos(self):
        ''' Função que gera dois graficos um de pontos X x Y e uma reta no 
        SkitLearning da regressão destes pontos'''
        ## Entra os dados do Gráfico ##
        # Texto
        titulo = str(input())  #solicita titulo do grafico para figura
        EixoX = str(input()) #solicita descrição do eixo X e unidades
        EixoY = str(input()) #solicita descrição do eixo Y e unidades 
        # Numericos
        escalaXmin = float(input())
        escalaXmax = float(input())
        escalaYmin = float(input())
        escalaYmax = float(input())
        
        ################ FORMATA O GRAFICO #################
        plt.style.use('ggplot') # estilo ggplot
        plt.plot(self.coodenadasX,self.coodenadasY,'X') # plota os pontos da lista de dados

        plt.title(titulo,fontsize=10, fontweight='bold')
        plt.axis([escalaXmin, escalaXmax, escalaYmin, escalaYmax]) # [xmin, xmax, ymin, ymax]  #Define o tamanho dos eixos
        #plt.xticks(range(0,0.0010 , 0.00001)) #Muda a escala de divisões do eixo X usando o range de 0 a 100 de 10 em 10
        plt.ylabel(EixoY, fontsize=9,  fontweight='bold')
        plt.xlabel(EixoX, fontsize=9, fontweight='bold')
        plt.grid(color='r', linestyle='dotted', linewidth=1)

        ##  Skitlearning faz a Regressão Linear aqui 
        # Roda o modelo
        X = np.array(self.coodenadasX).reshape(-1,1)  # cria um array X para skitlearnin      # Escreve a equação os coeficientes da equação no terminal
        #print('linear model coeff (w): {}' .format(linreg.coef_))
        #print('linear model intercept (b): {:.3f}' .format(linreg.intercept_))g
        Y = np.array(self.coodenadasY) # cria um array Y para skitlearning
        linreg = LinearRegression().fit(X, Y) # Cria o modelo de regressão Linear 

        equacao = (f'Y = {linreg.intercept_} + {linreg.coef_} X')
        #print(f' Equação ->  Y = {linreg.intercept_} + {linreg.coef_} X')

        # Plota o grafico da regressão com os coeficientes achados acima 
        plt.plot(self.coodenadasX, linreg.coef_ * self.coodenadasX + linreg.intercept_, 'b-', color='g')

        # apresentas os dois graficos ( os pontos e a reta de regressão)
        fig = plt.gcf()  # salva a figura gerada na variável fig
        ##  TERMINO DO GRAFICO JOAO *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        return (equacao, fig)

if __name__ ==  '__main__': 
    k1 = [1, 0.9698, 0.8830, 0.75, 0.5868, 0.4132, 0.25, 0.1170, 0.0301, 0]
    k2 = [1, 0.91, 0.88, 0.75, 0.59, 0.41, 0.25, 0.12, 0.03, 0]

    gr = Plotargrafico(k1,k2)

    eq, plot = gr.graficoPontos()
    print(eq)
    plt.show()

