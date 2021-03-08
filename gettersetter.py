class GetterSetter():
    def __init__(self):
        self.__privado = None
    
    def setprivado(self, valor):
        self.__privado = valor
        
    def getprivado(self):
        return self.__privado
    
    def getandset(self, valor=None):
        if valor == None:
            return self.privado
        else:
            return self.__privado = valor
    
    def __str__(self):
        return "Propiedad privada es -> {}".format(self.__privado)
    
        
if __name__ == '__main__':
    c = GetterSetter()