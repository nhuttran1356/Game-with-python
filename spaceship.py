import pgzrun
import random
from random import randint

WIDTH=800
HEIGHT=600
score=0
game_over=False
list_ship=[]
list_score =[0]

ship=Actor('playership1_blue')
ship.x=370
ship.y=550
list_ship.append(ship)

gem=Actor('gemblue')
gem.x=200
gem.y=0

gem2=Actor('gem2')
gem2.x = 300
gem2.y=-10

meto=Actor('meteorgrey_big1')
meto.x=400
meto.y=0

meto2=Actor('meteorgrey_big2')
meto2.x=400
meto2.y=0

speed_gem = random.randint(4,10)
speed_meto1 = random.randint(4,10)
speed_meto2 = random.randint(4,10)

def on_mouse_move(pos,rel,buttons):
    ship.x=pos[0]
    ship.y=pos[1]

def update():
    global score ,game_over, list_ship
    gem.y=gem.y+2+score/speed_gem
    meto.y=meto.y+2+score/speed_meto1
    meto2.y=meto2.y+2+score/speed_meto2
    
    if gem.y>600:
        gem.y=0
        gem.x=random.randint(20,780)
    if meto.y>600:
        meto.y=-50
        meto.x=random.randint(20,780)
    if meto2.y>600:
        meto2.y=0
        meto2.x=random.randint(100,780)-50
    if gem.collidelist(list_ship) == 0:
        gem.x=random.randint(20,780)
        gem.y=0
        score=score+1
        sounds.epe.play()
        list_score.append(score)
    if meto.collidelist(list_ship) == 0 or meto2.collidelist(list_ship) == 0:
        game_over=True
        sounds.bumm.play()
        sounds.gameover.play()
        list_ship= []
    if gem.colliderect(meto) or gem.colliderect(meto2):
        gem.x=random.randint(20,780)
        gem.y=0
    if score > 10:
        gem2.y=gem2.y+6+score/(speed_gem-1)
    if gem2.y>600:
        gem2.y=0
        gem2.x=random.randint(20,780)
    if gem2.collidelist(list_ship) == 0:
        score=score-2
        gem2.x=random.randint(20,780)
        gem2.y=-10
        list_score.append(score)
        sounds.gem2.play()


    if game_over==True:
        if keyboard.space:
            game_over= False
            score=0
            list_ship.append(ship)
            ship.x=370
            ship.y=550
            meto.x=400
            meto.y=0
            meto2.x=100
            meto2.y=-50
            gem.x=200
            gem.y=0
            gem2.x=100
            gem2.y=-10
    
def draw():
    screen.fill((0,0,0))
    if game_over:
        screen.draw.text('Game over !!',(120,80),color=(255,255,255),fontsize=140)
        screen.draw.text('Final score: '+str(score),(295,250),color=(255,0,255),fontsize=50)
        screen.draw.text('Press space to play again',(149,550),color=(100,100,255),fontsize=60)
        screen.draw.text('Highest score: '+ str(max(list_score)) ,(300,330),color=(212,58,47),fontsize=50)
        if score == max(list_score) and score != 0:
            screen.draw.text('The new high score !!! ',(120,400),color=(229,237,7),fontsize=80)
        
            
    else: 
      screen.draw.text('score:'+str(score),(10,15),color=(255,255,255),fontsize=60)
      ship.draw()
      gem.draw()
      meto.draw()
      meto2.draw()
      gem2.draw()

pgzrun.go()
