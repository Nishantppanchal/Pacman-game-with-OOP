# Imports required libraries
from JMSSGraphics import *
import random

# Variable to scale the game window
scaler = int(input("enter the scaling multiple:"))

# List of all the coin objects in the maze
coinList = []
# List of all the ghost objects in the maze
ghostList = []
# A map of Quaternary (4 numbers - 0,1,2,3) data
pathBlockList = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], 
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0], 
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0], 
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0], 
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], 
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0], 
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0], 
    [0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0], 
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 2, 2, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 3, 3, 3, 3, 3, 3, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0], 
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 3, 3, 3, 3, 3, 3, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 2, 2, 2, 2, 2, 2, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0], 
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], 
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0], 
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0], 
    [0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0], 
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0], 
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0], 
    [0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0], 
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], 
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], 
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

# Defines the width and height of the game window
screenWidth = 280 * scaler
screenHeight = 360 * scaler
# Sets the screen to the first screen
gameMode = 0
# Defines the size of pacman
pacManHeight = 10 * scaler
pacManWidth = 10 * scaler
# Defines the speed of all the moving objects
speed = 10 * scaler

# Defines the function that check if the object can be on that 'tile' or not
def pathCheck(self ,xValue, yValue):
    # Converts x and y on the game window to x and y on the Quaternary database
    modifiedX = int(xValue/pacManHeight)
    modifiedY = int(yValue/pacManWidth)

    # Teleport objects from on side of the 'tunnel' path thing to the other
    if modifiedX >= 29:
        self.xpos = 0
        self.ypos = 140 * scaler
    if modifiedX <= -1:
        self.xpos = 280 * scaler
        self.ypos = 140 * scaler
    
    else:
        # Prevent error if teleported
        try:
            # If on 0 value, returns False
            if pathBlockList[modifiedY][modifiedX] == 0:
                return False
            # If on 1 value, returns True
            if pathBlockList[modifiedY][modifiedX] == 1:
                return True
            # Prevent error when function used on pacman, as they don't have the attribute 'exit'
            try:
                # If exited that it prevents the re enter to the ghost box, by returning false
                if self.exit == 1:    
                    if pathBlockList[modifiedY][modifiedX] == 2 or 3:
                        return False
            except:
                # If it does not have the 'exit' attribute, it return the string "ghost only area"
                if pathBlockList[modifiedY][modifiedX] == 2 or 3:
                        return "ghost only area"
        except:
            pass

# Defines the colision funciton
def collisionChecker(object1, object2):
    # Checks if object colides on any four side collide
    if (object1.xpos == object2.xpos and object1.ypos == object2.ypos) or (object1.xpos + (10 * scaler) == object2.xpos and object1.ypos == object2.ypos) or (object1.xpos == object2.xpos + (10 * scaler) and object1.ypos == object2.ypos) or (object1.xpos == object2.xpos and object1.ypos + (10 * scaler) == object2.ypos) or (object1.xpos == object2.xpos and object1.ypos == object2.ypos + (10 * scaler)):
        # If they do true is returned
        return True

# Defines the game window
jmss = Graphics(width = screenWidth, height = screenHeight, title = "Game", fps = 10)

# Preload all the images to the RAM
pacManImage = jmss.loadImage("pacMan.png")
pacGirlImage = jmss.loadImage("pacGirl.png")
background = jmss.loadImage("Maze.png")
coinImage = jmss.loadImage("coin.png")
ghostImage1 = jmss.loadImage("ghostRed.png")
ghostImage2 = jmss.loadImage("ghostBlue.png")
ghostImage3 = jmss.loadImage("ghostYellow.png")
ghostImage4 = jmss.loadImage("ghostPink.png")
ghostImage5 = jmss.loadImage("ghostRed.png")
ghostImage6 = jmss.loadImage("ghostBlue.png")
ghostImage7 = jmss.loadImage("ghostYellow.png")
ghostImage8 = jmss.loadImage("ghostPink.png")
ghostImage9 = jmss.loadImage("ghostRed.png")
ghostImage10 = jmss.loadImage("ghostBlue.png")
ghostImage11 = jmss.loadImage("ghostYellow.png")
ghostImage12 = jmss.loadImage("ghostPink.png")
heart = jmss.loadImage("heart.png")

