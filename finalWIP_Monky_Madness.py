#####   funny block game   #####
#####        by Zain McCoy #####
#####       idea by Nathan #####

##### Initial

### config

app.maxFails = 100 # default = 100; decrease to speed up loading times

### app properties & defined values

app.maxBlocks = 10 # default = 10
app.maxThrees = 1 # default = 1
app.secsPerLvl = 5 # default = 5; Seconds per level until mobilization
app.boundingRectOpacity = 0 # default = 0

app.stepsPerSecond = 100
app.background = gradient('sandyBrown', 'peru')
app.steps = 0
app.seconds = 0
app.activeBlock = None
app.won = False
app.level = 1
app.IQ = 101
app.mouseScalar = 35 / 224

cursorURL = 'https://i.imgur.com/U08Hj53.png'
handURL = 'https://i.imgur.com/rOedRe5.png'
accessibilityURL = 'https://scalar.usc.edu/works/aaeebl-digital-ethics-principlesversion-1/media/Accessibility.png'
shuffleURL = 'https://static.thenounproject.com/png/5050-200.png'

### board
exit = Rect(0, 0, 40, 40, fill='saddleBrown', border='black', visible = False)
board = Group(
    Rect(200, 40, 240, 240, align='top', fill=gradient('sienna', 'saddleBrown')),
    Line( 80, 160, 320, 160, lineWidth=240, opacity=10, dashes=(2, 38)),
    Line(200,  40, 200, 280, lineWidth=240, opacity=10, dashes=(2, 38))
    )
boundingRect = Rect(200, 160, 240, 40, align='center', fill='yellow',
                    opacity=app.boundingRectOpacity, visible=False)
board.add(boundingRect)
blocks = Group()
Line( 80,  39, 320,  41)
Line( 81,  40,  81, 280)
Line(319,  40, 319, 280)
player = Rect(45, 45, 30, 70, fill='red', border='black')
leftLine = Line(81, 279, 82, 279)
rightLine = Line(318, 279, 319, 279)
exitLine = Line(40, 279, 80, 279)
levelCounter = Label('Level: ' + str(app.level), 395, 395, align='bottom-right', size=20)

### groups
buttons = Group()
startScreen = Group()
startButtons = Group()
mice = Group()
ad = Group()

### buttons
nextButton = Group(
    Rect(360, 360, 35, 10, align='right', fill='lime',
         border='black', borderWidth=1.5),
    RegularPolygon(360, 360, 20, 3, align='left', rotateAngle=90,
                   fill='lime', border='black', borderWidth=1.5),
    Rect(360, 360, 4, 7, align='center', fill='lime'),
    Rect(360, 360, 80, 40, align='center', fill=None)
    )
buttons.add(nextButton)
nextButton.visible = False

prohibitedSymbol1 = Group(
    Circle(10+35/2, 10+35/2, 20, fill=None, border='red', borderWidth=5),
    Line(13.36, 13.36, 41.64, 41.64, fill='red', lineWidth=5)
    )
prohibitedSymbol2 = Group(
    Circle(395-45/2, 5+45/2, 20, fill=None, border='red', borderWidth=5),
    Line(358.36, 41.64, 386.64, 13.36, fill='red', lineWidth=5)
    )

mouseToggleButton = Group(
    Image(cursorURL, 10, 10, width=35, height=35, opacity=50),
    prohibitedSymbol1
    )
accessibilityButton = Group(
    Image(accessibilityURL, 395, 5, align='top-right', width=45, height=45, opacity=50),
    prohibitedSymbol2
    )
prohibitedSymbol2.visible = False
buttons.add(mouseToggleButton, accessibilityButton)
shuffleButton = Image(shuffleURL, 5, 398, align='bottom-left', width=30, height=30, visible = False)

### mice
cursor = Image(cursorURL, 400, 400, width=(224*app.mouseScalar), height=(224*app.mouseScalar))
hand = Image(handURL, 400, 400, width=(199*app.mouseScalar), height=(245*app.mouseScalar))
mice.add(cursor, hand)
app.mouse = cursor

### ad
adWhiteHeader = Line(0, 40, 400, 40, lineWidth=80, fill='white',
                     opacity=90, visible=False)
adTextL1 = Label('Sample Text', 200, 30, size=25, visible=False)
adTextL2 = Label('Sample Text', 200, 60, size=25, visible=False)

### startScreen

lblP1 = Label('Drag the ', 50, 185, size=15)
lblP2 = Label('red ', 152, 185, size=15, fill='red')
lblP3 = Label('block outside of the board to win!', 275, 185, size=15)
lbl = Group(lblP1, lblP2, lblP3)

