# ******************************************
# Projeto de programa para Análise de Regressão
# Desenvolvedor  João Florentino
# ******************************************

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Imports 

from tkinter import *
from turtle import color
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression
# Importação para colocar o grafico dentro da janela do tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg



##  GUI 
jan = Tk()
jan.title('JF - Análise de Regressão')
jan.geometry('800x600')

# Meu Widget
    ## Criando figura nova 

figura = plt.figure(figsize=(8,4), dpi=100)
figura.set_size_inches(6, 4)
fig =  figura.add_subplot(111)

canvasbar = FigureCanvasTkAgg(figura, master=jan)
canvasbar.draw()
canvasbar.get_tk_widget().grid(row=0, column=0)
#canvasbar.get_tk_widget().place(relx=0.6, rely=0.78, anchor=CENTER)  # show the barchart on the ouput window

#widgets


#   layout


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Meu grafico feito no Laboratorio - 2022
# =-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=
#############
## Configurações do Grafico em Geral

titulo = 'Experimento Microndas - Variação da Intensidade x Angulo de Orientação'
EixoX = 'cosseno teta ^ 2'
EixoY = 'Intensidade I (mA)'


#Dados extraidos do Experimento para confecção do grafico
'''print('Digite os valores para Eixo X {EixoX} ')
x = []
x.append([float(ent) for ent in input().split()])
print('Digite os valores para Eixo y {EixoY} ')
y = []
y.append([float(ent) for ent in input().split()])'''
#####################################
### Dados Tabela 01 experimento 06 ##

x = [1, 0.9698, 0.8830, 0.75, 0.5868, 0.4132, 0.25, 0.1170, 0.0301, 0]
y = [1, 0.91, 0.88, 0.75, 0.59, 0.41, 0.25, 0.12, 0.03, 0]

################ FORMATA O GRAFICO #################
plt.style.use('ggplot') # estilo ggplot
plt.plot(x,y,'X') # plota os pontos da lista de dados

plt.title(titulo,fontsize=10, fontweight='bold')
plt.axis([0, 1.1, 0, 1.1]) # [xmin, xmax, ymin, ymax]  #Define o tamanho dos eixos
#plt.xticks(range(0,0.0010 , 0.00001)) #Muda a escala de divisões do eixo X usando o range de 0 a 100 de 10 em 10
plt.ylabel(EixoY, fontsize=9,  fontweight='bold')
plt.xlabel(EixoX, fontsize=9, fontweight='bold')
plt.grid(color='r', linestyle='dotted', linewidth=1)

#Skitlearning faz a Regressão Linear aqui 
# Roda o modelo
X = np.array(x).reshape(-1,1)  # cria um array X para skitlearning
Y = np.array(y) # cria um array Y para skitlearning
linreg = LinearRegression().fit(X, Y) # Cria o modelo de regressão Linear 

# Escreve a equação os coeficientes da equação
print('linear model coeff (w): {}'
.format(linreg.coef_))
print('linear model intercept (b): {:.3f}'
.format(linreg.intercept_))
print(f' Equação ->  Y = {linreg.intercept_} + {linreg.coef_} X')

# Plota o grafico da regressão com os coeficientes achados acima 
plt.plot(x, linreg.coef_ * x + linreg.intercept_, 'b-', color='g')

# apresentas os dois graficos ( os pontos e a reta de regressão)
fig = plt.gcf()  # salva a figura gerada na variável fig
##  TERMINO DO GRAFICO JOAO *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

# Comando para continuar janela ativa
jan.mainloop()