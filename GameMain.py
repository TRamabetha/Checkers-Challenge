import pygame
from Assets.constants import WIDTH, HEIGHT
from Assets.board import Board

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')

FPS = 60

def main():
    run = True
    clock = pygame.time.Clock()
    board = Board() 
    
    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
        
        board.draw_blocks(WIN)
        pygame.display.update()
        
    pygame.quit()
    
main()