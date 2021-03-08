# main libraries
import turtle
import random

class Race():
    runners = []
    __startY = (-30, -10, 10, 30)
    __colorTurtle = ('red', 'blue', 'green', 'orange')
    
    def __init__(self, width, height):
        # estos atributos ya no hacen falta porque los ponemos abajo como entrada
        # self.width = width
        # self.height = height
        self.__screen = turtle.Screen()
        self.__screen.setup(width, height)
        self.__screen.bgcolor('lightgray')
        self.__startLine = -width/2 + 20
        self.__finishLine = width/2 - 20
        
        self.crear_corredores()
    
    def crear_corredores(self):
        for i in range(4):
            runner = turtle.Turtle()
            runner.color(self.__colorTurtle[i])
            runner.penup()
            runner.shape('turtle')
            runner.setpos(self.__startLine, self.__startY[i])
                     
            self.runners.append(runner)
            
    def competition(self):
        winner = False
        while not winner:
            for tortuga in self.runners:
                avance = random.randint(1,6)
                tortuga.forward(avance)
                
                if tortuga.position()[0] >= self.__finishLine:
                    winner = True
                    print("La tortuga ganadora es la {}".format(tortuga.color()[0]))
                

if __name__ == '__main__':
    circuit = Race(640, 640)
    circuit.competition()