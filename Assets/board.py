import pygame
from .constants import BLACK, ROWS, RED, SQUARE_SIZE

class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.red_pieces = self.white_pieces = 12
        self.red_crowns = self.white_crowns = 0
    
    def draw_blocks(self,win):
        win.fill(BLACK)
        
        for row in range(ROWS):
            for col in range(row%2, ROWS, 2):
                pygame.draw.rect(win, RED, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                