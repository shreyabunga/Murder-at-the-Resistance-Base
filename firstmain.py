import pygame #Pygame is what we are using yk
import time
import random

WIDTH, HEIGHT = 1500, 1000 #How big the window is
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) #Display the window
pygame.display.set_caption("20.5 Game") #Name at the top of the window

def main():
     # Initialize Pygame
    pygame.init()
    pygame.font.init()  # Ensure font module is initialized

    # Set up font for title
    font = pygame.font.SysFont("Arial", 74)
    title_text = font.render("Murder at the Resistance Base", True, (255, 0, 0))  # White color
    title_rect = title_text.get_rect(center=(WIDTH // 2, 100))  # Center at the top
    player = pygame.Rect((300,250,50,50)) #Size of the player
    run = True #Program is running
    while run: #This stuff happens while its running
        WIN.fill((0,0,0)) 
        WIN.blit(title_text, title_rect)

        pygame.draw.rect(WIN, (255,0,0), player) #Draws the player on the screen

        key = pygame.key.get_pressed()
        if key[pygame.K_a] == True:
            player.move_ip(-1,0) #Need to write a if statement for figuring out how to not make it go off the window (prevent it for going off screen too far to the left)
        elif key[pygame.K_d] == True:
            player.move_ip(1,0)
        elif key[pygame.K_w] == True:
            player.move_ip(0, -1)
        elif key[pygame.K_s] == True:
            player.move_ip(0,1)
        
        for event in pygame.event.get():#event.get is a list of all events
            if event.type == pygame.QUIT: #Ends program when user clicks the x
                run = False
                break
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()
