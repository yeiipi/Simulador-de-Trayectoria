from fun import *

clock = pg.time.Clock()
FPS = 30

pg.init()

# dimensiones
d_width = 800
d_height= 800

# colores
transparent = (0,0,0,0)
white = (255,255,255, 155)
black = (0,0,0, 255)

light_pink = (255, 173, 173)
deep_champagne = (255, 214, 165)
lemon_yellow = (253, 255, 182)
tea_green = (202, 255, 191)
celeste = (155, 246, 255)
mauve = (255, 198, 255)



win = pg.display.set_mode((d_width,d_height))
pg.display.set_caption('Simulación tiro parabólico')


def main():
    while True:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()



if __name__ == '__main__':
    main()
