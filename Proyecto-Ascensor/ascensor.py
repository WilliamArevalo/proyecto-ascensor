from Stacks import StackSimpleArray
import pygame
import time


class elevator(object):

    def __init__(self, floors):
        self.floors = floors
        self.currentFloor = 0
        self.floorsUp = StackSimpleArray(10)
        self.floorsDown = StackSimpleArray(10)
        self.direction = None
        self.moving = False
        self.floorsCallUp = StackSimpleArray(10)
        self.floorsCallDown = StackSimpleArray(10)
        self.CabRequest = StackSimpleArray(10)
        self.door = True

    def closeDoor(self):
        self.door = False
        time.sleep(1)
        print('Cerrando puerta')

    def openDoor(self):
        self.door = True
        time.sleep(1)
        print('Abriendo puerta')

    def move(self):
        if self.door is False:
            if self.direction == 'up':
                time.sleep(0.5)
                print('going up')
                while len(self.floorsCallUp.stk) != 0:
                    p = self.floorsCallUp.pop()
                    for i in range(self.currentFloor, p):
                        self.moving = True
                        self.currentFloor += 1
                        print('Piso actual: ', self.currentFloor)
                        time.sleep(1)
                    self.moving = False
                    self.direction = None
                    self.openDoor()
                    print('Piso alcanzado')
                self.closeDoor()
                if len(self.floorsCallDown.stk) != 0:
                    self.direction = 'down'
                    self.move()
            if self.direction == 'down':
                time.sleep(0.5)
                print('going down')
                while len(self.floorsCallDown.stk) != 0:
                    for i in range(self.floorsCallDown.pop(), self.currentFloor):
                        self.moving = True
                        self.currentFloor -= 1
                        print('Piso actual: ', self.currentFloor)
                        time.sleep(1)
                    self.moving = False
                    self.direction = None
                    self.openDoor()
                    print('Piso alcanzado')
                self.closeDoor()
                if len(self.floorsCallUp.stk) != 0:
                    self.direction = 'up'
                    self.move()

    def selectFloorFromCab(self, floor):
        if self.currentFloor < floor:
            self.floorsCallUp.push(floor)
            self.floorsCallUp.Sort()
            if self.direction is None:
                self.direction = 'up'
        elif self.currentFloor > floor:
            self.floorsCallDown.push(floor)
            self.floorsCallDown.SortReverse()
            if self.direction is None:
                self.direction = 'down'


screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
pygame.init()

elevador = elevator(10)


crashed = False
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                dir = 'up'
                elevador.selectDirFromFloor(dir)
            if event.key == pygame.K_DOWN:
                dir = 'down'
                elevador.selectDirFromFloor(dir)
            try:
                floor = int(event.unicode)
                elevador.selectFloorFromCab(floor)
                print(elevador.floorsCallUp.stk)
                print(elevador.floorsCallDown.stk)
            except:
                elevador.closeDoor()
                elevador.move()
    pygame.display.update()
    clock.tick(60)
pygame.quit()
quit()


