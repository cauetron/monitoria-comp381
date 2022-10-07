from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 640

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)

def draw_triangle():
    glBegin(GL_POLYGON)
    glColor3f(1, 0, 0)
    glVertex3f(-0.6, -0.75, 0.5)
    glColor3f(0, 1, 0)
    glVertex3f(0.6, -0.75, 0)
    glColor3f(0, 0, 1)
    glVertex3f(0, 0.75, 0)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)
    draw_triangle()
    glutSwapBuffers()

def idle_display():
    glutPostRedisplay()

def reshape(w, h):
    pass

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
glutInitWindowPosition(50, 50)
glutCreateWindow("Hello World")
init()
glutDisplayFunc(display)
glutIdleFunc(idle_display)
glutReshapeFunc(reshape)
glutMainLoop()
