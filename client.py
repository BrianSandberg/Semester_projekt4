import pygame

width = 500
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

#The clients number on the server
clientNumber = 0


class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        #This is only needed in the current game - might not be needed later on
        self.rect = (x,y,width,height)
        #Speed of character
        self.vel = 3

    #Draws the characters/players
    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    #Defines the players movement
    def move(self):
        keys = pygame.key.get_pressed()

        #Checks for key presses - Can detect multiple presses - Better than checking for events like we do in main
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.vel

        if keys[pygame.K_RIGHT] and self.x < width-self.width:
            self.x += self.vel

        if keys[pygame.K_UP] and self.y > 0:
            self.y -= self.vel

        if keys[pygame.K_DOWN] and self.y < height-self.height:
            self.y += self.vel

        #Redefines the rect, while the if-statements only redifines the self.values. Updates the rect in draw()
        self.rect = (self.x, self.y, self.width, self.height)

#Pygame window
def redrawWindow(win,player):
    win.fill((255,255,255))
    player.draw(win)
    pygame.display.update()

#main loop - This is always running while the game is running - Asks the server for information
def main():
    run = True
    p = Player(50,50,100,100,(0,255,0))
    #Create a clock so we can control the framerate of the game
    clock = pygame.time.Clock()

    while run:
        #Clock.tick() sets the framerate of the loop - Higher number = higher framerate = faster parsing of actions = faster game
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        p.move()
        redrawWindow(win, p)

main()