from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from collections import namedtuple 

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 640

UNIT_PIXEL = 1

class Vector():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

eye = Vector(0, 20, 30)
center = Vector(0, 0, 0)
up = Vector(0, 1, 0)

colors ={
    "green": [143/255, 188/255, 143/255],
    "brown": [118/255, 74/255, 43/255]
}

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0) 
    
    update_camera()
    
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, WINDOW_WIDTH/WINDOW_HEIGHT, 0.1, 100.)
    glMatrixMode(GL_MODELVIEW)

def update_camera():
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(eye.x   , eye.y   , eye.z,
              center.x, center.y, center.z,
              up.x    , up.y    , up.z)

    print(f"_________________")
    print(f"eye: ({eye.x}, {eye.y}, {eye.z})")
    print(f"center: ({center.x}, {center.y}, {center.z})")
    print(f"up: ({up.x}, {up.y}, {up.z})")

def draw_teapot(size):
    glColor3fv(colors["green"])
    glutWireTeapot(size * UNIT_PIXEL)

def draw_table_foot(x, y, z):
    glPushMatrix()
    glTranslatef(x, y, z)
    glutWireCube(UNIT_PIXEL)
    glPopMatrix() 

def draw_table(width, height, depth, thickness):
    width *= UNIT_PIXEL
    height *= UNIT_PIXEL
    depth *= UNIT_PIXEL
    thickness *= UNIT_PIXEL
    offset = 2 * thickness 

    glColor3fv(colors["brown"])

    glPushMatrix()
    glTranslatef(0, -offset, 0)
    glScalef(width, thickness , depth)
    glutWireCube(UNIT_PIXEL)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0, -offset - depth // 2, 0)
    glScalef(thickness, height - thickness, thickness)
    draw_table_foot(- int(width / offset - offset / 4), 
                    0,
                    - int(depth / offset - offset / 4))
    draw_table_foot(- int(width / offset - offset / 4), 
                    0,
                    int(depth / offset - offset / 4))
    draw_table_foot(int(width / offset - offset / 4), 
                    0,
                    - int(depth / offset - offset / 4))
    draw_table_foot(int(width / offset - offset / 4), 
                    0,
                    int(depth / offset - offset / 4))                                
    glPopMatrix()   

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)

    glMatrixMode(GL_MODELVIEW)
    
    draw_table(width= 20, height= 10, depth= 10, thickness= 2)
    draw_teapot(size= 4)

    glutSwapBuffers()

def reshape(width, height):
    pass

def keyboard_handler(key, x, y):
    global eye
    global center
    global up

    # Movimentando a posição do observador (eye)
    if key == b"w":
        eye.z -= UNIT_PIXEL # Move uma unidade para frente

    elif key == b"s":
        eye.z += UNIT_PIXEL # Move uma unidade para trás

    elif key == b"d":
        eye.x += UNIT_PIXEL # Move uma unidade para direita

    elif key == b"a":
        eye.x -= UNIT_PIXEL # Move uma unidade para esquerda
    
    elif key == b"q":
        eye.y += UNIT_PIXEL # Move uma unidade para cima

    elif key == b"e":
        eye.y -= UNIT_PIXEL # Move uma unidade para baixo   

    # Movimentando a posição do ponto observado (center)
    elif key == b"i": # Código da seta para cima
        center.z -= UNIT_PIXEL # Move uma unidade para frente

    elif key == b"k": # Código da seta para baixo
        center.z += UNIT_PIXEL # Move uma unidade para trás

    elif key == b"l": # Código da seta pra direita
        center.x += UNIT_PIXEL # Move uma unidade para direita

    elif key == b"j": # Código da seta pra esquerda
        center.x -= UNIT_PIXEL # Move uma unidade para esquerda
    
    elif key == b"u": # Código da tecla page up
        center.y += UNIT_PIXEL # Move uma unidade para cima

    elif key == b"o": # Código da tecla page down
        center.y -= UNIT_PIXEL # Move uma unidade para baixo  

    # Movimentando o vetor cima da câmera
    elif key == b"f":
        if up.x != 0: # Se já estiver orientado no eixo x
            up.x *= -1   # Inverte a câmera
        else: 
            up.x = 1
        
        up.y = 0
        up.z = 0
    
    elif key == b"g":
        if up.y != 0: # Se já estiver orientado no eixo y
            up.y *= -1   # Inverte a câmera
        else: 
            up.y = 1
        
        up.x = 0
        up.z = 0

    elif key == b"h":
        if up.z != 0: # Se já estiver orientado no eixo z
            up.z *= -1   # Inverte a câmera
        else: 
            up.z = 1
        
        up.x = 0
        up.y = 0

    update_camera()

    glutPostRedisplay()

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_DEPTH | GLUT_RGB)
glutInitWindowPosition(0,0)
glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)  
glutCreateWindow("Teapot")

init() 

glutDisplayFunc(display)
glutReshapeFunc(reshape)
glutKeyboardFunc(keyboard_handler)

glutMainLoop()