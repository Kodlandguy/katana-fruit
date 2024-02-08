#pgzero
import random


# Okno gry wykonane z komórek
cell = Actor("space")
WIDTH = 1280
HEIGHT = 720

TITLE = "Katana Fruit" # Tytuł okna gry
FPS = 30 # Liczba klatek na sekundę

#zmienne
mode = "menu"
count = 0

# Obiekty
sword = Actor('weapon_longsword', (300, 150))
splat = Actor("splat16-removebg-preview", (300 , 700))
splat1 = Actor("splat11-removebg-preview")
splat2 = Actor("splat20-removebg-preview")
bomb1 = Actor("Bomba-removebg-preview")
bomb2 = Actor("Bomba-removebg-preview")
fruit1 = Actor("owoc1-removebg-preview", (1000,1000))
fruit2 = Actor("owoc2-removebg-preview", (1000,1000))
fruit3 = Actor("owoc3-removebg-preview", (1000,1000))
settings = Actor("settings",(500, 300))
settings1 = Actor("settings",(500, 400))
settings2 = Actor("settings",(700, 400))
settings3 = Actor("settings",(300, 400))
gra = Actor("gra", (500, 200))
wybuch = Actor("wybuch", (500, 300))
cross = Actor("cross", (580, 20))    
sword1 = Actor("miecz2-removebg-preview", (300, 300))
sword2 = Actor("miecz3-removebg-preview", (700, 300))


fruit1.y=700
fruit2.y=700
fruit3.y=700

price_1=300
price_2=500

        

def draw():
    cell.draw()
    if mode == "menu":
        gra.draw()
        settings.draw()
        settings1.draw()
        screen.draw.text("Bonusy", center=(500, 295), color="white", fontsize = 26)
        screen.draw.text("Sklep", center=(500, 395), color="white", fontsize = 26)
    if mode == "Bonus":
        cell.draw()
        settings2.draw()
        settings3.draw()
        cross.draw()
        screen.draw.text("+1 życie = 500$", center=(300, 395), color="white", fontsize = 26)
        screen.draw.text("+2 życia = 700$", center=(700, 395), color="white", fontsize = 26)
        screen.draw.text("Coming Soon", center=(500, 195), color="white", fontsize = 36)
    if mode == "Sklep":
        cell.draw()
        sword1.draw()
        sword2.draw()
        screen.draw.text(price_1, center=(300, 395), color="white", fontsize = 26)
        screen.draw.text(price_2, center=(700, 395), color="white", fontsize = 26)
        cross.draw()
    elif mode == "game":
        cell.draw()
        sword.draw()
        fruit1.draw()
        fruit2.draw()
        fruit3.draw()
        splat.draw()
        splat1.draw()
        splat2.draw()
        bomb1.draw()
        if count >= 100:
            bomb2.draw()
        cross.draw()
        screen.draw.text(count, center=(150, 150), color="white", fontsize = 96)
    if mode == "end":
        cell.draw()
        wybuch.draw()
        screen.draw.text("GAME OVER!", center=(500, 300), color = 'red', fontsize = 50)
        screen.draw.text(count, center=(150, 150), color="white", fontsize = 96)
    
# Sterowanie
def on_mouse_move(pos):
    sword.pos = pos

def on_mouse_down(button, pos):
    global mode
    global sword1
    global image
    global count
    if mode == "menu":
        if gra.collidepoint(pos):
            mode = "game"
    if cross.collidepoint(pos):
        mode = "menu"
    if settings.collidepoint(pos):
        mode = "Bonus"
    if settings1.collidepoint(pos):
        mode = "Sklep"
    if sword1.collidepoint(pos) and count >= 300:
        sword.image = "miecz2-removebg-preview"
        count -= 300
        sword1.y=305
        animate(sword1, tween="bounce_end", duration=0.5,y = 300)
    if sword2.collidepoint(pos) and count >= 300:
        sword.image = "miecz3-removebg-preview"
        count -= 500
        sword2.y=305
        animate(sword2, tween="bounce_end", duration=0.5,y = 300)
    
        
def update(dt):
    global count
    global mode
    global fruit2
    global weapon_longsword
    
    
    
    if mode == "game":
        for i in range(5):
            o1 = random.randint(5,800)
            o2 = random.randint(4,846)
            o3 = random.randint(6,746)
            b1 = random.randint(6,629)
            b2 = random.randint(5,573)
            
            fruit1.y -= 10
            if fruit1.y <= -50:
                fruit1.y = 700
                fruit1.x = o1
                
                
            fruit2.y -= 10
            if fruit2.y <= -50:
                fruit2.y = 700
                fruit2.x = o2        
            
            
            fruit3.y -= 10
            if fruit3.y <= -50:
                fruit3.y = 700
                fruit3.x = o3  
                
            bomb1.y -= 6
            if bomb1.y <= -50:
                bomb1.y = 700
                bomb1.x = b1
                
                
            if count >= 100:
                bomb2.x -= 6
                if bomb2.x <= -10:
                    bomb2.y = b2
                    bomb2.x = 1200
                
                    
            
        if sword.colliderect(fruit1):
            splat1.pos = (fruit1.pos)            
            count = count + 1
        
        
        if sword.colliderect(fruit1):
            fruit1.y = 2400
            count = count + 1
        
        
        if sword.colliderect(fruit2):
            splat.pos = (fruit2.pos)            
            count = count + 1
        
        
        if sword.colliderect(fruit2):
            fruit2.y = 2400
            count = count + 1   
        
        if sword.colliderect(fruit3):
            splat2.pos = (fruit3.pos)            
            count = count + 1
        
        
        if sword.colliderect(fruit3):
            fruit3.y = 2400    
            count = count + 1
        
        if count <= 100:
            bomb2.x = 2400
        
        
        if sword.colliderect(bomb1):
            mode = "end"
            
        if sword.colliderect(bomb2):
            mode = "end"     
        
        
        
        
        
    if mode == "end" and keyboard.space:
        mode = "game"
        count = count - count


















