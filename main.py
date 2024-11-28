import random
import pgzrun

WIDTH = 400
HEIGHT = 400

score  = 0
bee = Actor("bee")
bee.pos = (150,100)

flower = Actor("flower")
flower.pos = (100,100)

def draw():
    screen.blit("bggrass",(0,0))
    bee.draw()
    flower.draw()

def place_flower():
    flower.x = random.randint(70,(WIDTH - 70))
    flower.y = random.randint(70,(HEIGHT - 70))

def update():
    global score
    if keyboard.left:
        bee.x -= 2
    if keyboard.right:
        bee.x += 2
    if keyboard.up:
        bee.y -= 2
    if keyboard.down:
        bee.y += 2
    flower_collected = bee.colliderect(flower)
    if flower_collected:
        score = score +10
        place_flower()



    


pgzrun.go()