import pygame as pg

pg.init()

# RGB
colors = {
    "blue": (60, 80, 230),
    "background": (255, 255, 255)
}

screen_width = 800
screen_height = 600

screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption("My first game")

running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill(colors["blue"])
    pg.display.flip()
    
pg.quit()