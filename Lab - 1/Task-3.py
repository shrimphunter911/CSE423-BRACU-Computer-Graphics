from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def draw_points(x, y):
    glPointSize(5)  # pixel size.
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()


def draw_lines():
    glLineWidth(10)
    glBegin(GL_LINES)
    # 1
    glColor3f(0, 0, 1)
    glVertex2f(50, 50)
    glVertex2f(50, 250)
    # 9
    glColor3f(0, 1, 0)
    glVertex2f(60, 150)
    glVertex2f(60, 250)
    glVertex2f(60, 250)
    glVertex2f(90, 250)
    glVertex2f(90, 250)
    glVertex2f(90, 50)
    glVertex2f(60, 50)
    glVertex2f(90, 50)
    glVertex2f(60, 150)
    glVertex2f(90, 150)
    # 2
    glColor3f(0, 1, 1)
    glVertex2f(100, 175)
    glVertex2f(100, 250)
    glVertex2f(100, 250)
    glVertex2f(130, 250)
    glVertex2f(130, 250)
    glVertex2f(100, 50)
    glVertex2f(100, 50)
    glVertex2f(130, 50)
    # 0
    glColor3f(1, 0, 0)
    glVertex2f(140, 50)
    glVertex2f(140, 250)
    glVertex2f(140, 250)
    glVertex2f(170, 250)
    glVertex2f(170, 250)
    glVertex2f(170, 50)
    glVertex2f(170, 50)
    glVertex2f(140, 50)
    # 1
    glColor3f(1, 0, 1)
    glVertex2f(190, 50)
    glVertex2f(190, 250)
    # 0
    glColor3f(1, 1, 0)
    glVertex2f(200, 50)
    glVertex2f(200, 250)
    glVertex2f(200, 250)
    glVertex2f(230, 250)
    glVertex2f(230, 250)
    glVertex2f(230, 50)
    glVertex2f(230, 50)
    glVertex2f(200, 50)
    # 7
    glColor3f(1, 1, 1)
    glVertex2f(240, 250)
    glVertex2f(270, 250)
    glVertex2f(270, 250)
    glVertex2f(240, 50)
    # 9
    glColor3f(0.5, 0.5, 0.5)
    glVertex2f(280, 150)
    glVertex2f(280, 250)
    glVertex2f(280, 250)
    glVertex2f(310, 250)
    glVertex2f(310, 250)
    glVertex2f(310, 50)
    glVertex2f(280, 50)
    glVertex2f(310, 50)
    glVertex2f(280, 150)
    glVertex2f(310, 150)
    glEnd()



def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def showscreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 0.25, 1.0)
    # call the draw methods here
    draw_lines()
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)  # window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice")  # window name
glutDisplayFunc(showscreen)

glutMainLoop()
