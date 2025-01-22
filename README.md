# TETRIS
[![descarga.jpg](https://i.postimg.cc/RZhw1RLy/descarga.jpg)](https://postimg.cc/BjW842yB)
<p align="center" > 
  
# DESCRIPCION
El programa de Tetris que realicé es una implementación básica del popular juego Tetris utilizando la biblioteca pygameen Python. A continuación, te explico los elementos principales del programa y cómo funciona:
[![Captura-de-pantalla-2025-01-22-142409.png](https://i.postimg.cc/gj4GN3HB/Captura-de-pantalla-2025-01-22-142409.png)](https://postimg.cc/YLGcSGV1)
# Elementos del Programa
Tablero de juego

- El tablero está representado como una cuadrícula de bloques (10 columnas x 20 filas).
Cada celda del tablero puede estar vacía o contener un bloque de un color específico.
Piezas de Tetris

- Las piezas están representadas como formas hechas de bloques (L, T, I, Z, S, J, O).
Cada pieza tiene rotaciones posibles que se manejan con una lista de configuraciones.
Movimiento de piezas

- Las piezas caen automáticamente hacia abajo a intervalos regulares.
El jugador puede mover las piezas hacia la izquierda, derecha o rotarlas.
Eliminación de Filas

- Cuando una fila se llena completamente de bloques, se elimina, y las filas superiores se desplazan hacia abajo.
colisiones

- El programa detecta colisiones con el borde del tablero, otras piezas o el fondo del tablero.
Si una pieza no puede moverse más hacia abajo, se fija en su posición actual, y una nueva pieza aparece en la parte superior.
Puntuación

- Cada fila eliminada incrementa la puntuación del jugador.
- Las filas eliminadas simultáneamente otorgan más puntos (por ejemplo, 4 filas = un "Tetris").
Juego terminado

El juego termina si las piezas alcanzan la parte superior del tablero.

# ESTRUCTURAS DEL JUEGO
Ustedes se preguntaran como se realiza este programa,estos son los siguientes pasos:
- pygame.init(): Inicializa todos los módulos de Pygame.
- Parámetros de la cuadrícula: Dividimos la pantalla en bloques para facilitar el manejo de las piezas.
- Colores: Definimos colores para las piezas y el fondo.
  
  #### EJEMPLO
  ```
  import pygame
  import random
  #Inicializamos pygame
  pygame.init()
  
  #configuracion de pantalla
  SCREEN_WIDTH = 300
  SCREN_HEIGHT = 600
  BLOCK_SIZE = 30 #tamaño de cada bloque
  
  #configuracion de tablero
  GRID_WIDTH = SCREEN_WIDTH // BLOCK_SIZE
  GRID_HEIGHT = SCREEN_HEIGHT // BLOCK_SIZE
  #Colores
  WHITE = (255,255,255)
  BLACK = (0, 0 , 0)
  COLORS = [
    (0, 255, 255),  # Cyan
    (255, 165, 0),  # Orange
    (0, 255, 0),    # Green
    (255, 0, 0),    # Red
    (0, 0, 255),    # Blue
    (128, 0, 128),  # Purple
    (255, 255, 0)   # Yellow
  ]
  #Inicialización de la ventana
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  pygame.display.set_caption("Tetris")
  
 - Crear el tablero y las funciones principales
   
### EJEMPLO

```
def create_grid(locked_positions={}):
    grid = [[BLACK for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
    for (x, y), color in locked_positions.items():
        grid[y][x] = color
    return grid

def draw_grid(surface, grid):
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            pygame.draw.rect(
                surface,
                grid[y][x],
                (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
            )
    # Dibujar líneas de la cuadrícula
    for x in range(GRID_WIDTH):
        pygame.draw.line(surface, WHITE, (x * BLOCK_SIZE, 0), (x * BLOCK_SIZE, SCREEN_HEIGHT))
    for y in range(GRID_HEIGHT):
        pygame.draw.line(surface, WHITE, (0, y * BLOCK_SIZE), (SCREEN_WIDTH, y * BLOCK_SIZE))











  

