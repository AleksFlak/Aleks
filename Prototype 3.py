import pygame, time, random
pygame.init()

displayHeight = 800
displayWidth = 1000

gameDisplay = pygame.display.set_mode((displayWidth,displayHeight))

pygame.display.set_caption("Game Prototype")

background = pygame.image.load('./Images/backgroundcopy.png')

clock = pygame.time.Clock()
FPS = 10
            
class player(object):
    def __init__(self, x, y, width, height):
        self.winScreen = pygame.image.load('./Images/WinScreen.png')
        self.userRight = pygame.image.load('./Images/userRight.png')
        self.userLeft = pygame.image.load('./Images/userLeft.png')
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.left = True
        self.right = False
        self.down = False
        self.up = False
        self.standing = False
        self.x_vel = 5
        self.y_vel = 5
        self.collect1 = False
        self.collect2 = False
        self.collect3 = False
        self.numGenerated = False
        self.choiceGenerated = False
        self.health = 3
    def draw(self, gameDisplay):
        if self.standing or self.right or self.down or self.up:
            gameDisplay.blit(self.userRight, (self.x,self.y))
        elif self.left:
            gameDisplay.blit(self.userLeft, (self.x,self.y))
        self.hitbox = pygame.Rect(self.x+5, self.y+12, 73, 45)
        pygame.draw.rect(gameDisplay, (255,0,0), self.hitbox,2)

    def generation(self):
        self.digit1 = random.randint(0,9)
        self.digit2 = random.randint(0,9)
        self.sign = random.randint(1,3)

        while sub.numGenerated == False:
            if self.sign == 1:
                sub.numGenerated = True
                print('addition')
                Answer = self.digit1 + self.digit2
                print('What is',self.digit1,'add',self.digit2,'?')
            elif self.sign == 2:
                sub.numGenerated = True
                print('subtraction')
                if self.digit1 > self.digit2:
                    Answer = self.digit1 - self.digit2
                    print('What is',self.digit1,'minus',self.digit2,'?')
                else:
                    Answer = self.digit2 - self.digit1
                    print('What is',self.digit2,'minus',self.digit1,'?')
            elif self.sign == 3:
                sub.numGenerated = True
                print('multiplication')
                Answer = self.digit1 * self.digit2
                print('What is',self.digit1,'times',self.digit2,'?')

    def winning(self, gameDisplay):
        if sub.choiceGenerated == False:
            choice = random.randint(1,3)
            if choice == 1:
                collect1.answer = True
                sub.choiceGenerated == True
            if choice == 2:
                collect2.answer == True
                sub.choiceGenerated == True
            if choice == 3 :
                collect3.answer == True
                sub.choiceGenerated == True
       
        if self.hitbox.colliderect(collect1.hitbox) == True:
            collect1.standing = False
            collect1.collected = True
            self.collect1 = True
        if self.hitbox.colliderect(collect2.hitbox) == True:
            collect2.standing = False
            collect2.collected = True
            self.collect2 = True
        if self.hitbox.colliderect(collect3.hitbox) == True:
            collect3.standing = False
            collect3.collected = True
            self.collect3 = True

        if collect3.answer == True and self.collect3 == True or collect2.answer == True and self.collect2 == True or collect1.answer == True and self.collect1 == True:
            if self.x > 10 and self.x < 275:
                if self.y >0 and self.y < 80:
                    walls.clear()
                    gameDisplay.blit(self.winScreen, (0,0))
                    sub.x_vel=0
                    sub.y_vel=0
                    monster.y_vel = 0
                    monster.x_vel = 0
                    
    def collision(self):
        for wall in walls:   
            if self.hitbox.colliderect(wall.rect):
                if sub.up == True:
                    sub.y += sub.y_vel -4.3
                elif sub.down == True:
                    sub.y -= sub.y_vel -4.3
                if sub.right == True:
                    sub.x -= sub.x_vel -3.2
                elif sub.left == True:
                    sub.x += sub.x_vel -3.2
                    
        if self.hitbox.colliderect(monster.hitbox):
                if sub.up == True:
                    sub.y += sub.y_vel -2.5
                elif sub.down == True:
                    sub.y -= sub.y_vel -2.5
                if sub.right == True:
                    sub.x -= sub.x_vel -2
                elif sub.left == True:
                    sub.x += sub.x_vel -2
                    
class enemy(object):
    def __init__(self, x, y, width, height):
        self.Foe = pygame.image.load('./Images/Foe.png')
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.x_vel = 3
        self.y_vel = 3
        self.hitbox = (self.x + 10, self.y + 10, 100, 100)
        self.collect = False
        self.standing = True
        self.up = False
        self.down = False
        self.right = False
        self.left = False
        self.health = 1
        
    def draw(self, gameDisplay):
        if self.standing or self.up or self.down or self.right or self.left:
            gameDisplay.blit(self.Foe, (self.x,self.y))
        self.hitbox = pygame.Rect(self.x + 13, self.y + 7, 70, 87)
        pygame.draw.rect(gameDisplay, (255,0,0), self.hitbox,2)
        
    def movement(self):
        if self.hitbox.colliderect(sub.hitbox) == False:
            if sub.x > self.x:
                self.x += self.x_vel
                self.standing = False
                self.right = False
                self.left = True
                self.up = False
                self.down = False
            if sub.x < self.x:
                self.x -= self.x_vel
                self.standing = False
                self.right = True
                self.left = False
                self.up = False
                self.down = False
            if sub.y > self.y:
                self.y += self.y_vel
                self.standing = False
                self.up = False
                self.down = True
                self.right = False
                self.left = False
            if sub.y < self.y:
                self.y -= self.y_vel
                self.standing = False
                self.up = True
                self.down = False
                self.right = False
                self.left = False

    def collision(self):
        for wall in walls:   
            if self.hitbox.colliderect(wall.rect):
                if monster.up == True:
                    monster.y += monster.y_vel -2.5
                elif monster.down == True:
                    monster.y -= monster.y_vel -2.5
                if monster.left == True:
                    monster.x -= monster.x_vel -2
                elif monster.right == True:
                    monster.x += monster.x_vel -2

        if self.hitbox.colliderect(sub.hitbox):
                if monster.up == True:
                    monster.y += monster.y_vel -2.5
                elif monster.down == True:
                    monster.y -= monster.y_vel -2.5
                if monster.right == True:
                    monster.x -= monster.x_vel -2
                elif monster.left == True:
                    monster.x += monster.x_vel -2
                
