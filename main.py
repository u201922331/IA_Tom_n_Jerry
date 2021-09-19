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


# ########################
# # All entities go here #
# ########################
class Entity:
    def __init__(self, x: int, y: int, sprite_path: str, w, m):
        self.x, self.y = x, y
        self.sprite = pygame.image.load(sprite_path)
        self.sprite = pygame.transform.scale(self.sprite, (w.get_width() // m.width, w.get_height() // m.height))

        self.dx = [1, -1, 0, 0]
        self.dy = [0, 0, 1, -1]

    def render(self, window, m):
        scaled_pos = (
            self.x * window.get_width() // m.width,
            self.y * window.get_height() // m.height
        )

        window.blit(self.sprite, scaled_pos)

    def get_pos(self):
        return tuple((self.x, self.y))

    @staticmethod
    def valid(x: int, y: int, lista_cerrada, m):
        return \
            (x >= 0) and \
            (x < 7) and \
            (y >= 0) and \
            (y < 10) and \
            (m.vals[x][y] != 4 and m.vals[x][y] != 5 and m.vals[x][y] != 6 and m.vals[x][y] != 7) and \
            ((x, y) not in lista_cerrada)

    def A_estrella(self, m, init, destino, objetivo_peligro, entity):
        lista_cerrada = [init]
        padres = [[0 for _ in range(m.width)] for _ in range(m.height)]
        F = [[1000 for _ in range(m.width)] for _ in range(m.height)]
        G = [[0 for _ in range(m.width)] for _ in range(m.height)]

        while True:
            block = False
            x, y = lista_cerrada[-1]

            for i in range(4):
                nx = x + self.dx[i]
                ny = y + self.dy[i]

                if self.valid(nx, ny, lista_cerrada, m):
                    if (x, y) == init:
                        F[nx][ny] = 5 + entity.heuristica(m, [nx, ny], destino, objetivo_peligro)
                        padres[nx][ny] = (x, y)
                    elif (nx, ny) == destino:
                        lista_cerrada.append((nx, ny))
                        padres[nx][ny] = (x, y)
                    else:
                        G[nx][ny] = G[x][y] + 5
                        F[nx][ny] = G[nx][ny] + entity.heuristica(m, [nx, ny], destino, objetivo_peligro)
                        padres[nx][ny] = (x, y)

            if lista_cerrada[-1] == destino:
                break

            menor = min(map(min, F))
            # print(F, menor)
            for i in range(m.height):
                for j in range(m.width):
                    if menor == F[i][j] and (i, j) not in lista_cerrada and not block:
                        lista_cerrada.append((i, j))
                        F[i][j] = 1000
                        block = True

        return padres

    def algoritmo(self, m, init, destino, objetivo_peligro, entity):
        _inicio = (init[1], init[0])
        _destino = (destino[1], destino[0])
        _objetivo_peligro = (objetivo_peligro[1], objetivo_peligro[0])

        padres = self.A_estrella(m, _inicio, _destino, _objetivo_peligro, entity)
        recorrido = [_destino]
        x, y = _destino
        block = False

        while not block:
            for i in range(m.height):
                for j in range(m.width):
                    if (i, j) == padres[x][y]:
                        recorrido.append((i, j))
                        if (i, j) == _inicio:
                            block = True
                        x, y = i, j

        recorrido.reverse()
        return recorrido


class Tom(Entity):
    def __init__(self, x: int, y: int, w, m):
        super().__init__(x, y, 'resources/tom.png', w, m)

    @staticmethod
    def heuristica(m, pos, jerry_end, objetivo_peligro):
        heuristica = abs(pos[0] - jerry_end[0]) + abs(pos[1] - jerry_end[1])
        if m.vals[pos[0]][pos[1]] == 8 or m.vals[pos[0]][pos[1]] == 9 or m.vals[pos[0]][pos[1]] == 10:
            heuristica += 1
        return heuristica


class Jerry(Entity):
    def __init__(self, x: int, y: int, w, m):
        super().__init__(x, y, 'resources/jerry.png', w, m)

    @staticmethod
    def heuristica(m, pos, jerry_end, objetivo_peligro):
        heuristica = abs(pos[0] - jerry_end[0]) + abs(pos[1] - jerry_end[1])
        if m.vals[pos[0]][pos[1]] == 8 or m.vals[pos[0]][pos[1]] == 9 or m.vals[pos[0]][pos[1]] == 10:
            heuristica += 100
        if abs(pos[0] - objetivo_peligro[0]) + abs(pos[1] - objetivo_peligro[1]) <= 2:
            heuristica += 200
        return heuristica


# ########################
# # Map class definition #
# ########################
class Map:
    def __init__(self, tiles_vals: list):
        self.vals = tiles_vals
        self.width = len(self.vals[0])
        self.height = len(self.vals)

        # Validate the map
        ti_count, ji_count, je_count = 0, 0, 0
        i, j = 0, 0
        for row in self.vals:
            for column in row:
                if column == TOM_INIT:
                    ti_count += 1
                elif column == JERRY_INIT:
                    ji_count += 1
                elif column == JERRY_END:
                    je_count += 1
                    self.j_end = (j, i)
                j += 1
            i += 1
        assert ti_count == 1 and ji_count == 1 and je_count == 1

    def render(self, window):
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


# ##############
# # CORE class #
# ##############
class Game:
    def __init__(self, wnd_resolution: tuple):
        pygame.init()

        map1 = [[3,  0, 7, 0, 6, 6, 0,  9,  0, 2],
                [8,  0, 7, 0, 0, 0, 0,  0,  0, 0],
                [0, 10, 7, 0, 5, 5, 5, 10, 10, 9],
                [8,  0, 7, 0, 0, 0, 0,  0,  0, 0],
                [0, 10, 7, 7, 7, 7, 7,  0,  0, 4],
                [0,  0, 4, 5, 5, 5, 4,  0,  0, 0],
                [0,  0, 0, 0, 0, 0, 0,  0,  9, 1]]

        map2 = [[3, 0, 8, 6, 6, 6, 4, 9, 0, 2],
                [0, 10, 0, 9, 0, 0, 0, 8, 0, 0],
                [4, 0, 7, 0, 5, 0, 7, 0,  0, 9],
                [5, 0, 7, 0, 5, 0, 7, 0, 10, 4],
                [5, 0, 0, 0, 5, 0, 0, 0,  0, 0],
                [5, 0, 7, 0, 0, 0, 7, 0,  9, 0],
                [4, 0, 7, 7, 7, 7, 7, 0,  0, 1]]

        map3 = [[3, 0, 4, 0, 4, 4, 0, 8, 0, 2],
                [8, 0, 4, 0, 0, 0, 0, 0, 0, 0],
                [0, 8, 4, 0, 4, 4, 4, 8, 8, 8],
                [8, 0, 4, 0, 0, 0, 0, 0, 0, 0],
                [0, 8, 4, 4, 4, 4, 4, 0, 0, 4],
                [0, 0, 4, 4, 4, 4, 4, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 8, 1]]

        self.window = pygame.display.set_mode(wnd_resolution)
        self.game_over = False
        self.jerry_wins = False
        self.map = Map(map2)

        selected = self.map.vals
        for i in range(len(selected)):
            for j in range(len(selected[0])):
                if selected[i][j] == 3:
                    self.tom_ai = Tom(j, i, self.window, self.map)
                if selected[i][j] == 1:
                    self.jerry_ai = Jerry(j, i, self.window, self.map)
                if selected[i][j] == 2:
                    self.ratonera = (j, i)

    def run(self):
        def event_handler():
            for event in pygame.event.get():
                # Main exit event
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                # Keyboard events
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        exit()

        # Initialize
        # -----------
        pygame.display.set_caption("Tom & Jerry in...")
        # pygame.display.set_icon(pygame.image.load("resources/icon.png"))
        my_font = pygame.font.Font(None, 30)
        frame = 0
        # -----------
        j_end = [0, 0]
        for i in range(self.map.height):
            for j in range(self.map.width):
                if self.map.vals[i][j] == JERRY_END:
                    j_end = [j, i]

        time = 2000
        cont = 0
        # Now actually run the game
        # --------------------------

        while not self.game_over:
            current_frame = pygame.time.get_ticks()
            self.window.fill((0, 0, 0))

            if self.tom_ai.get_pos() == self.jerry_ai.get_pos() or \
                    self.tom_ai.get_pos() == self.map.j_end:
                self.game_over = True
            elif self.jerry_ai.get_pos() == self.map.j_end:
                self.jerry_wins = True
                self.game_over = True

            self.map.render(self.window)
            self.tom_ai.render(self.window, self.map)
            self.jerry_ai.render(self.window, self.map)

            if time <= 0 and cont == 0:
                t_pos = (self.tom_ai.x, self.tom_ai.y)
                j_pos = (self.jerry_ai.x, self.jerry_ai.y)
                self.tom_ai.y, self.tom_ai.x = self.tom_ai.algoritmo(self.map, t_pos, j_pos, (-1, -1), self.tom_ai)[1]
                time = 2000
                cont = 1

            if time <= 0 and cont == 1:
                t_pos = (self.tom_ai.x, self.tom_ai.y)
                j_pos = (self.jerry_ai.x, self.jerry_ai.y)
                self.jerry_ai.y, self.jerry_ai.x = \
                    self.jerry_ai.algoritmo(self.map, j_pos, j_end, t_pos, self.jerry_ai)[1]
                time = 2000
                cont = 0

            time -= 1

            event_handler()
            pygame.display.update()

        if self.jerry_wins:
            print("GANASTE!")
            mensaje = my_font.render("GANASTE!", False, (0, 0, 0))
        else:
            print("PERDISTE!")
            mensaje = my_font.render("PERDISTE!", False, (0, 0, 0))

        self.window.blit(mensaje, (self.window.get_width() // 2, self.window.get_width() // 2))
        pygame.display.update()
        pygame.time.delay(5 * 1000)
        pygame.quit()
        exit()
        # --------------------------


def main():
    tnj = Game((800, 600))
    tnj.run()


if __name__ == '__main__':
    main()
