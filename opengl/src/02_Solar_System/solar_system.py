from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from numpy import interp
import sys

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 640
SLICES, STACKS = 15, 15
DELAY = 1000//60 # glutTimerFunc callback's delay
VIRTUAL_TIME = 0.6 # determines how fast is our virtual time
                   # the higher, the faster
EARTH_RADIUS = 0.1
MARS_RADIUS = EARTH_RADIUS/1.88
MOON1_RADIUS = EARTH_RADIUS/3.66
MOON2_RADIUS = EARTH_RADIUS/7
SUN_RADIUS = EARTH_RADIUS*4

year = 0 # time between the current moment and the start of the application

is_paused = False # keeps track of the application current state



def period_to_angle(max):
  '''
  Maps the current position of our object given the current time and their
  cicle. The position is represented by an angle between 0° and 360°
  '''
  return interp(year%max, [0,max], [0, 360])

def draw_sun():
  glColor4f(1.0, 1.0, 0.0, 1.0) # yellow
  glutSolidSphere(SUN_RADIUS, SLICES*2, STACKS*2)

def draw_moon_1():
  glPushMatrix()

  # rotation around the previous object (earth, in this case)
  glRotatef(period_to_angle(27.3), 0, 1, 0)
  glTranslatef(0.2, 0, 0)

  glPushMatrix()
  glRotatef(period_to_angle(27), 0, 1, 0) # moon1's spin around its own axis(y)
  glColor4f(0.6, 0.6, 0.6, 1.0) # light gray
  glutWireSphere(MOON1_RADIUS, SLICES, STACKS)
  glPopMatrix()

  glPopMatrix()

def draw_moon_2():
  glPushMatrix()

  # rotation around the previous object (earth, in this case)

  #glRotatef(period_to_angle(400), 1, 0, 0) # around y axis
  #glTranslatef(0, 0.25, 0) # around y axis

  glRotatef(period_to_angle(400), 1, 1, 0) # around xy axis
  glTranslatef(-0.2, 0.2, 0) # around xy axis

  glPushMatrix()
  glRotatef(period_to_angle(400), 0, 1, 0) # moon2's spin around its own axis(y)
  glColor4f(0, 1, 0, 1.0) #green
  glutWireSphere(MOON2_RADIUS, SLICES, STACKS)
  glPopMatrix()

  glPopMatrix()

def draw_earth_with_two_moons():
  glPushMatrix()

  # counterclockwise rotation around the previous object (sun, in this case)
  glRotatef(period_to_angle(365), 0, 1, 0)
  glTranslatef(0.8, 0, 0)

  glPushMatrix()
  glRotatef(period_to_angle(24), 0, 1, 0) # earth's spin around its own axis(y)
  glColor4f(0.0, 0.0, 1.0, 1.0) # blue
  glutWireSphere(EARTH_RADIUS, SLICES, STACKS)
  glPopMatrix()

  draw_moon_1()
  draw_moon_2()

  glPopMatrix()

def draw_mars():
  glPushMatrix()

  # clockwise rotation around the previous object (sun, in this case)
  glRotatef(-period_to_angle(687), 0, 1, 0)
  glTranslatef(1, 0, 0)

  glPushMatrix()
  glRotatef(period_to_angle(24), 0, 1, 0) # mars' spin around its own axis(y)
  glColor4f(1.0, 0.0, 0.0, 1.0) # red
  glutWireSphere(MARS_RADIUS, SLICES, STACKS)
  glPopMatrix()

  glPopMatrix()

def init():
  glClearColor(0.0, 0.0, 0.0, 1.0) # set background color to black

def display():
  glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
  glEnable(GL_DEPTH_TEST)

  draw_sun()
  draw_earth_with_two_moons()
  draw_mars()

  glutSwapBuffers()

def timer(v):
  global year
  if not is_paused: # only redraws the canvas is our application is not paused
    year += VIRTUAL_TIME
    glutPostRedisplay()

  glutTimerFunc(DELAY, timer, v)

def keyboard_handler(key, x, y):
    global is_paused

    if key == b'y': # pause/start the application if the Y-key is pressed
      print("Y-key was pressed")
      is_paused = not is_paused

    glutPostRedisplay()

def reshape(w, h):
  pass

def main():
  glutInit(sys.argv)
  glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
  glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
  glutInitWindowPosition(50, 50)
  glutCreateWindow("Solar System")
  init()
  glutDisplayFunc(display)
  glutTimerFunc(DELAY, timer, 0)
  glutReshapeFunc(reshape)
  glutKeyboardFunc(keyboard_handler)
  glutMainLoop()

if __name__ == "__main__":
    main()
