import math
from argument import Argument
class Confianca:
    def __init__(self):
        self.argument = Argument({})
    
    def verificar(self):
        if self.argument.t == 0: self.area = self.argument.z
        elif self.argument.z == 0: self.area = self.argument.t
        else: self.area = 0
        self.finita = math.sqrt((self.argument.N - self.argument.n ) / (self.argument.N - 1))
        self.pontual = self.pontual() * (1 - self.pontual())

    def media_inf(self):
        self.verificar()
        return (self.area * (self.argument.desvio / math.sqrt(self.argument.n)))
    
    def media_fin(self):
        self.verificar()
        return (
            self.area *
            (
                self.argument.desvio /
                math.sqrt(self.argument.n)
            ) *
            self.finita
        )
    
    def amostra_inf(self):
        self.verificar()
        return math.pow((
            (
                self.area * self.argument.desvio
            ) /
            self.argument.e
        ),2)
    
    def amostra_fin(self):
        self.verificar()
        return (
            (
                math.pow(self.area,2) * math.pow(self.argument.desvio,2) * self.argument.N
            ) /
            (
                (math.pow(self.area,2) * math(self.argument.desvio)) +
                (math.pow(self.argument.e,2) * (self.argument.N - 1))
            )
        )
    
    def erro_inf(self):
        self.verificar()
        return (
            (self.area * self.argument.desvio) /
            math.sqrt(self.argument.n)
        )
    
    def erro_fin(self):
        self.verificar()
        return (
            (self.area * self.argument.desvio) /
            math.sqrt(self.argument.n) * self.finita
        )
    
    def pontual(self):
        return (self.argument.x / self.argument.n)
    
    def intervalar_inf(self):
        self.verificar()
        return (
            self.area *
            math.sqrt(self.pontual / self.argument.n)
        )
    
    def intervalar_fin(self):
        self.verificar()
        return (self.intervalar_inf() * self.finita)
    
    def amostra_inf_estimativa(self):
        self.verificar()
        return (
            math.pow(self.area,2) *
            (self.pontual / math.pow(self.argument.e,2))
        )
    
    def amostra_fin_estimativa(self):
        self.verificar()
        return (
            (math.pow(self.area,2) * self.pontual * self.argument.N) /
            (
                ((self.argument.N - 1) * math.pow(self.argument.e,2)) +
                (math.pow(self.area,2) * self.pontual)
            )
        )
    
    def erro_inf_estimativa(self):
        self.verificar()
        return (self.area * math.sqrt(self.pontual / self.argument.n))
    
    def erro_fin_estimativa(self):
        self.verificar()
        return (self.erro_inf_estimativa * self.finita)

