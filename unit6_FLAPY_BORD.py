#####  FLAPY BORD   #####
##### by Zain McCoy #####

### Art ###

# background
app.background = 'mediumTurquoise'

# clouds
clouds1 = Group(
    Oval(    0, 360, 40, 80, fill='white'),
    Circle( 20, 360, 20,     fill='white'),
    Circle( 40, 350, 20,     fill='white'),
    Oval(   60, 380, 40, 70, fill='white')
    )
clouds2 = Group(
    Oval(   80, 360, 40, 80, fill='white'),
    Circle(100, 360, 20,     fill='white'),
    Circle(120, 350, 20,     fill='white'),
    Oval(  140, 380, 40, 70, fill='white')
    )
clouds3 = Group(
    Oval(  160, 360, 40, 80, fill='white'),
    Circle(180, 360, 20,     fill='white'),
    Circle(200, 350, 20,     fill='white'),
    Oval(  220, 380, 40, 70, fill='white')
    )
clouds4 = Group(
    Oval(  240, 360, 40, 80, fill='white'),
    Circle(260, 360, 20,     fill='white'),
    Circle(280, 350, 20,     fill='white'),
    Oval(  300, 380, 40, 70, fill='white')
    )
clouds5 = Group(
    Oval(  320, 360, 40, 80, fill='white'),
    Circle(340, 360, 20,     fill='white'),
    Circle(360, 350, 20,     fill='white'),
    Oval(  380, 380, 40, 70, fill='white')
    )
clouds6 = Group(
    Oval(  400, 360, 40, 80, fill='white'),
    Circle(420, 360, 20,     fill='white'),
    Circle(440, 350, 20,     fill='white'),
    Oval(  460, 380, 40, 70, fill='white')
    )

clouds = Group(clouds1, clouds2, clouds3, clouds4, clouds5, clouds6)
clouds.dx = -1

def wrapClouds():
    if (clouds1.right < 20):
        clouds1.left = 400
    if (clouds2.right < 20):
        clouds2.left = 400
    if (clouds3.right < 20):
        clouds3.left = 400
    if (clouds4.right < 20):
        clouds4.left = 400
    if (clouds5.right < 20):
        clouds5.left = 400
    if (clouds6.right < 20):
        clouds6.left = 400

# bushes
bushes1 = Group(
    Circle(  0, 380, 20, fill=rgb(0, 200, 0), border=rgb(0, 175, 0), borderWidth=3),
    Circle( 20, 360, 22, fill=rgb(0, 200, 0), border=rgb(0, 175, 0), borderWidth=3),
    Circle( 40, 370, 17, fill=rgb(0, 200, 0), border=rgb(0, 175, 0), borderWidth=3),
    Circle( 60, 365, 20, fill=rgb(0, 200, 0), border=rgb(0, 175, 0), borderWidth=3)
    )
bushes2 = Group(
    Circle( 80, 380, 20, fill=rgb(0, 200, 0), border=rgb(0, 175, 0), borderWidth=3),
    Circle(100, 360, 22, fill=rgb(0, 200, 0), border=rgb(0, 175, 0), borderWidth=3),
    Circle(120, 370, 17, fill=rgb(0, 200, 0), border=rgb(0, 175, 0), borderWidth=3),
    Circle(140, 365, 20, fill=rgb(0, 200, 0), border=rgb(0, 175, 0), borderWidth=3)
    )
bushes3 = Group(
    Circle(160, 380, 20, fill=rgb(0, 200, 0), border=rgb(0, 175, 0), borderWidth=3),
    Circle(180, 360, 22, fill=rgb(0, 200, 0), border=rgb(0, 175, 0), borderWidth=3),
    Circle(200, 370, 17, fill=rgb(0, 200, 0), border=rgb(0, 175, 0), borderWidth=3),
    Circle(220, 365, 20, fill=rgb(0, 200, 0), border=rgb(0, 175, 0), borderWidth=3)
    )
bushes4 = Group(
    Circle(240, 380, 20, fill=rgb(0, 200, 0), border=rgb(0, 175, 0), borderWidth=3),
    Circle(260, 360, 22, fill=rgb(0, 200, 0), border=rgb(0, 175, 0), borderWidth=3),
    Circle(280, 370, 17, fill=rgb(0, 200, 0), border=rgb(0, 175, 0), borderWidth=3),
    Circle(300, 365, 20, fill=rgb(0, 200, 0), border=rgb(0, 175, 0), borderWidth=3)
    )
