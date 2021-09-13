import pygame

# Some "macros"
# --------------
INF = 10 ** 6

FREE = 0
JERRY_INIT = 1
JERRY_END = 2
TOM_INIT = 3

OBSTACLE0 = 4
OBSTACLE1 = 5
OBSTACLE2 = 6
OBSTACLE3 = 7

TRAP0 = 8
TRAP1 = 9
TRAP2 = 10

C_FREE = (255, 255, 255)
C_JI = (250, 2, 64)
C_JE = (250, 110, 2)
C_TI = (61, 0, 148)

C_OBS0 = (0, 102, 12)
C_OBS1 = (102, 24, 0)
C_OBS2 = (232, 177, 104)
C_OBS3 = (201, 162, 111)

C_TR0 = (36, 255, 240)
C_TR1 = (168, 94, 34)
C_TR2 = (237, 36, 0)


class Tom:
    def __init__(self, x: int, y: int):
        self.x, self.y = x, y
        self.icon = pygame.image.load('resources/tom.jpg')

    def algoritmo(self):
        # Inserte algoritmo aquí
        pass

    def draw(self, window):

        window.blit(self.icon, (self.x, self.y))


class Jerry:
    def __init__(self, x: int, y: int):
        self.x, self.y = x, y
        self.icon = pygame.image.load('resources/jerry.jpg')

    def algoritmo(self):
        # Inserte algoritmo aquí
        pass

    def draw(self, window):
        window.blit(self.icon, (self.x, self.y))


"""
class Tile:
    def __init__(self, tile_type):
        self.type = tile_type

        self.delay = \
            0 if tile_type == (FREE or JERRY_INIT or JERRY_END or TOM_INIT) else \
            1 if tile_type == TRAP0 else \
            2 if tile_type == TRAP1 else \
            3 if tile_type == TRAP2 else INF
"""


class Map:
    def __init__(self, tiles_vals: list):
        self.vals = tiles_vals
        self.width = len(self.vals[0])
        self.height = len(self.vals)

    def draw(self, window):
        scr_w = window.get_width() // self.width
        scr_h = window.get_height() // self.height

        for y in range(self.height):
            for x in range(self.width):
                t = self.vals[y][x]

                color = \
                    C_FREE if t == FREE else \
                    C_JI if t == JERRY_INIT else \
                    C_JE if t == JERRY_END else \
                    C_TI if t == TOM_INIT else \
                    C_OBS0 if t == OBSTACLE0 else \
                    C_OBS1 if t == OBSTACLE1 else \
                    C_OBS2 if t == OBSTACLE2 else \
                    C_OBS3 if t == OBSTACLE3 else \
                    C_TR0 if t == TRAP0 else \
                    C_TR1 if t == TRAP1 else C_TR2

                pygame.draw.rect(window, color, (x * scr_w, y * scr_h, scr_w, scr_h))


class Game:
    def __init__(self, wnd_resolution: tuple):
        map1 = [[3,  0, 7, 0, 6, 6, 0,  9,  0, 2],
                [8,  0, 7, 0, 0, 0, 0,  0,  0, 0],
                [0, 10, 7, 0, 5, 5, 5, 10, 10, 9],
                [8,  0, 7, 0, 0, 0, 0,  0,  0, 0],
                [0, 10, 7, 7, 7, 7, 7,  0,  0, 4],
                [0,  0, 4, 5, 5, 5, 4,  0,  0, 0],
                [0,  0, 0, 0, 0, 0, 0,  0,  9, 1]]

        map2 = [[3,  0, 8, 6, 6, 6, 4, 9,  0, 2],
                [0, 10, 0, 9, 0, 0, 0, 8,  0, 0],
                [4,  0, 7, 0, 5, 0, 7, 0,  0, 9],
                [5, 0,  7, 0, 5, 0, 7, 0, 10, 4],
                [5, 0,  0, 0, 5, 0, 0, 0,  0, 0],
                [5, 0,  7, 0, 0, 0, 7, 0,  9, 0],
                [4, 0,  7, 7, 7, 7, 7, 0,  0, 1]]

        self.resol = wnd_resolution
        self.game_over = False
        self.board = Map(map2)

        self.tom_ai = Tom(0, 0)
        self.jerry_ai = Jerry(20, 40)

    def run(self):
        # Initialize
        # -----------
        pygame.init()
        window = pygame.display.set_mode(self.resol)
        pygame.display.set_caption("Tom & Jerry in...")
        # pygame.display.set_icon(pygame.image.load("resources/icon.png"))
        my_font = pygame.font.Font(None, 20)
        # -----------

        # Now actually run the game
        # --------------------------
        while not self.game_over:
            window.fill((0, 0, 0))
            self.board.draw(window)
            self.tom_ai.draw(window)
            # self.jerry_ai.draw(window)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        exit()

            pygame.display.update()
        # --------------------------


def main():
    tnj = Game((800, 600))
    tnj.run()


if __name__ == '__main__':
    main()
