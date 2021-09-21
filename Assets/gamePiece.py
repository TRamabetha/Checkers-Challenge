import pygame
from .constants import GREY, SQUARE_SIZE

class GamePiece:
    
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.isCrowned = False
        self.posX = 0
        self.posY = 0
        self.calc_pos()
    
    def calc_pos(self):
        self.posX = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.posY = SQUARE_SIZE * self.row + SQUARE_SIZE // 2
        
    def crown_piece(self):
        self.isCrowned = True
        
    def draw(self, win):
        if self.isCrowned:
            self.draw_crown_piece(win)
        else:
            pygame.draw.circle(win, GREY,(self.posX, self.posY), SQUARE_SIZE//2 - 14)
            pygame.draw.circle(win, self.color,(self.posX, self.posY), SQUARE_SIZE//2 - 15)

    def draw_crown_piece(self, win):
        pygame.draw.circle(win, GREY,(self.posX, self.posY), SQUARE_SIZE//2 - 14)
        pygame.draw.circle(win, GREY,(self.posX, self.posY), SQUARE_SIZE//2 - 15)
        pygame.draw.circle(win, self.color,(self.posX, self.posY), SQUARE_SIZE//2 - 17)
        pygame.draw.circle(win, GREY,(self.posX, self.posY), SQUARE_SIZE//2 - 19)
        pygame.draw.circle(win, self.color,(self.posX, self.posY), SQUARE_SIZE//2 - 21)
        pygame.draw.circle(win, GREY,(self.posX, self.posY), SQUARE_SIZE//2 - 22)
        pygame.draw.circle(win, self.color,(self.posX, self.posY), SQUARE_SIZE//2 - 24)
        

    def move(self,row,col):
        self.row = row
        self.col = col
        self.calc_pos()

    def __repr__(self):
        return str(self.color)