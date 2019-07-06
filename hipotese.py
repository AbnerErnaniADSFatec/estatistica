import math
from argument import Argument
class Hipotese:
    def __init__(self):
        self.argument = Argument({})

    def area(self):
        if self.argument.t == 0: self.area = self.argument.z
        elif self.argument.z == 0: self.area = self.argument.t
        else: self.area = 0

    def zt(self):
        self.area()
        return (
            (self.argument.media - self.argument.u) /
            (
                self.argument.desvio /
                math.sqrt(self.argument.n)
            )
        )
    
    def testar(self):
        if self.zt() >= self.area: return True
        else: return False