# Create the class pacMan
class pacMan():
    def __init__(self, x, y, image):
        # Defines all the attributes
        self.image = image
        self.height = pacManHeight
        self.width = pacManWidth
        self.xpos = x
        self.ypos = y
        self.xvel = 0
        self.yvel = 0
        self.score = 0
        self.lives = 0
        self.active = 0

    # Defines the funciton draw
    def draw(self):
        # Draws the pacMan 
        jmss.drawImage(self.image, x = self.xpos, y = self.ypos, height = self.height, width = self.width)

    # Defines the function that moves pacman
    def movePacMan(self,keyU,keyD,keyR,keyL):
        # Checks if keyU is pressed
        if jmss.isKeyPressed(keyU):
            # Checks if the next is valid 'tile'
            if pathCheck(self, self.xpos, self.ypos + (10 * scaler)) == True:
                self.yvel = speed
                self.xvel = 0
        # Checks if keyD is pressed
        if jmss.isKeyPressed(keyD):
            # Checks if the next is valid 'tile'
            if pathCheck(self, self.xpos, self.ypos - (10 * scaler)) == True:
                self.yvel = -speed
                self.xvel = 0
        # Checks if keyR is pressed
        if jmss.isKeyPressed(keyR):
            # Checks if the next is valid 'tile'
            if pathCheck(self, self.xpos + (10 * scaler), self.ypos) == True:
                self.yvel = 0
                self.xvel = speed
        # Checks if keyL is pressed
        if jmss.isKeyPressed(keyL):
            # Checks if the next is valid 'tile'
            if pathCheck(self, self.xpos - (10 * scaler), self.ypos) == True:
                self.yvel = 0
                self.xvel = -speed
        
        # For debugging purposes
        #if jmss.isKeyPressed(KEY_SPACE):
            #self.yvel = 0
            #self.xvel = 0

        # Adds/substracts the xpos from xvel and ypos from yvel
        self.xpos += self.xvel
        self.ypos += self.yvel

        # Stops the object going into a '0' tile 
        if pathCheck(self, self.xpos, self.ypos) == False:
            self.xpos -= self.xvel
            self.ypos -= self.yvel

# Creates the class coin
class coin():
    def __init__(self, xValue, yValue):
        # Defines the class's attributes
        self.image = coinImage
        self.xpos = xValue
        self.ypos = yValue
    
    # Defines the function draw
    def draw(self):
        # Draws the coin
        jmss.drawImage(self.image, x = self.xpos + (2.5 * scaler), y = self.ypos + (2.5 * scaler), height = 5 * scaler, width = 5 * scaler)

    # Defines the function eatCoin
    def eatCoin(self, pacMan):
        # Need to do this try and except thing as without it, the code crashes when the two pacman eat the same coin at the same time. (Both get the coin)
        try:
            # If the xpos of the coin and the pacman and ypos of the coin and the pacman are the same, then the coin is eaten
            if pacMan.xpos == self.xpos and pacMan.ypos == self.ypos:
                # Removes it from the list
                coinList.remove(self)
                # Add one to the score
                pacMan.score += 1
        except:
            # Add one to the score
            pacMan.score += 1

