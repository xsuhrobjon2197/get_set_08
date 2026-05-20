#9-m
class Game:
    def __init__(self, name, gb):
        self.name = name
        self.__gb = gb
        
    @property
    def gb(self):
        return self.__gb
    
    @gb.setter
    def gb(self, yangi):
        self.__gb = yangi
        
g1 = Game("Minecraft", 10)
print(g1)

res = g1.gb
print(res)

g1.gb = 20
print(g1.gb)
