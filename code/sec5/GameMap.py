import pygame
from Tile import *
from Tileset import *
import json
class GameMap:
    def __init__(self, tileset):
        self.tileset = tileset
        self.player = None
        #janela de visualização
        self.window = [0,0,400,300]
        #'matriz' de tiles
        self.cells = []
        #numero de tiles de altura e largura
        self.width  = 0
        self.height = 0
        self.widthPixels = 0
        self.heigthPixels = 0
        
    def loadFromFile(self, file):
        mapDict = json.load(open(file,'rt'))
        print(mapDict)
        self.tileset = Tileset(mapDict['tileFile'], int(mapDict['tileSize']))
        self.setSize(int(mapDict['width']), int(mapDict['height']))
        self.setWindow([0,0,int(mapDict['windowWidth']), int(mapDict['windowHeight'])])
        for i in range(0, len(mapDict['mapCels'])):
            for j in range(0, len(mapDict['mapCels'][i])):
                self.cells[i][j] = self.tileset.getTile(mapDict['mapCels'][i][j])



    def update(self):
        pass
    def getCell(self, line, col):
        return self.cells[line][col]
    def setWindow(self, w):
        self.window = w
    def moveWindow(self, d):
        self.window[0] += d[0]
        self.window[1] += d[1]
        if self.window[0] <= 0:
            self.window[0] = 0
        if (self.window[0]+self.window[2]) > self.widthPixels -1:
            self.window[0] = self.widthPixels - 1 -self.window[2]
        if self.window[1] < 0:
            self.window[1] = 0
        if (self.window[1] + self.window[3]) > self.heigthPixels-1:
            self.window[1] = self.heigthPixels - 1 - self.window[3]

    def getWindow(self):
        return self.window

    def setSize(self, width, height):
        self.width = width
        self.height = height
        for i in range(0, height):
            line = []
            for j in range(0, width):
                line.append(None)
            self.cells.append(line)
        self.widthPixels = self.width  * self.tileset.getSize()
        self.heigthPixels = self.height * self.tileset.getSize()
    def setCell(self, line, col, tile):
        if len(self.cells) < line or len(self.cells[0]) < col:
            print("Line or Col greater than map size")
            exit()
        self.cells[line][col] = tile

    def getTileset(self):
        return self.tileset

    def render(self, dest):
        startY  = int (self.window[1]/self.tileset.getSize())
        endY = int ( (self.window[1] + self.window[3])/self.tileset.getSize())

        startX = int (self.window[0]/self.tileset.getSize())
        endX   = int ( (self.window[0] + self.window[2])/self.tileset.getSize())

        print("tiles? " + str([startX, endX,startY,endY]))
        offsetY = int (self.window[1]%self.tileset.getSize())
        offsetX = int (self.window[0]%self.tileset.getSize())

        print("window: " + str(self.window))
        yScreenPos = 300 - self.getTileset().getSize()
        i = startY
        while i <=endY:
        #for i in range(startY, endY-1, -1):
            for j in range(startX, endX+1):
                cell = self.getCell(i,j)
                if cell != None:
                    screenPos = [(j-startX) * self.getTileset().getSize() - offsetX,0]

                    screenHeightPixels = self.window[3] - self.window[1]
                    screenPos[1] =   yScreenPos + offsetY#screenHeightPixels - (offsetY + (i-startY) * self.getTileset().getSize()) - self.getTileset().getSize()
                    dest.blit(cell.getImage(), screenPos)
            yScreenPos-=self.getTileset().getSize()
            i = i +1