# Creates the class ghost
class ghost():
    def __init__(self, ghostImage, xValue, yValue):
        # Defines the class's attributes
        self.image = ghostImage
        self.xpos = xValue
        self.ypos = yValue
        self.xvel = 0
        self.yvel = speed
        self.exit = 0
    
    # Defines the function draw
    def draw(self):
        # Draws the object
        jmss.drawImage(self.image, x = self.xpos, y = self.ypos, height = 10 * scaler, width = 10 * scaler)

    # Defines the function move
    def move(self):
        # Moves the ghost
        self.xpos += self.xvel
        self.ypos += self.yvel

        # If the exits the 'ghost box'
        if (self.xpos == 130*scaler or self.xpos == 140*scaler) and self.ypos == 120*scaler:
            # Sets the attribute, 'exit', to exit
            self.exit = 1

        # Makes a list for the possible moves
        possibleMoves = []

        # Checks if the next tile is 'allowed'
        if pathCheck(self, self.xpos, self.ypos + (10 * scaler)) != False:
            # If already moving in the opposite direction, it reduce the probability
            if self.yvel < 0:    
                # Append the direction in the list
                possibleMoves.append('U')
            # If not moving in the opposite direction, it increases the probability
            if self.yvel >= 0:   
                # Append the direction in the list
                 possibleMoves.append('U')
                 possibleMoves.append('U')
                 possibleMoves.append('U')
                 possibleMoves.append('U')
                 possibleMoves.append('U')
                 possibleMoves.append('U')
        if pathCheck(self, self.xpos, self.ypos - (10 * scaler)) != False:
            # If already moving in the opposite direction, it reduce the probability
            if self.yvel > 0:
                # Append the direction in the list    
                possibleMoves.append('D')
            # If not moving in the opposite direction, it increases the probability
            if self.yvel <= 0:   
                # Append the direction in the list
                 possibleMoves.append('D')
                 possibleMoves.append('D')
                 possibleMoves.append('D')
                 possibleMoves.append('D')
                 possibleMoves.append('D')
                 possibleMoves.append('D')

        if pathCheck(self, self.xpos + (10 * scaler), self.ypos) != False:
            # If already moving in the opposite direction, it reduce the probability
            if self.xvel < 0:    
                # Append the direction in the list
                possibleMoves.append('R')
            # If not moving in the opposite direction, it increases the probability
            if self.xvel >= 0:   
                # Append the direction in the list
                 possibleMoves.append('R')
                 possibleMoves.append('R')
                 possibleMoves.append('R')
                 possibleMoves.append('R')
                 possibleMoves.append('R')
                 possibleMoves.append('R')
        if pathCheck(self, self.xpos - (10 * scaler), self.ypos) != False:
            # If already moving in the opposite direction, it reduce the probability
            if self.xvel > 0:    
                # Append the direction in the list
                possibleMoves.append('L')
            # If not moving in the opposite direction, it increases the probability
            if self.xvel <= 0:   
                # Append the direction in the list
                 possibleMoves.append('L')
                 possibleMoves.append('L')
                 possibleMoves.append('L')
                 possibleMoves.append('L')
                 possibleMoves.append('L')
                 possibleMoves.append('L')
            
        # Select a random move
        pickedMove = random.randint(0, len(possibleMoves)-1)

        # If up is selected:
        if possibleMoves[pickedMove] == 'U':
            # yvel set to speed
            self.yvel = speed
            # xvel set to 0
            self.xvel = 0
        # If down is selected:
        if possibleMoves[pickedMove] == 'D':
            # yvel set to -speed
            self.yvel = -speed
            # xvel set to 0
            self.xvel = 0
        # If right is selected:
        if possibleMoves[pickedMove] == 'R':
            # yvel set to 0
            self.yvel = 0
            # xvel set to speed
            self.xvel = speed
        # If left is selected:
        if possibleMoves[pickedMove] == 'L':
            # yvel set to 0
            self.yvel = 0
            # xvel set to -speed
            self.xvel = -speed

# Make the two pacman objects
pacMan1 = pacMan(10*scaler, 10*scaler, pacManImage)
pacMan2 = pacMan(screenWidth-(10*scaler*2), 10*scaler, pacGirlImage)

# Creates coin objects where there are 1 on the maps
for a in range(0,len(pathBlockList)):
    for b in range(0, len(pathBlockList[a])):
        if pathBlockList[a][b] == 1 and (a != 1 or b != 1):
            # Creates the objects
            Coin = coin(b*(10 * scaler), a*(10 * scaler))
            # Appends to the list
            coinList.append(Coin)

# Makes are counter
imageNumberCounter = 1
# Creates ghosts objects where there are 3 on the maps
for a in range(0,len(pathBlockList)):
    for b in range(0, len(pathBlockList[a])):
        if pathBlockList[a][b] == 3:
            Ghost = ghost(globals()["ghostImage" + str(imageNumberCounter)], b*(10 * scaler), a*(10 * scaler))
            # Creates the objects
            ghostList.append(Ghost)
            # Appends to the list
            imageNumberCounter += 1

