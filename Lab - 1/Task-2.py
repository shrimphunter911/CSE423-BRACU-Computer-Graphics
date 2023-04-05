from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def draw_points(x, y):
    glPointSize(5)  # pixel size.
    glBegin(GL_POINTS)
    glColor3f(1, 1, 1)
    glVertex2f(x, y)
    glEnd()


def draw_triangle():
    glBegin(GL_TRIANGLES)
    glColor3f(0.6, 0.3, 0.0)
    glVertex2f(375, 250)
    glVertex2f(250, 350)
    glVertex2f(125, 250)
    glEnd()


def draw_lines():
    glBegin(GL_LINES)
    glColor3f(0.6, 0.3, 0.0)
    glVertex2f(130, 250)
    glVertex2f(130, 50)
    glVertex2f(130, 50)
    glVertex2f(370, 50)
    glVertex2f(370, 50)
    glVertex2f(370, 250)
    glEnd()


def draw_quads():
    glBegin(GL_QUADS)
    glColor3f(0.5, 0.5, 0.5)
    glVertex2f(200, 225)
    glVertex2f(140, 225)
    glVertex2f(140, 175)
    glVertex2f(200, 175)
    # 2nd window
    glVertex2f(360, 175)
    glVertex2f(300, 175)
    glVertex2f(300, 225)
    glVertex2f(360, 225)
    # door
    glVertex2f(225, 50)
    glVertex2f(225, 150)
    glVertex2f(275, 150)
    glVertex2f(275, 50)
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
    # call the draw methods here
    draw_triangle()
    draw_lines()
    draw_quads()
    draw_points(270, 120)
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)  # window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice")  # window name
glutDisplayFunc(showscreen)

glutMainLoop()