class collectible(object):
    def __init__(self, x, y, width, height):
        self.Collectible = pygame.image.load('./Images/Collectible.png')
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x + 10, self.y + 10)
        self.collected = False
        self.standing = True
        self.answer = False
    def draw(self, gameDisplay):
        if self.standing:
            gameDisplay.blit(self.Collectible, (self.x,self.y))
        self.hitbox = pygame.Rect(self.x + 26, self.y + 22, 48, 45)
        pygame.draw.rect(gameDisplay, (255,0,0), self.hitbox,2)

class Wall(object):
    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)
    def draw(self, gameDisplay):
        for wall in walls:
            pygame.draw.rect(gameDisplay, (0,0,178), wall.rect)
            
def RedrawGameWindow():
    gameDisplay.blit(background, (0,0))
    collect1.draw(gameDisplay)
    collect2.draw(gameDisplay)
    collect3.draw(gameDisplay)    
    monster.draw(gameDisplay)
    sub.draw(gameDisplay)
    monster.collision()
    monster.movement()
    sub.generation()
    sub.collision()
    wall.draw(gameDisplay)
    sub.winning(gameDisplay)
    pygame.display.update()  

walls = []

level = [
"    XXXXXXXXXXXXXXXXXXXXXXXXX                                                                        ",
"    X                       X                                                                        ",
"    X                       X                   XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                     ",
"    X                       X                   X                              X                     ",
"    X                       X                   X                              X                     ", 
"    X                       X                   X                              X                     ",
"    X                       X                   X                              X                     ",
"    X                       X                   X                              X                     ",
"    X                       X                   X                              X                     ",
"    X                       X                   X          XXXXXXXXXXXXXXXXXXXXX                     ",
"    X                       X                   X          X                        XXXXXXXXXXXX     ",
"    X                       X                   X          X                        X          X     ",
"    X                       X                   X          X                        X          X     ",
"    X                       XXXXXXXXXXXXXXXXXXXXX          XXXXXXXX                 X          X     ",
"    X                                                             X                 X          X     ",
"    X                                                             X                 X          X     ",
"    X                                                             X                 X          X     ",
"    X                                                             XXXXXXXXXXXXXXXXXXX          X     ",
"    X                                                                                          X     ",
"    X                                                                                          X     ",
"    X                                                                                          X     ",
"    X                                                                                          X     ",
"    X                                                                                          X     ",
"    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX  ",
"       X                                      X     X                X                 X          X  ",        
"       X                                      X     X                X                 X          X  ",
"       X                                      X     X                X                 X          X  ",
"       X                                      X     X                X                 X          X  ",
"       X                                      X     X                X                 X          X  ",
"       X          XXXXXXXXXXXXXXXX            X     X                X                 X          X  ",
"       X          X              X            XXXXXXX                X                 X          X  ",
"       X          X              X                                   X                 X          X  ",
"       X          X              X                                   X                 X          X  ",
"       X          X              X                                   XXXXXXXXXXXXXXXXXXX          X  ",
"       X          XXXXXXXXXXXXXXXX                                                                X  ",
"       X                                                                                          X  ",
"       X                                                                                          X  ",
"       X                                                                                          X  ",
"       X                                                                                          X  ",
"       XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX  ",
]

x = y = 0
for row in level:
    for col in row:
        if col == "X":
            Wall((x,y))
        x+=10
    y+=20
    x= 0
    
sub = player(100, 10, 100,100)
monster = enemy(600, 60, 100,100)
collect1 = collectible(883, 470, 50, 43)
collect2 = collectible(850, 200, 50, 43)
collect3 = collectible(75, 470, 50, 43)
wall = Wall((x,y))

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
  
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and sub.x >=0:
        sub.x -= sub.x_vel
        sub.standing = False
        sub.right = False
        sub.down = False
        sub.up = False
        sub.left = True
    elif keys[pygame.K_RIGHT] and sub.x <= displayWidth -80:
        sub.x += sub.x_vel
        sub.left = False
        sub.standing = False
        sub.down = False
        sub.up = False
        sub.right = True
    elif keys[pygame.K_DOWN] and sub.y < displayHeight - 65:
        sub.y +=sub.y_vel
        sub.left = False
        sub.right = False
        sub.standing = False
        sub.up = False
        sub.down = True
    elif keys[pygame.K_UP] and sub.y > -10:
        sub.y -=sub.y_vel
        sub.left = False
        sub.right = False
        sub.standing = False
        sub.down = False
        sub.up = True
    else:
        sub.left = False
        sub.right = False
        sub.down = False
        sub.up = False
        sub.standing = True

    RedrawGameWindow()
    clock.tick(FPS)

pygame.quit()
