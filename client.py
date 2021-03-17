import pygame
pygame.init()

width = 500
height = 500
win = pygame.display.set_mode(width, height)
pygame.display.set_caption("Client")

#The clients number
clientNumber = 0

class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self. height = height
        self.width = width
        self.color = color
        #This is only needed for the server tests - Makes it easier to draw the rectangles
        self.rect = (x,y,width,height)
        self.vel = 3

    #Draws the "characters"/players
    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    #Defines the players movement
    def move(self):
        #Checks if keys are being pressed by returning a 1 or a 0 - 1 is key press. Can press multiple keys - Better than checking for events, like we do in main()
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.vel

        if keys[pygame.K_RIGHT]:
            self.x += self.vel

        if keys[pygame.K_UP]:
            self.y -= self.vel

        if keys[pygame.K_DOWN]:
            self.y += self.vel



#Pygame window
def redrawWindow(player, win):
    player.draw(win)
    win.fill(255,255,255)
    pygame.display.update()


#main loop - This is always running while the game is running - asks the server for information
def main():
    run = True
    p = Player(50, 50, 100, 100, (255, 0, 0))

    #Basic for every pygame - Makes sure the game can close
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        p.move()
        redrawWindow(win, p)

main()