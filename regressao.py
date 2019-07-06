import math
from argument import Argument
class Regressao:
    def __init__(self):
        self.argument = Argument({})
    
    def somar(self, vetor):
        soma = 0
        for i in vetor: soma = soma + float(i)
        return soma
    
    def potencia(self, vetor):
        soma = 0
        for i in vetor: soma = soma + (float(i) ** 2)
        return soma
    
    def produto(self, dataframe):
        soma = 0
        if len(dataframe['y']) == len(dataframe['x']): count = len(dataframe['x'])
        else: count = 0
        for i in range(count): soma = soma + (float(dataframe['x'][i]) * float(dataframe['y'][i]))
        return soma

    def calcularValores(self, dataframe):
        self.argument.Sx = self.somar(dataframe['x'])
        self.argument.Sy = self.somar(dataframe['y'])
        self.argument.Sx2 = self.potencia(dataframe['x'])
        self.argument.Sy2 = self.potencia(dataframe['y'])
        self.argument.Sxy = self.produto(dataframe)
        self.argument.n = len(dataframe['x'])

    def coeficiente(self):
        return (
            ((self.argument.n * self.argument.Sxy) - (self.argument.Sx * self.argument.Sy)) /
            math.sqrt(
                ((self.argument.n * self.argument.Sx2) - math.pow(self.argument.Sx,2)) *
                ((self.argument.n * self.argument.Sy2) - math.pow(self.argument.Sy,2))
            )
        )

    def a(self):
        return (
            ((self.argument.n * self.argument.Sxy) - (self.argument.Sx * self.argument.Sy)) /
            ((self.argument.n * self.argument.Sx2) - math.pow(self.argument.Sx,2))
        )
    
    def b(self):
        return (self.argument.Sy - (self.a() * self.argument.Sx)) / self.argument.n
    
    def prever(self, arguments):
        try: resultado = (self.a() * float(arguments['x'])) + self.b()
        except:
            try: resultado = (float(arguments['y']) - self.b()) / self.a()
            except: resultado = 0
        return resultado