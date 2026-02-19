from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, 500, 0, 500, -1, 1)
    
    glMatrixMode(GL_MODELVIEW)

def draw_SP():
    glColor3f(0.0, 1.0, 1.0)
    glLineWidth(6)

    glBegin(GL_LINES)

    # ===== S (Upper Left) =====
    glVertex2f(50, 450); glVertex2f(150, 450)
    glVertex2f(50, 450); glVertex2f(50, 400)
    glVertex2f(50, 400); glVertex2f(150, 400)
    glVertex2f(150, 400); glVertex2f(150, 350)
    glVertex2f(50, 350); glVertex2f(150, 350)

    # ===== P =====
    glVertex2f(200, 450); glVertex2f(200, 350)
    glVertex2f(200, 450); glVertex2f(280, 450)
    glVertex2f(280, 450); glVertex2f(280, 400)
    glVertex2f(200, 400); glVertex2f(280, 400)

    glEnd()

def draw_ID():
    glColor3f(1.0, 0.5, 0.0)
    glLineWidth(5)

    glBegin(GL_LINES)

    # ===== 1 =====
    glVertex2f(50, 300); glVertex2f(50, 230)

    # ===== 1 =====
    glVertex2f(90, 300); glVertex2f(90, 230)

    # ===== 6 =====
    glVertex2f(130, 300); glVertex2f(130, 230)
    glVertex2f(130, 300); glVertex2f(190, 300)
    glVertex2f(130, 265); glVertex2f(190, 265)
    glVertex2f(190, 265); glVertex2f(190, 230)
    glVertex2f(130, 230); glVertex2f(190, 230)

    # ===== 7 =====
    glVertex2f(220, 300); glVertex2f(280, 300)
    glVertex2f(280, 300); glVertex2f(220, 230)

    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    draw_SP()
    draw_ID()

    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
glutInitWindowSize(500, 500)
glutCreateWindow(b"SP - 1167")

init()
glutDisplayFunc(display)
glutMainLoop()
