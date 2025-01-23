import pygame as pg

pg.init()

# RGB
colors = {
    "blue": (60, 80, 230),
    "background": (255, 255, 255),
    "white": (255, 255, 255),
    "black": (0,0,0),
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "yellow": (255, 255, 0)
}

screen_width = 800
screen_height = 600

screen = pg.display.set_mode((screen_width, screen_height))
clock = pg.time.Clock()
pg.display.set_caption("My first game")

running = True

class Vector():
    def __init__(self, x : float | tuple, y):
        if isinstance(x, tuple):
            self.x = x[0]
            self.y = x[1]
            
        elif isinstance(y, float):
            self.x = x
            self.y = y
        
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __iadd__(self, other):
        return self + other
    

class Ball():
    def __init__(self, x, y, radius, color, vel : Vector | tuple | None):
        self.cords = Vector(x, y)
        self.radius = radius
        self.color = color
        self.velocity = vel
        
        self.update()
        
    def update(self):
        self.cords += self.velocity
        pg.draw.circle(screen, self.color, self.cords, self.radius)

ball = Ball(0,0,10,colors["white"])

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False    
    
    if x < 20 or x > screen_width-20: acc = -acc
    x += acc
    
    screen.fill(colors["black"])
    ball.update()
    
    clock.tick(144)
    pg.display.flip()
    
pg.quit()