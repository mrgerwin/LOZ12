from pygame_functions10 import *

HUD_Height = 32
tile_size = 32
screen_width=tile_size*32
screen_height=tile_size*24 + HUD_Height

screenSize(screen_width,screen_height)
HealthLabel = makeLabel("Health = 6", 32, 50, 8, "white", "system")
RupeeLabel = makeLabel("Rupee = 0", 32, 200, 8, "white", "system")
setAutoUpdate(False)
link = Player()
sword = Sword(link)
heart1 = Heart()
rupee = Rupee()
brupee = BlueRupee()


heart1.move(64, 350)
rupee.move(128, 350)
brupee.move(96, 350)



scene1 = Scene(link, "ZeldaMapTilesBrown.png", "map1.txt", 6,8)
scene2 = Scene(link, "ZeldaMapTilesBrown.png", "map2.txt", 6,8)
scene3 = Scene(link, "ZeldaMapTilesWhite.png", "map3.txt", 6,8)
scene4 = Scene(link, "ZeldaMapTilesGreen.png", "map4.txt", 6, 8)
currentScene = scene1
scenes = [[scene1, scene3], [scene2, scene4]]

showBackground(currentScene)
showSprite(heart1)
showSprite(rupee)
showSprite(brupee)
showSprite(link)
scene1.Items=[heart1, rupee, brupee]
for enemy in currentScene.Enemies:
    showSprite(enemy)

showLabel(HealthLabel)
showLabel(RupeeLabel)

nextFrame = clock()
frame = 0
i = 0
j = 0
while True:
    if clock() >nextFrame:
        frame= (frame + 1)%2
        nextFrame += 80
        pause(10)
        
        for wall in currentScene.Wall_Tiles:
            if touching(wall, link):
                link.speed = -link.speed
                link.move(frame)
                link.speed = - link.speed
        
        if keyPressed("down"):
            
            link.orientation =0
            link.move(frame)
        elif keyPressed("up"):
            link.orientation =1
            link.move(frame)
        elif keyPressed("right"):
            link.orientation =2
            link.move(frame)
        elif keyPressed("left"):
            link.orientation =3
            link.move(frame)
        elif keyPressed("space"):
            changeSpriteImage(link, link.orientation + 8)
        #Sword Swing Code
            sword.swing()
            for enemy in currentScene.Enemies:
                if touching(sword, enemy):
                    if enemy.health == 1:
                        currentScene.Enemies.remove(enemy)
                        link.kills += 1
                        itemDrop = dropChart(link.kills)
                        print(itemDrop)
                        if itemDrop == 0:
                            aRupee = Rupee()
                            aRupee.move(enemy.rect.x, enemy.rect.y)
                            currentScene.Items.append(aRupee)
                            showSprite(aRupee)
                        elif itemDrop == 1:
                            aHeart = Heart()
                            aHeart.move(enemy.rect.x, enemy.rect.y)
                            currentScene.Items.append(aHeart)
                            showSprite(aHeart)
                        elif itemDrop == 2:
                            pass
                            #To Do Program Fairy
                        elif itemDrop == 3:
                            pass
                            #To Do Program Bomb
                        elif itemDrop == 4:
                            pass
                            #To Do Program Timer
                        elif itemDrop ==5:
                            aBRupee = BlueRupee()
                            aBRupee.move(x,y)
                            currentScene.Items.append(aBRupee)
                            showSprite(aBRupee)
                    enemy.hit()
        if not keyPressed("space") or keyPressed("left") or keyPressed("right") or keyPressed("up") or keyPressed("down"):
            hideSprite(sword)
        if keyPressed("h"):
            changeSpriteImage(link, frame+12)
        
        for enemy in currentScene.Enemies:
            enemy.move(frame)            
            if touching(enemy, link):
                link.hit(currentScene.Wall_Tiles)
            for wall in currentScene.Wall_Tiles:
                while touching(enemy, wall) or enemy.rect.x > screen_width or enemy.rect.y>screen_height or enemy.rect.x<0 or enemy.rect.y<0:
                    enemy.turn()
                    enemy.move(frame)
        for item in currentScene.Items:
            item.animate(frame)
            if touching(item, link):
                link.collect(item)
                currentScene.Items.remove(item)
                killSprite(item)
                changeLabel(HealthLabel, "Health = " + str(link.health))
                changeLabel(RupeeLabel, "Rupee = " + str(link.rupee))
        if link.rect.x + tile_size//2 > screen_width:
            hideBackground(currentScene)
            i += 1
            currentScene = scenes[i][j]
            showBackground(currentScene)
            hideSprite(link)
            link.rect.x = 32
            showSprite(link)
        elif link.rect.x - tile_size//2 < 0:
            i -= 1
            hideBackground(currentScene)
            currentScene = scenes[i][j]
            showBackground(currentScene)
            hideSprite(link)
            link.rect.x = screen_width - 32
            showSprite(link)
        elif link.rect.y + tile_size//2> screen_height:
            hideBackground(currentScene)
            j += 1
            currentScene = scenes[i][j]
            showBackground(currentScene)
            hideSprite(link)
            link.rect.y = 64
            showSprite(link)
        elif link.rect.y - tile_size//2<32:
            hideBackground(currentScene)
            j -= 1
            currentScene = scenes[i][j]
            showBackground(currentScene)
            hideSprite(link)
            link.rect.y = screen_height - 32
            showSprite(link)
            
        updateDisplay()

endWait()