lblP1.right = lblP2.left
lblP3.left = lblP2.right
lbl.centerX = 200

startScreen.add(
    Rect(0, 0, 400, 400, fill=gradient('sandyBrown', 'peru')),
    Label('WELCOME TO', 200, 75, align='bottom', size=20, italic=True),
    Label('funny block game', 200, 100, size=45, bold=True,
          fill=gradient('peru', 'sienna'), border='black', borderWidth=1.5),
    Label('by Zain McCoy', 390, 130, align='top-right', size=15),
    lbl,
    Label('SELECT DIFFICULTY', 200, 230, size=20),
    Label('blocks: 6',   25, 365, align='top-left', opacity=50),
    Label('blocks: 8',  150, 365, align='top-left', opacity=50),
    Label('blocks: 10', 275, 365, align='top-left', opacity=50),
    Label('3-long blocks', 150, 377, align='top-left', opacity=50),
    Label('3-long blocks', 275, 377, align='top-left', opacity=50)
    )

### startButtons

easyDiff = Group(
    Rect(75, 310, 100, 100, align='center',
         fill='lime', border='black', borderWidth=3.5),
    Label('easy', 75, 310, size=20, bold=True, opacity=60)
    )
mediumDiff = Group(
    Rect(200, 310, 100, 100, align='center',
         fill='yellow', border='black', borderWidth=3.5),
    Label('medium', 200, 310, size=20, bold=True, opacity=60)
    )
hardDiff = Group(
    Rect(325, 310, 100, 100, align='center',
         fill='red', border='black', borderWidth=3.5),
    Label('hard', 325, 310, size=20, bold=True, opacity=75)
    )
startButtons.add(easyDiff, mediumDiff, hardDiff)
startScreen.add(startButtons)

### properties & lists

blocks.hCount = 0
blocks.vCount = 0
blocks.threeCount = 0
blocks.fails = 0

blocksList = [ ]
boundedBlocks = [ ]
messageList = [
    
    # # vs 1-line
    # ("vs", 1, "EXPECTATION", "REALITY"),
    # ("vs", 1, "MY MOM", "MY DAD"),
    # ("vs", 1, "NOOB", "PRO"),
    
    # updating 1-line
    ("updating", 1, "IQ = ", app.IQ),
    
    # variable 2-line
    ("variable", 2, "L1", "If you reach level ",  app.level + 1, "you are legally logic"),
    ("variable", 2, "L1", "If you pass level ",  app.level, "you can go to Disneyland"),
    
    # variable 1-line
    ("variable", 1, "I can't reach level ",  app.level + 1),
    ("variable", 1, "Even Einstein can't pass level ", app.level),
    
    # simple 2-line
    ("simple", 2, "Can you clear the level", "in under 15sec?"),
    ("simple", 2, "PROMISE ME ! DON'T", "PLAY THIS DURING WORK."),
    ("simple", 2, "50 attempts later", "he has brain damage"),
    ("simple", 2, "my family dont get it", "because their irrelevant"),
    ("simple", 2, "95% of players can't", "beat this satisfying game"),
    
    # simple 1-line
    ("simple", 1, "Only left brained can solve this!"),
    ("simple", 1, "Only 0.03% can pass this level"),
    ("simple", 1, "This game will ruin your life"),
    ("simple", 1, "Harder than you think!"),
    ("simple", 1, "Only geniuses can win at this"),
    ("simple", 1, "I can't do funny block game"),
    ("simple", 1, "how far can you reach it ?"),
    ("simple", 1, "When I let my little brother play"),
    ("simple", 1, "After 437 tries, I still cant beat it"),
    ("simple", 1, "OCD people find the solution"),
    ("simple", 1, "GnhnHnnnnh"),
    ("simple", 1, "Really harder than you think"),
    ("simple", 1, "Can you go futher?"),
    ("simple", 1, "I can't do it"),
    ("simple", 1, "named after my ex")
    ]



##### Functions

### functions

def orientation(block):
    # returns orientation of block
    if (block.height == 30):
        return 'horizontal'
    else:
        return 'vertical'

def type(block):
    # returns type of block (3-long or normal)
    if ((block.width == 110) or (block.height == 110)):
        return '3-long'
    else:
        return 'normal'

def currentSecond(second):
    if ((app.seconds == second) and (app.steps % app.stepsPerSecond == 0)):
        return True
    else:
        return False



