import pygame
from network import Network

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

        self.update()

    def update(self):
        #Redefines the rect, while the if-statements only redifines the self.values. Updates the rect in draw()
        self.rect = (self.x, self.y, self.width, self.height)

#Takes the position as a string, splits it by comma, and returns it as a touple wchich we can use
def read_pos(str):
    #Has to check if the string is not empty - It starts off empty, so we have to check before we can run the program i think
    if str is not None:
        str = str.split(",")
        return int(str[0]), int(str[1])

#Makes the position out of a touple
def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])

#Pygame window
def redrawWindow(win,player, player2):
    win.fill((255,255,255))
    player.draw(win)
    player2.draw(win)
    pygame.display.update()

#main loop - This is always running while the game is running - Asks the server for information
def main():
    run = True

    n = Network()
    startPos = read_pos(n.getPos())

    p = Player(startPos[0], startPos[1],100,100,(0,255,0))
    p2 = Player(50,50,100,100,(255,0,0))
    #Create a clock so we can control the framerate of the game
    clock = pygame.time.Clock()

    while run:
        #Clock.tick() sets the framerate of the loop - Higher number = higher framerate = faster parsing of actions = faster game
        clock.tick(60)

        #Algorithm to send current clients position, and recieving the other clients position
        p2Pos = read_pos(n.send(make_pos((p.x, p.y))))
        p2.x = p2Pos[0]
        p2.y = p2Pos[1]
        p2.update()

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        p.move()
        redrawWindow(win, p, p2)

main()