bushes5 = Group(
    Circle(320, 380, 20, fill=rgb(0, 200, 0), border=rgb(0, 175, 0), borderWidth=3),
    Circle(340, 360, 22, fill=rgb(0, 200, 0), border=rgb(0, 175, 0), borderWidth=3),
    Circle(360, 370, 17, fill=rgb(0, 200, 0), border=rgb(0, 175, 0), borderWidth=3),
    Circle(380, 365, 20, fill=rgb(0, 200, 0), border=rgb(0, 175, 0), borderWidth=3)
    )
bushes6 = Group(
    Circle(400, 380, 20, fill=rgb(0, 200, 0), border=rgb(0, 175, 0), borderWidth=3),
    Circle(420, 360, 22, fill=rgb(0, 200, 0), border=rgb(0, 175, 0), borderWidth=3),
    Circle(440, 370, 17, fill=rgb(0, 200, 0), border=rgb(0, 175, 0), borderWidth=3),
    Circle(460, 365, 20, fill=rgb(0, 200, 0), border=rgb(0, 175, 0), borderWidth=3)
    )

bushes = Group(bushes1, bushes2, bushes3, bushes4, bushes5, bushes6)
bushes.dx = -2

def wrapBushes():
    if (bushes1.right < 0):
        bushes1.left = 380
    if (bushes2.right < 0):
        bushes2.left = 380
    if (bushes3.right < 0):
        bushes3.left = 380
    if (bushes4.right < 0):
        bushes4.left = 380
    if (bushes5.right < 0):
        bushes5.left = 380
    if (bushes6.right < 0):
        bushes6.left = 380

# ground
Rect(0, 370, 400, 30, fill='navajoWhite')
Line(0, 375, 400, 375, fill=rgb(0, 175, 0), lineWidth=10)
Line(0, 375, 400, 375, fill=rgb(0, 200, 0), lineWidth=10, dashes=(5, 5))

# bird
bird = Group(
    Circle(100, 200, 20, fill=gradient('lemonChiffon', 'yellow', 'yellow', 'gold',
                                   'gold', start='top'), border='black'),
    Circle(110, 192, 8, fill='white', border='black'),
    Oval(113, 192, 3.5, 6, fill='black'),
    Oval(114, 207, 15, 10, fill='crimson', border='black'),
    Line(113, 207, 120, 207, lineWidth=1.5),
    Oval(86, 198, 20, 15, fill=gradient('lemonChiffon', 'yellow', start='top'), border='black', rotateAngle=15)
    )

bird.isJumping = False

jumpLine = Line(80, bird.centerY, 0, bird.centerY, visible=False)

# pipes
topPipe = Group(
    Rect(340, 400, 40, 400, border='black', align='bottom',
         fill=gradient(rgb(0, 200, 0), rgb(0, 250, 0), rgb(0, 225, 0),
                       rgb(0, 175, 0), rgb(0, 100, 0), start='left')),
    Rect(340, 400, 45, 20, border='black', align='bottom',
         fill=gradient(rgb(0, 200, 0), rgb(0, 250, 0), rgb(0, 225, 0),
                       rgb(0, 175, 0), rgb(0, 100, 0), start='left'))
    )
topPipe.bottom = 120

bottomPipe = Group(
    Rect(340, 0, 40, 400, border='black', align='top',
         fill=gradient(rgb(0, 200, 0), rgb(0, 250, 0), rgb(0, 225, 0),
                       rgb(0, 175, 0), rgb(0, 100, 0), start='left')),
    Rect(340, 0, 45, 20, border='black', align='top',
         fill=gradient(rgb(0, 200, 0), rgb(0, 250, 0), rgb(0, 225, 0),
                       rgb(0, 175, 0), rgb(0, 100, 0), start='left'))
    )

bottomPipe.top = 220

pipes = Group(topPipe, bottomPipe)
pipes.left = 450
pipes.dx = -3

def wrapPipes():
    if (pipes.right < 0):
        pipes.left = 400
        topPipe.bottom = (400 - bird.centerY) - 50
        bottomPipe.top = (400 - bird.centerY) + 50

# score
score     = Label(0,        380, 20, fill='white', size=20, visible=False)
best      = Label(0,        390, 35, fill='white', size=10, visible=False)
bestLabel = Label('Best: ', best.left, 35, align='right', fill='white', size=10, visible=False)

# end screen
endScore = Label(score.value, 340, 180, align='right', fill='white', size=35)
endBest = Label(best.value, 340, 240, align='right', fill='white', size=35)
endNewBestBox = Rect(295, 221, 37, 14, align='bottom-right', fill='red',
                     visible=False)
endNewBestLabel = Label('NEW', endNewBestBox.centerX, endNewBestBox.centerY,
                        fill='white', size=18, bold=True, font='monospace',
                        visible=False)

