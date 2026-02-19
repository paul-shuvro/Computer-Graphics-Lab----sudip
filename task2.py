from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)  
    
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, 500, 0, 500, -1, 1)
    
    glMatrixMode(GL_MODELVIEW)

def draw_house():

    glColor3f(0.0, 1.0, 1.0)  
    glLineWidth(2)

    glBegin(GL_LINES)

    # House Body
    glVertex2f(150, 100); glVertex2f(350, 100)
    glVertex2f(150, 100); glVertex2f(150, 300)
    glVertex2f(350, 100); glVertex2f(350, 300)
    glVertex2f(150, 300); glVertex2f(350, 300)

    # Roof
    glVertex2f(150, 300); glVertex2f(250, 420)
    glVertex2f(350, 300); glVertex2f(250, 420)

    # Left Window (Upper)
    glVertex2f(180, 260); glVertex2f(230, 260)
    glVertex2f(180, 220); glVertex2f(230, 220)
    glVertex2f(180, 220); glVertex2f(180, 260)
    glVertex2f(230, 220); glVertex2f(230, 260)
 

    # Right Window (Upper)
    glVertex2f(270, 260); glVertex2f(320, 260)
    glVertex2f(270, 220); glVertex2f(320, 220)
    glVertex2f(270, 220); glVertex2f(270, 260)
    glVertex2f(320, 220); glVertex2f(320, 260)


    # Door
    glVertex2f(220, 100); glVertex2f(280, 100)
    glVertex2f(220, 100); glVertex2f(220, 170)
    glVertex2f(280, 100); glVertex2f(280, 170)
    glVertex2f(220, 170); glVertex2f(280, 170)

    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    draw_house()
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
glutInitWindowSize(500, 500)
glutCreateWindow(b"My House")

init()
glutDisplayFunc(display)
glutMainLoop()