@jmss.mainloop
def play_game():
    # Defines global variables
    global gameMode

    # Clears screen
    jmss.clear(1,1,1,1)

    # If menu is in mode is 0
    if gameMode == 0:
        # Draws text
        jmss.drawText("PACMAN RIP OFF!", x=(screenWidth/2)-(120*scaler), y=screenHeight-(40*scaler), fontSize= 20*scaler,color=(0.1, 0.9, 0.3, 1))
        jmss.drawText("Press up arrow to activite player1", x=(screenWidth/2)-(120*scaler), y=screenHeight-(80*scaler), fontSize= 10*scaler,color=(0.1, 0.9, 0.3, 1))
        jmss.drawText("Press W to activite player2", x=(screenWidth/2)-(120*scaler), y=screenHeight-(120*scaler), fontSize= 10*scaler,color=(0.1, 0.9, 0.3, 1))
        jmss.drawText("Press backspace to deactivate all player", x=(screenWidth/2)-(120*scaler), y=screenHeight-(160*scaler), fontSize= 10*scaler,color=(0.1, 0.9, 0.3, 1))
        jmss.drawText("Press enter to start game", x=(screenWidth/2)-(120*scaler), y=screenHeight-(200*scaler), fontSize= 10*scaler,color=(0.1, 0.9, 0.3, 1))

        # Activates pacman if certain keys are pressed
        if jmss.isKeyPressed(KEY_UP):
            pacMan1.active = 1
            pacMan1.lives = 3
        if jmss.isKeyPressed(KEY_W):
            pacMan2.active = 1
            pacMan2.lives = 3
        
        # Resets the selection
        if jmss.isKeyPressed(KEY_BACKSPACE):
            pacMan1.active = 0
            pacMan1.live = 0
            pacMan2.active = 0
            pacMan2.live = 0

        # Set games mode to 1 if enter is pressed
        if jmss.isKeyPressed(KEY_ENTER):
            gameMode = 1
        
        # Draws the respective pacman is it is selected
        if pacMan1.active == 1:
            jmss.drawImage(pacManImage, x = 50*scaler, y = 50*scaler, height = 30*scaler, width = 30*scaler)
        if pacMan2.active == 1:
            jmss.drawImage(pacGirlImage, x = screenWidth-(50*scaler+30*scaler), y = 50*scaler, height = 30*scaler, width = 30*scaler)
    
    # If menu is in mode 1
    if gameMode == 1:
        # Draws background
        jmss.drawImage(background, x = 0, y = 0, height = screenHeight-(50*scaler), width = screenWidth)
        # For all the coins objects in coinList, coins are drawn
        for coins in coinList:
            coins.draw()
        
        # If the pacman has more then 0 lives, it is drawn
        if pacMan1.lives > 0:
            pacMan1.draw()
        if pacMan2.lives > 0:
            pacMan2.draw()

        # If the 1st pacman is active
        if pacMan1.active == 1:
            # Draws the text
            jmss.drawText("P1:", x=5, y=screenHeight-(10*2*scaler), fontSize= 10*scaler,color=(0.1, 0.9, 0.3, 1))
            jmss.drawText(str(pacMan1.score), x=5, y=screenHeight- 2*(10*2*scaler) + 5*scaler, fontSize= 10*scaler,color=(0.1, 0.9, 0.3, 1))
            # Draws the hearts
            for r in range(0,pacMan1.lives):
                jmss.drawImage(heart, x = (r*15*scaler) + (5*scaler), y = screenHeight-(50*scaler) + 5, height = 10*scaler, width = (28/3)*scaler)

        # If the 2nd pacman is active
        if pacMan1.active == 1:    
            # Draw text
            jmss.drawText("P2:", x=screenWidth-(25*scaler), y=screenHeight-(10*2*scaler), fontSize= 10*scaler,color=(0.1, 0.9, 0.3, 1))
            jmss.drawText(str(pacMan2.score), x=screenWidth-(30*scaler), y=screenHeight- 2*(10*2*scaler) + 5*scaler, fontSize= 10*scaler,color=(0.1, 0.9, 0.3, 1))
            # Draw hearts
            for r in range(0,pacMan2.lives):
                jmss.drawImage(heart, x = screenWidth - ((r*15*scaler) + (15*scaler)), y = screenHeight-(50*scaler) + 5, height = 10*scaler, width = (28/3)*scaler)

        # For all the ghosts in ghostlist
        for Ghost in ghostList:
            # Draws the ghost
            Ghost.draw()
            # Moves the ghost
            Ghost.move()
        
        # For all the ghost
        for y in range(0, len(ghostList)):
            # My best attempt to prevent overlap of ghost. It does not fully work, but it does kind of make them bounce of once transposed.
            for z in range(0, len(ghostList)):
                # Prevent the same ghost being compared to itself
                if ghostList[y] != ghostList[z]:
                    # Checks for collision
                    if collisionChecker(ghostList[y], ghostList[z]) == True:
                        # If there is collision, the velocities are reversed
                        ghostList[y].xvel *= -1
                        ghostList[z].xvel *= -1

                        ghostList[y].yvel *= -1
                        ghostList[z].yvel *= -1

            # Checks for collision with pacman1
            if collisionChecker(ghostList[y], pacMan1) == True and pacMan1.lives > 0:
                # If there is a collison
                # A live is substracted
                pacMan1.lives -= 1
                # The pacman is teleport
                pacMan1.xpos = 10*scaler
                pacMan1.ypos = 10*scaler
                # yvel and xvel set to 0
                pacMan1.xvel = 0
                pacMan1.yvel = 0
            if collisionChecker(ghostList[y], pacMan2) == True and pacMan2.lives > 0:
                # If there is a collison
                # A live is substracted
                pacMan2.lives -= 1
                # The pacman is teleport
                pacMan2.xpos = screenWidth - 20*scaler
                pacMan2.ypos = 10*scaler
                # yvel and xvel set to 0
                pacMan2.xvel = 0
                pacMan2.yvel = 0
            
        # Allows pacman to move with it specific keys
        pacMan1.movePacMan(KEY_UP, KEY_DOWN, KEY_RIGHT, KEY_LEFT)
        pacMan2.movePacMan(KEY_W, KEY_S, KEY_D, KEY_A)

        # Alls pacman to eat the coins
        for coins in coinList:
            # If pacMan has lost all it's live, it will not be able to eat the coins
            if pacMan1.lives > 0:
                coins.eatCoin(pacMan1)
            if pacMan2.lives > 0:
                coins.eatCoin(pacMan2)
        
        # If all the pacman's die or are not activated:
        if ((pacMan1.lives <= 0 or pacMan1.active == 0) and (pacMan2.lives <= 0 or pacMan2.active == 0)) or len(coinList) == 0:
            # It they are all not activated
            if pacMan1.active == 0 and pacMan2.active == 0:
                # Return to menu screen 1
                gameMode = 1
            # Else the other specifications are met
            else:
                # Go to menu screen 3
                gameMode = 3

    # The final menu (3rd)
    if gameMode == 3:
        # If pacman1's score is higher then pacman2's
        if pacMan1.score > pacMan2.score:
            # Draw text
            jmss.drawText("Player1", x=(screenWidth/2)-(115*scaler), y=screenHeight-(80*scaler), fontSize= 50*scaler,color=(0.1, 0.9, 0.3, 1))
            jmss.drawText("Wins!", x=(screenWidth/2)-(80*scaler), y=screenHeight-(150*scaler), fontSize= 50*scaler,color=(0.1, 0.9, 0.3, 1))
            # Draw image of winner
            jmss.drawImage(pacManImage, x = (screenWidth/2)-(30*scaler), y = 100*scaler, height = 30*scaler, width = 30*scaler)

        # If pacman2's score is higher then pacman1's
        if pacMan1.score < pacMan2.score:
            # Draw text
            jmss.drawText("Player2", x=(screenWidth/2)-(115*scaler), y=screenHeight-(80*scaler), fontSize= 50*scaler,color=(0.1, 0.9, 0.3, 1))
            jmss.drawText("Wins!", x=(screenWidth/2)-(80*scaler), y=screenHeight-(150*scaler), fontSize= 50*scaler,color=(0.1, 0.9, 0.3, 1))
            # Draw image of winner
            jmss.drawImage(pacGirlImage, x = (screenWidth/2)-(30*scaler), y = 100*scaler, height = 30*scaler, width = 30*scaler)

        # If the scores are the same
        if pacMan1.score == pacMan2.score:
            # Draw some text
            jmss.drawText("Draw", x=(screenWidth/2)-(80*scaler), y=screenHeight-(150*scaler), fontSize= 50*scaler,color=(0.1, 0.9, 0.3, 1))

# Run the gamewindow
jmss.run()