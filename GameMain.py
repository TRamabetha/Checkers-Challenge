import pygame
from Assets.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED
from Assets.game import Game

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')

FPS = 60

def get_onclick_row_col(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN) 
    
    if game.winner() != None:
        print(game.winner())
        run = False
    
    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_onclick_row_col(pos)
                game.select(row, col)
        
        game.update()
        
    pygame.quit()
    
main()