smallBronzeMedal = Group(
    Line(145, 145, 150, 155, fill='red', lineWidth=4),
    Line(155, 145, 150, 155, fill='red', lineWidth=4),
    Circle(150, 155, 5, fill='orange', border='darkOrange'),
    Label('5',  150, 170, bold=True, font='monospace')
    )
smallSilverMedal = Group(
    Line(170, 145, 175, 155, fill='red', lineWidth=4),
    Line(180, 145, 175, 155, fill='red', lineWidth=4),
    Circle(175, 155, 5, fill='lightGray', border='gray'),
    Label('10', 175, 170, bold=True, font='monospace')
    )
smallGoldMedal = Group(
    Line(195, 145, 200, 155, fill='red', lineWidth=4),
    Line(205, 145, 200, 155, fill='red', lineWidth=4),
    Circle(200, 155, 5, fill='yellow', border='gold'),
    Label('15', 200, 170, bold=True, font='monospace')
    )
smallPlatinumMedal = Group(
    Line(220, 145, 225, 155, fill='red', lineWidth=4),
    Line(230, 145, 225, 155, fill='red', lineWidth=4),
    Circle(225, 155, 5, fill='white', border='lightGray'),
    Label('20', 225, 170, bold=True, font='monospace')
    )
smallMedals = Group(smallBronzeMedal, smallSilverMedal,
                    smallGoldMedal, smallPlatinumMedal)
smallMedals.centerX = 205

bronzeMedal = Group(
    Circle(100, 215, 35, fill='orange', border='darkOrange', borderWidth=5),
    Star(100, 215, 20, 5, fill='darkOrange')
    )
silverMedal = Group(
    Circle(100, 215, 35, fill='lightGray', border='gray', borderWidth=5),
    Star(100, 215, 20, 5, fill='gray')
    )
goldMedal = Group(
    Circle(100, 215, 35, fill='yellow', border='gold', borderWidth=5),
    Star(100, 215, 20, 5, fill='gold')
    )
platinumMedal = Group(
    Circle(100, 215, 35, fill='white', border='lightGray', borderWidth=5),
    Star(100, 215, 20, 5, fill='lightGray')
    )
medals = Group(bronzeMedal, silverMedal, goldMedal, platinumMedal)

endScreen = Group(
    Circle(    60, 140,  20, border='black', fill='navajoWhite', borderWidth=4),
    Circle(   340, 140,  20, border='black', fill='navajoWhite', borderWidth=4),
    Circle(    60, 260,  20, border='black', fill='navajoWhite', borderWidth=4),
    Circle(   340, 260,  20, border='black', fill='navajoWhite', borderWidth=4),
    Rect(200, 200, 280, 120, align='center', fill='navajoWhite'),
    Rect( 60, 200,  20, 120, align='right',  fill='navajoWhite'),
    Rect(340, 200,  20, 120, align='left',   fill='navajoWhite'),
    Rect(200, 140, 280,  20, align='bottom', fill='navajoWhite'),
    Rect(200, 260, 280,  20, align='top',    fill='navajoWhite'),
    Line( 60, 122, 340, 122, lineWidth=4),
    Line( 60, 278, 340, 278, lineWidth=4),
    Line( 42, 140,  42, 260, lineWidth=4),
    Line(358, 140, 358, 260, lineWidth=4),
    
    Label('Game Over!', 203,  83, fill='black',  size=50, bold=True),
    Label('Game Over!', 200,  80, fill='orange', size=50, bold=True),
    Label('Press [ENTER] to restart!', 200, 295, fill='white', size=18,
          bold=True, italic=True),
    Label('MEDAL', 100, 160, align='bottom', fill='orangeRed', size=18,
          bold=True, font='monospace'),
    Label('SCORE', 340, 160, align='bottom-right', fill='orangeRed',
          size=18, bold=True, font='monospace'),
    Label('BEST', 340, 220, align='bottom-right', fill='orangeRed',
          size=18, bold=True, font='monospace'),
    Circle(100, 215, 35, fill='gray', border='dimGray', borderWidth=5),
    endScore,
    endBest,
    endNewBestBox,
    endNewBestLabel,
    smallMedals,
    medals
    )

# start screen

playButton = Circle(120, 200, 80, fill=rgb(0, 200, 0), border='black', borderWidth=4)

