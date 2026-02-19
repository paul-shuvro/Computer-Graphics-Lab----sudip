import random
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0) 
    
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, 500, 0, 500, -1, 1)
    
    glMatrixMode(GL_MODELVIEW)

def draw_pixels():

    glColor3f(0.0, 1.0, 1.0) 

    glBegin(GL_POINTS)

    for i in range(50): 
        x = random.randint(10, 500)
        y = random.randint(10, 500)
        glVertex2f(x, y)

    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    draw_pixels()

    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
glutInitWindowSize(500, 500)
glutCreateWindow(b"50 Random Pixels")

init()
glutDisplayFunc(display)
glutMainLoop()
