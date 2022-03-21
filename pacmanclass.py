class PacPerson :
    #Properties:
    def Properties(self,name,speed,color,lives):
        self.name = name
        self.speed = speed
        self.color = color
        self.lives = lives
    #Functions:
    def MoveUp():
        None
    def MoveDown():
        None
    def MoveLeft():
        None
    def MoveRight():
        None
    def Eat():
        #makesound
        None
    def Death():
        None

class Ghosts :
    #Propeties:
    def Properties(self,name,color,personality,speed):
        self.name = name
        self.color = color
        self.personality = personality 
        self.speed = speed
    #Functions
    def MoveUp():
        None
    def MoveDown():
        None
    def MoveLeft():
        None
    def MoveRight():
        None
    def Kill():
        None
    def Death():
        None


PacMan = PacPerson("Pacman",1,"Yellow",4)
Blinky = Ghosts("Blinky","Red","Chaser",2)
Pinky = Ghosts("Pinky","Pink","Supriserd",1)