def drawBlock(): # draws one block on the board
    x = randrange(80, 281, 40) + 5
    y = randrange(40, 241, 40) + 5
    hCount = 0
    vCount = 0
    passed = True
    
    # if too many 3-longs, then normal
    if (blocks.threeCount >= app.maxThrees):
        type = 1 # normal
    else:
        type = randrange(0, 2) # 1/2 chance to be three
    
    # if too many horizontals, then vertical; vice versa; random
    if (blocks.hCount >= app.maxBlocks // 2 + 1):
        orientation = 1
    elif (blocks.vCount >= app.maxBlocks // 2 + 1):
        orientation = 0
    else:
        orientation = randrange(0, 2)
    
    if (orientation == 0): # horizontal
        width = 70
        height = 30
        if (type == 0): # 3-long
            width = 110
    else: # vertical
        width = 30
        height = 70
        if (type == 0): # 3-long
            height = 110
    
    # if full block isn't within the board or hits another blocks:
    if not ((x + width < 320) and
    (y + height < 280) and
    (blocks.hits(x, y) == False) and
    (blocks.hits(x + width - 1, y + height - 1) == False) and
    (blocks.hits(x + (width/2) - 1, y + (height/2) - 1) == False)):
        passed = False
        
    if (orientation == 0): # horizontal
        # if block has another horizontal same column:
        for block in blocks.children:
            if ((y == block.top) and (block.height == 30)):
                hCount += 1
        if (hCount > 0):
            passed = False
    
    else: # vertical
        # if block has another in same column:
        for block in blocks.children:
            if ((x == block.left) and (block.width == 30)):
                vCount += 1
        if (vCount > 0):
            passed = False
        # if block is in same column as player
        if (x == player.x):
            passed = False
    
    if (passed == True):
        blocks.add(Rect(x, y, width, height, fill='peru', border='black'))
        if (orientation == 0): # horizontal
            blocks.hCount += 1
        else: # vertical
            blocks.vCount += 1
        if (type == 0): # 3-long
            blocks.threeCount += 1
    else:
        blocks.fails += 1

def generateBlocks(): # draws blocks until there is 1 player and blocksPerLevel # of blocks
    blocks.clear()
    app.won = False
    exit.visible = False
    exitLine.centerY = 279
    
    player.x = randrange(80, 281, 40) + 5
    player.left = player.x
    player.top = 45
    blocks.add(player)
    
    leftLine.visible, rightLine.visible = True, True
    if (player.centerX > 100):
        leftLine.x2 = player.left - 5
    else:
        leftLine.visible = False
    if (player.centerX < 300):
        rightLine.x1 = player.right + 5
    else:
        rightLine.visible = False
    exitLine.centerX = player.centerX
    
    while ((len(blocks) < 1 + app.maxBlocks) and (blocks.fails < app.maxFails)):
        drawBlock()
    
    buttons.add(blocks)

def moveBlock(block, x, y):
    
    # moves block on axis depending on orientation
    if (orientation(block) == 'horizontal'):
        if ((type(block) == '3-long') and (140 <= x <= 260)):
            block.centerX = x
        elif ((type(block) == 'normal') and (120 <= x <= 280)):
            block.centerX = x
    else:
        if (block == player):
            if (80 <= y <= 280):
                block.centerY = y
        elif ((type(block) == '3-long') and (100 <= y <= 240)):
            block.centerY = y
        elif ((type(block) == 'normal') and (80 <= y <= 240)):
            block.centerY = y

def boundActiveBlock():
    
    if (orientation(app.activeBlock) == 'horizontal'):
        
        # initialize horizontal boundary
        boundingRect.width, boundingRect.height = 240, 40
        boundingRect.centerX = 200
        boundingRect.centerY = app.activeBlock.centerY
        
        # assign other blocks that are bounded into BoundedBlocks
        updateBoundedBlocks()
        
        # correct bounds
        for block in boundedBlocks:
            
            # if block is left of activeBlock
            if (block.centerX < app.activeBlock.centerX):
                if (block.right + 5 > boundingRect.left):
                    boundingRect.width -= (block.right + 5) - boundingRect.left
                    boundingRect.left = block.right + 5
            
            # if block is right of activeBlock
            else:
                if (block.left - 5 < boundingRect.right):
                    boundingRect.width -= boundingRect.right - (block.left - 5)
                    boundingRect.right = block.left - 5
    
    else:
        
        # initialize vertical boundary
        if (app.activeBlock == player):
            boundingRect.width, boundingRect.height = 40, 280
            boundingRect.centerY = 180
        else:
            boundingRect.width, boundingRect.height = 40, 240
            boundingRect.centerY = 160
        boundingRect.centerX = app.activeBlock.centerX
        
        # assign other blocks that are bounded into BoundedBlocks
        updateBoundedBlocks()
        
        # correct bounds
        for block in boundedBlocks:
            
            # if block is above activeBlock
            if (block.centerY < app.activeBlock.centerY):
                if (block.bottom + 5 > boundingRect.top):
                    boundingRect.height -= (block.bottom + 5) - boundingRect.top
                    boundingRect.top = block.bottom + 5
            
            # if block is below activeBlock
            else:
                if (block.top - 5 < boundingRect.bottom):
                    boundingRect.height -= boundingRect.bottom - (block.top - 5)
                    boundingRect.bottom = block.top - 5
    boundingRect.opacity = app.boundingRectOpacity

def updateBlocksList():
    blocksList.clear()
    for block in blocks.children:
        if (block != app.activeBlock):
            blocksList.append(block)

def updateBoundedBlocks():
    boundedBlocks.clear()
    for block in blocksList:
        if (boundingRect.hitsShape(block) == True):
            boundedBlocks.append(block)

def nextLevel(mod):
    blocks.hCount = 0
    blocks.vCount = 0
    blocks.fails = 0
    app.IQ = 100
    app.steps = 0
    app.seconds = 0
    
    if (mod == 'shuffle'):
        pass
    else:
        app.level += 1
    
    ad.clear()
    nextButton.visible = False
    shuffleButton.visible = False
    levelCounter.value = 'Level: ' + str(app.level)
    levelCounter.right = 395
    
    generateBlocks()

def moveMouse(x, y):
    if (mice.visible == True):
        if (startScreen.visible == True):
            if (startButtons.contains(x, y) == True):
                app.mouse = hand
                cursor.visible = False
                hand.visible = True
            else:
                app.mouse = cursor
                cursor.visible = True
                hand.visible = False
        else:
            if (buttons.contains(x, y) == True):
                app.mouse = hand
                cursor.visible = False
                hand.visible = True
            else:
                app.mouse = cursor
                cursor.visible = True
                hand.visible = False
            
        if (app.mouse == hand):
            app.mouse.left = x - 11
            app.mouse.top = y
        else:
            app.mouse.left = x
            app.mouse.top = y

def updateMessageList():
    messageList[1] = ("variable", 2, "L1", "If you reach level ",  app.level + 2, "you are legally logic")
    messageList[2] = ("variable", 2, "L1", "If you pass level ",  app.level + 1, "you can go to Disneyland")
    messageList[3] = ("variable", 1, "I can't reach level ",  app.level + 2)
    messageList[4] = ("variable", 1, "Even Einstein can't pass level ", app.level + 1)

def mobilize(message, adType, lines):
    updateMessageList()
    if (adType == 'updating'):
        if (lines == 1):
            adTextL1.centerY = 40
            adTextL1.value = message[2] + str(message[3])
            ad.add(adWhiteHeader, adTextL1)
    
    elif (adType == 'variable'):
        if (lines == 2):
            adWhiteHeader.lineWidth = 100
            adTextL1.centerY = 30
            if (message[2] == "L1"):
                adTextL1.value = message[3] + str(message[4])
                adTextL2.value = message[5]
            else:
                adTextL1.value = message[3]
                adTextL2.value = str(message[4]) + message[5]
            ad.add(adWhiteHeader, adTextL1, adTextL2)
        else:
            adTextL1.centerY = 40
            adTextL1.value = message[2] + str(message[3])
            ad.add(adWhiteHeader, adTextL1)
    
    elif (adType == 'simple'):
        if (lines == 2):
            adWhiteHeader.lineWidth = 100
            adTextL1.centerY = 30
            adTextL1.value = message[2]
            adTextL2.value = message[3]
            ad.add(adWhiteHeader, adTextL1, adTextL2)
        
        else:
            adTextL1.centerY = 40
            adTextL1.value = message[2]
            ad.add(adWhiteHeader, adTextL1)
    
    buttons.add(shuffleButton)



### input functions

def onMouseMove(mouseX, mouseY):
    moveMouse(mouseX, mouseY)

def onMousePress(mouseX, mouseY):
    
    if (startScreen.visible == True):
        if (easyDiff.contains(mouseX, mouseY) == True):
            app.maxBlocks = 6
            app.maxThrees = 0
            generateBlocks()
            startScreen.visible = False
        elif (mediumDiff.contains(mouseX, mouseY) == True):
            app.maxBlocks = 8
            app.maxThrees = 1
            generateBlocks()
            startScreen.visible = False
        elif (hardDiff.contains(mouseX, mouseY) == True):
            app.maxBlocks = 10
            app.maxThrees = 1
            generateBlocks()
            startScreen.visible = False
        app.secsPerLvl = (app.maxBlocks * 1.5 - 2) // 1 # 7, 10, 13
    
    else:
        
        # mouse toggle button
        if (mouseToggleButton.contains(mouseX, mouseY) == True):
            mice.visible = not mice.visible
            prohibitedSymbol1.visible = not prohibitedSymbol1.visible
        
        # accessibility button
        if (accessibilityButton.contains(mouseX, mouseY) == True):
            if (prohibitedSymbol2.visible == False):
                app.boundingRectOpacity = 20
            else:
                app.boundingRectOpacity = 0
            prohibitedSymbol2.visible = not prohibitedSymbol2.visible
        
        # shuffle button
        if ((shuffleButton.visible == True) and
            (shuffleButton.contains(mouseX, mouseY) == True)):
            nextLevel('shuffle')
        
        # next button
        if ((nextButton.visible == True) and
            (nextButton.contains(mouseX, mouseY) == True)):
            nextLevel(None)
        
        # identify blocks
        app.activeBlock = blocks.hitTest(mouseX, mouseY)
        updateBlocksList()
        
        # reposition boundingRect or hide boundingRect
        if (app.activeBlock != None):
            boundActiveBlock()
            boundingRect.visible = True
        else:
            boundingRect.visible = False

def onMouseDrag(mouseX, mouseY):
    moveMouse(mouseX, mouseY)
    
    if (app.activeBlock != None):
        
        # move block if it will stay within boundingRect
        if (type(app.activeBlock) == '3-long'):
            if (orientation(app.activeBlock) == 'horizontal'):
                if (boundingRect.left + 60 < mouseX < boundingRect.right - 60):
                    moveBlock(app.activeBlock, mouseX, mouseY)
            else:
                if (boundingRect.top + 60 < mouseY < boundingRect.bottom - 60):
                    moveBlock(app.activeBlock, mouseX, mouseY)
        
        else:
            if (orientation(app.activeBlock) == 'horizontal'):
                if (boundingRect.left + 40 < mouseX < boundingRect.right - 40):
                    moveBlock(app.activeBlock, mouseX, mouseY)
            else:
                if (boundingRect.top + 40 < mouseY < boundingRect.bottom - 40):
                    moveBlock(app.activeBlock, mouseX, mouseY)
        
        if (280 < app.activeBlock.bottom < 313):
            exit.centerX = player.centerX
            exit.bottom = player.bottom + 5
            exitLine.centerY = player.bottom + 5
            exit.visible = True

def onMouseRelease(mouseX, mouseY):
    if (app.activeBlock!= None):
        
        # keep blocks on grid
        if (type(app.activeBlock) == '3-long'):
            if (orientation(app.activeBlock) == 'horizontal'):
                app.activeBlock.centerX = 40 * pythonRound((app.activeBlock.centerX + 20) / 40) - 20
            else:
                app.activeBlock.centerY = 40 * pythonRound((app.activeBlock.centerY + 20) / 40) - 20
        
        else:
            if (orientation(app.activeBlock) == 'horizontal'):
                app.activeBlock.centerX = 40 * pythonRound(app.activeBlock.centerX / 40)
            else:
                app.activeBlock.centerY = 40 * pythonRound(app.activeBlock.centerY / 40)
        
        # win
        if (app.activeBlock == player):
            if (player.bottom > 280):
                exit.bottom = player.bottom + 3
                exitLine.centerY = player.bottom + 3
                app.won = True

def onStep():
    # timer
    if (startScreen.visible == False):
        app.steps += 1
        app.seconds = app.steps // app.stepsPerSecond
    
    if (currentSecond(app.secsPerLvl) == True):
        message = choice(messageList)
        mobilize(message, message[0], message[1])
    
    if (adWhiteHeader.visible == True):
        if (
        (app.steps % app.stepsPerSecond == app.stepsPerSecond // 2) or
        (app.steps % app.stepsPerSecond == 0)
        ): # every half-second
            app.IQ -= 1
            if ("IQ" in adTextL1.value):
                adTextL1.value = "IQ = " + str(app.IQ)
    
    if (app.won == True):
        nextButton.visible = True
        pass
