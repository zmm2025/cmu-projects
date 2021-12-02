##### Russian Roulette #####
#####                  #####
##### by Zain McCoy    #####
##### idea from Nathan #####



### Configurable values ###

app.woodLineDensity = 50 # (default: 50)
app.fadeToBlack = True # (default: True)
app.spinTime = 2 # in seconds (default: 2)



### Art ###

app.stepsPerSecond = 100 # 100 steps = 1 second
app.background = gradient('fireBrick', 'darkRed')

app.counter = 0
app.survives = 0
app.phase = 0
# 0: inital
# 1: spinning chamber
# 2: chamber spun (safe)
# 3: chamber spun (death)

spinSteps = app.spinTime * 100
largeFade = gradient('dimGray', 'silver',    start='left')
smallFade = gradient('gray',    'darkGray',  start='left')
woodFade  = gradient('peru',    'burlyWood', start='left')
bulletFade = gradient(rgb(255, 255, 175), 'gold', rgb(100, 75, 0))

# gun
Oval(200, 280, 60, 220, align='top', fill=woodFade)
Oval(200, 140, 60, 220, align='top', fill=woodFade)

for woodLine in range(app.woodLineDensity):
    x   = randrange(180, 221)
    top = randrange(165, 381)
    rVal = randrange(0, 2)
    if (rVal == 0):
        color = 'burlyWood'
    else:
        color = 'peru'
    
    Line(x, top, x, top + 50, fill=color)

chamber = Group(Circle(200, 200, 60, fill=largeFade))
chamberHoles = Group()
chamber.add(chamberHoles)

Rect(200, 130, 5, 15, align='bottom', fill=smallFade)
Circle(200, 140, 10, fill=smallFade)
Rect(200, 200, 40, 120, align='center', fill=smallFade)
Polygon(180, 260, 185, 270, 180, 280, 220, 280,
        215, 270, 220, 260, fill=smallFade)
Rect(200, 300, 40, 40, align='center', fill=smallFade)
Polygon(180, 320, 195, 360, 205, 360, 220, 320, fill=smallFade)
Rect(200, 400, 10, 40, align='bottom', fill=smallFade)

Circle(200, 220, 15, fill=gradient('dimGray', 'gray', start='top-left'))
Arc(200, 220, 30, 30, 0, 105,
    fill=gradient('darkGray', 'silver', start='bottom-right'))
Circle(200, 160, 21, border='darkGray', borderWidth=6)

for chamberHole in range(6):
    angle = chamberHole * 60
    x, y = getPointInDir(200, 200, angle, 40)
    chamberHoles.add(Circle(x, y, 15))

for chamberHole in chamberHoles.children:
    chamberHole.bulletHovering = False



# shelf, bullet, text, blackScreen
Rect(400, 375, 80, 10, align='top-right', fill=woodFade)
bullet = Circle(360, 360, 15, fill=bulletFade)
bullet.holding = False
bullet.hoveringHole = False
bullet.inserted = False

topText1 = Label('Russian Roulette!', 200, 30, size=35, fill='white', bold=True)
topText2 = Label('Sample Text', 200, 30, size=35, fill='limeGreen', bold=True,
                 visible=False) # had to peek at unit 9 for this
topText3 = Label('Uh oh...', 200, 30,
                 size=35, fill='red', bold=True, visible=False)
subText1 = Label('Drag the bullet into the gun to start!',
                 200, 60, size=15, fill='white')
subText2 = Label('Now cross your fingers, and spin the chamber!',
                 200, 60, size=15, fill='white', visible=False)
subText3 = Label('Spin again to try your luck!',
                 200, 60, size=15, fill='white', visible=False)

bigBullet = Circle(200, 160, 15, fill=bulletFade, visible=False)
blackScreen = Rect(0, 0, 400, 400, opacity=0)



### Functions ###

# 



### User input functions ###

def onMousePress(mouseX, mouseY):
    if (bullet.inserted == False):
        if (bullet.hits(mouseX, mouseY)):
            bullet.holding = True

def onMouseDrag(mouseX, mouseY):
    if (bullet.holding == True):
        bullet.centerX, bullet.centerY = mouseX, mouseY
    
    for chamberHole in chamberHoles.children:
        if (bullet.hitsShape(chamberHole)):
            chamberHole.bulletHovering = True
        else:
            chamberHole.bulletHovering = False
    
    if (bullet.hitsShape(chamberHoles)):
        bullet.hoveringHole = True
    
    if (bullet.inserted == True):
        if ((chamber.hits(mouseX, mouseY)) and (app.phase == 0)):
            app.phase = 1
            chamber.randHole = randrange(0, 6)
            chamber.totRotation = chamber.randHole * 60 + 720
    

def onMouseRelease(mouseX, mouseY):
    if ((bullet.holding == True) and (bullet.inserted == False)):
        if (bullet.hoveringHole == True):
            for chamberHole in chamberHoles.children:
                if (chamberHole.bulletHovering == True):
                    bulletTargetX = chamberHole.centerX
                    bulletTargetY = chamberHole.centerY
            bullet.centerX = bulletTargetX
            bullet.centerY = bulletTargetY
            bullet.holding = False
            bullet.inserted = True
            chamber.add(bullet)
            subText1.visible = False
            subText2.visible = True
        else:
            bullet.centerX = 360
            bullet.centerY = 360

def onStep():
    if (app.phase == 1):
        
        app.counter += 1
        chamber.rotateAngle += chamber.totRotation / spinSteps
        
        if (app.fadeToBlack == True):
            blackScreen.opacity += (100 / spinSteps) - 0.001
        
        if (app.counter >= spinSteps):
            app.counter = 0
            app.phase = 2
    
    elif (app.phase == 2):
        blackScreen.opacity = 0
        topText1.visible = False
        topText2.visible = True
        subText2.visible = False
        
        if (bullet.centerY <= 170):
            app.phase = 3
            topText2.visible = False
            topText3.visible = True
            subText3.visible = False
        else:
            app.survives += 1
            app.phase = 0
            if (app.survives == 1):
                topText2.value = 'You survived ' + str(app.survives) + ' time!'
            else:
                topText2.value = 'You survived ' + str(app.survives) + ' times!'
            subText3.visible = True
    
    elif (app.phase == 3):
        bullet.visible = False
        bigBullet.visible = True
        if (bigBullet.radius < 1000):
            bigBullet.radius += 5
        else:
            app.stop()