startScreen = Group(
    Circle(    40,  40,  20, border='black', fill='navajoWhite', borderWidth=4),
    Circle(   360,  40,  20, border='black', fill='navajoWhite', borderWidth=4),
    Circle(    40, 360,  20, border='black', fill='navajoWhite', borderWidth=4),
    Circle(   360, 360,  20, border='black', fill='navajoWhite', borderWidth=4),
    Rect(200, 200, 320, 320, align='center', fill='navajoWhite'),
    Rect( 40, 200,  20, 320, align='right',  fill='navajoWhite'),
    Rect(360, 200,  20, 320, align='left',   fill='navajoWhite'),
    Rect(200,  40, 320,  20, align='bottom', fill='navajoWhite'),
    Rect(200, 360, 320,  20, align='top',    fill='navajoWhite'),
    Line( 40,  22, 360,  22, lineWidth=4),
    Line( 40, 378, 360, 378, lineWidth=4),
    Line( 22,  40,  22, 360, lineWidth=4),
    Line(378,  40, 378, 360, lineWidth=4),
    Label('FLAPY BORD', 203, 63, fill='black',  size=50, bold=True),
    Label('FLAPY BORD', 200, 60, fill='orange', size=50, bold=True),
    playButton,
    RegularPolygon(120, 200, 50, 3, fill='white', border='black', borderWidth=4, rotateAngle=-30),
    Label('Press play button to start!', 200, 320, fill='black', size=25),
    Rect(340, 180, 10, 60, align='bottom', fill=rgb(0, 200, 0)),
    Rect(340, 180, 20, 10, align='bottom', fill=rgb(0, 200, 0)),
    Rect(340, 220, 20, 10, align='top',    fill=rgb(0, 200, 0)),
    Rect(340, 220, 10, 60, align='top',    fill=rgb(0, 200, 0)),
    Label('Press any key to', 265, 185,),
    Label('jump and stay', 265, 200,),
    Label('between the pipes!', 265, 215,)
    )

### Functions ###

def endGame():
    # Show end screen & hide top-right values
    endScreen.visible = True
    medals.visible = False
    score.visible = False
    bestLabel.visible = False
    best.visible = False
    # If score > current best:
    endScore.value = score.value
    if (score.value > best.value):
        # Update best value & show NEW
        best.value = score.value
        endBest.value = score.value
        endNewBestBox.visible = True
        endNewBestLabel.visible = True
    # Otherwise:
    else:
        # Hide NEW
        endNewBestBox.visible = False
        endNewBestLabel.visible = False
    if (score.value >= 20):
        platniumMedal.visible = True
    elif (score.value >= 15):
        goldMedal.visible = True
    elif (score.value >= 10):
        silverMedal.visible = True
    elif (score.value >= 5):
        bronzeMedal.visible = True

def onMousePress(mouseX, mouseY):
    if (playButton.contains(mouseX, mouseY)):
        startScreen.clear()
        endScreen.visible = False
        score.visible = True
        bestLabel.visible = True
        best.visible = True

def onKeyPress(key):
    # If under y60:
    if (bird.top >= 60):
        # Jump
        bird.isJumping = True
        jumpLine.centerY = bird.centerY
        jumpLine.rotateAngle = 0
    # If game is stopped & key is 'enter':
    if ((endScreen.visible == True) and (key == 'enter')):
        # Restart game
        endScreen.visible = False
        endNewBestBox.visible = False
        endNewBestLabel.visible = False
        bird.centerY = 200
        jumpLine.centerY = 200
        pipes.left = 450
        score.value = 0
        score.visible = True
        bestLabel.visible = True
        best.visible = True
        bronzeMedal.visible = False
        silverMedal.visible = False
        goldMedal.visible = False
        platinumMedal.visible = False

def onStep():
    # While game is running:
    if (endScreen.visible == False):
        # Move background/pipes
        clouds.centerX += clouds.dx
        bushes.centerX += bushes.dx
        pipes.centerX += pipes.dx
        wrapClouds()
        wrapBushes()
        wrapPipes()
        
        # If jump is complete:
        if (jumpLine.rotateAngle >= 180):
            # Reset jump
            jumpLine.rotateAngle = 0
            bird.isJumping = False
        # Otherwise:
        else:
            # If bird is jumping:
            if (bird.isJumping == True):
                # Rotate jumpLine to make curved motion
                jumpLine.rotateAngle += 9
                bird.centerY = jumpLine.y2
            # Otherwise:
            else:
                # Freefall
                bird.centerY += 7
        # If bird hits pipes or ground:
        if ((bird.hitsShape(pipes)) or (bird.bottom >= 380)):
            # End game
            endGame()
        # Otherwise, if bird passes through pipes:
        elif (pipes.centerX <= bird.centerX <= pipes.centerX + 2):
            # Increase score by 1
            score.value += 1
            endScore.value = score.value
