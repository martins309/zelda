import pygame

def __init__pygame():
    red = (255, 0, 0)  

    WIDTH = 800
    HEIGHT = 600
def pygame_display_set():
    screen = pygame_display_set_mode((WIDTH, HEIGHT))
    clock = pygame_time_Clock()

    running = True
    while running:
        clock_tick(30)
        for event in pygame_display_set():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(red)
     

        pygame.quit()