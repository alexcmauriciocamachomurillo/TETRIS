import pygame
import random

# Configuración del juego
WIDTH, HEIGHT = 300, 600
BLOCK_SIZE = 30
GRID_WIDTH = WIDTH // BLOCK_SIZE
GRID_HEIGHT = HEIGHT // BLOCK_SIZE

# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [
    (255, 0, 0), (0, 255, 0), (0, 0, 255),
    (255, 255, 0), (0, 255, 255), (255, 165, 0), (128, 0, 128)
]

# Formas de Tetris
SHAPES = [
    [[1, 1, 1], [0, 1, 0]],  # T
    [[1, 1], [1, 1]],        # O
    [[1, 1, 1, 1]],          # I
    [[0, 1, 1], [1, 1, 0]],  # S
    [[1, 1, 0], [0, 1, 1]],  # Z
    [[1, 1, 1], [1, 0, 0]],  # L
    [[1, 1, 1], [0, 0, 1]]   # J
]

# Clase para las piezas
class Piece:
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = random.choice(COLORS)

    def rotated_shape(self):
        return [list(row) for row in zip(*self.shape[::-1])]

# Crear la cuadrícula
def create_grid(locked_positions={}):
    grid = [[BLACK for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
    for (x, y), color in locked_positions.items():
        grid[y][x] = color
    return grid

# Dibujar la cuadrícula
def draw_grid(screen, grid):
    for y, row in enumerate(grid):
        for x, color in enumerate(row):
            pygame.draw.rect(screen, color, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            pygame.draw.rect(screen, WHITE, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)

# Dibujar la pieza actual
def draw_piece(screen, piece):
    for i, row in enumerate(piece.shape):
        for j, cell in enumerate(row):
            if cell:
                pygame.draw.rect(
                    screen,
                    piece.color,
                    ((piece.x + j) * BLOCK_SIZE, (piece.y + i) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
                )

# Verificar espacio válido
def valid_space(piece, grid):
    for i, row in enumerate(piece.shape):
        for j, cell in enumerate(row):
            if cell:
                x, y = piece.x + j, piece.y + i
                if x < 0 or x >= GRID_WIDTH or y >= GRID_HEIGHT or grid[y][x] != BLACK:
                    return False
    return True

# Borrar filas completas
def clear_rows(grid, locked_positions):
    cleared = 0
    for y in range(GRID_HEIGHT - 1, -1, -1):
        if BLACK not in grid[y]:  # Fila completa
            cleared += 1
            del grid[y]
            grid.insert(0, [BLACK for _ in range(GRID_WIDTH)])
            # Actualizar posiciones bloqueadas
            keys_to_remove = [(x, y) for (x, y) in locked_positions if y == y]
            for key in keys_to_remove:
                del locked_positions[key]
            for key in sorted(list(locked_positions.keys()), key=lambda k: k[1], reverse=True):
                x, y = key
                if y < y:
                    locked_positions[(x, y + 1)] = locked_positions.pop(key)
    return cleared

# Juego principal
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tetris")
    clock = pygame.time.Clock()

    locked_positions = {}
    grid = create_grid(locked_positions)

    current_piece = Piece(GRID_WIDTH // 2 - 1, 0, random.choice(SHAPES))
    running = True
    fall_time = 0
    score = 0

    while running:
        grid = create_grid(locked_positions)
        fall_speed = 500  # Velocidad de caída en milisegundos
        fall_time += clock.get_rawtime()
        clock.tick()

        # Manejar caída automática
        if fall_time >= fall_speed:
            current_piece.y += 1
            if not valid_space(current_piece, grid):
                current_piece.y -= 1
                for i, row in enumerate(current_piece.shape):
                    for j, cell in enumerate(row):
                        if cell:
                            locked_positions[(current_piece.x + j, current_piece.y + i)] = current_piece.color
                current_piece = Piece(GRID_WIDTH // 2 - 1, 0, random.choice(SHAPES))
                if not valid_space(current_piece, grid):
                    running = False  # Fin del juego
                score += clear_rows(grid, locked_positions)
            fall_time = 0

        # Manejo de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1
                    if not valid_space(current_piece, grid):
                        current_piece.x += 1
                if event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                    if not valid_space(current_piece, grid):
                        current_piece.x -= 1
                if event.key == pygame.K_DOWN:
                    current_piece.y += 1
                    if not valid_space(current_piece, grid):
                        current_piece.y -= 1
                if event.key == pygame.K_UP:
                    current_piece.shape = current_piece.rotated_shape()
                    if not valid_space(current_piece, grid):
                        current_piece.shape = current_piece.rotated_shape()[::-1]

        # Dibujar todo
        screen.fill(BLACK)
        draw_grid(screen, grid)
        draw_piece(screen, current_piece)
        pygame.display.update()

    pygame.quit()

main()
