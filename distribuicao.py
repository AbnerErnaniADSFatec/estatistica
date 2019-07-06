import math
import pandas as pd
from argument import Argument
class Distribuicao:
    def __init__(self):
        self.argument = Argument({})

    def media(self, vetor):
        soma = 0
        for i in vetor: soma = soma + int(i)
        return soma / int(len(vetor))
    
    def moda(self, vetor):
        ocorrencias = {}
        for i in vetor:
            if i in ocorrencias: ocorrencias[i] += 1
            else: ocorrencias[i] = 0
        maior = math.inf * (-1)
        for i in vetor:
            if ocorrencias[i] > maior:
                maior = ocorrencias[i]
                valor = i
        return i
    
    def mediana(self, vetor):
        resultado = 0
        if int(len(vetor)) % 2 == 0: resultado = (vetor[int(int(len(vetor))/2) - 1] + vetor[int(int(len(vetor))/2)]) / 2
        else: resultado = vetor[int(int(len(vetor))/2)]
        return resultado

    def somar(self, vetor):
        soma = 0
        for i in vetor: soma = soma + float(i)
        return soma
    
    def produto(self, dataframe):
        soma = 0
        if len(dataframe['y']) == len(dataframe['x']): count = len(dataframe['x'])
        else: count = 0
        for i in range(count): soma = soma + (float(dataframe['x'][i]) * float(dataframe['y'][i]))
        return soma
    
    def acumulado(self, vetor):
        soma, data = 0, []
        for i in range(len(vetor)):
            soma = soma + float(vetor[i])
            data.append(soma)
        return data
    
    def porcentagem(self, total, vetor):
        data = []
        for i in range(len(vetor)): data.append(float(vetor[i]) / total)
        return data
    
    def calcularValores(self, dataframe):
        self.argument.obj = dataframe['x']
        self.argument.fi = dataframe['y']
        self.argument.Sfi = self.somar(self.argument.fi)
        self.argument.fri = self.porcentagem(self.somar(self.argument.fi),self.argument.fi)
        self.argument.Sfri = self.somar(self.argument.fri)
        self.argument.Fi = self.acumulado(self.argument.fi)
        self.argument.Fri = self.acumulado(self.argument.fri)
        print(pd.DataFrame({
            'Fri' : self.argument.Fri,
            'fri' : self.argument.fri,
            'Fi' : self.argument.Fi,
            'fi' : self.argument.fi,
            'obj' : self.argument.obj
        }))
    
    def mediaFrequencia(self):
        return (
            self.produto({'x':self.argument.obj,'y':self.argument.fi}) /
            self.somar(self.argument.fi)
        )

    def diferenca(self):
        data = []
        for i in range(len(self.argument.obj)):
            data.append(
                math.pow((float(self.argument.obj[i]) - self.mediaFrequencia()),2) *
                float(self.argument.fi[i])
            )
        return data

    def desvio(self):
        return math.sqrt(self.somar(self.diferenca()) / (self.argument.Sfi - 1))
 
    def variancia(self):
        return math.pow(self.desvio(),2)
    
    def binomial(self):
        return (
            (math.factorial(self.argument.n) / (math.factorial(self.argument.k) * math.factorial(self.argument.n - self.argument.k))) *
            math.pow(self.argument.p,self.argument.k) *
            math.pow(self.argument.q,(self.argument.n - self.argument.k))
        )
    
    def poisson(self):
        return (
            (
                (self.argument.e ** ((-1) * self.argument.l * self.argument.t )) *
                (( self.argument.l * self.argument.t ) ** self.argument.x)
            ) /
            math.factorial(self.argument.x)
        )
    
    def geometrica(self):
        return ((self.argument.q ** (self.argument.x - 1)) * self.argument.p)
    
    def normal(self):
        return self.argument.z
    
    def student(self):
        return self.argument.t
