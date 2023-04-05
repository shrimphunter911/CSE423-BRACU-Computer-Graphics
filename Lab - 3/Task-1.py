from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math


def draw_points(x, y):
    glPointSize(4)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()


def Circlepoints(x, y, xi, yi):
    draw_points(x + xi, y + yi)
    draw_points(y + xi, x + yi)
    draw_points(y + xi, -x + yi)
    draw_points(x + xi, -y + yi)
    draw_points(-x + xi, -y + yi)
    draw_points(-y + xi, -x + yi)
    draw_points(-y + xi, x + yi)
    draw_points(-x + xi, y + yi)


def midPointCircleAlgorithm(x0, y0, radius):
    d = 1 - radius
    x = 0
    y = radius
    Circlepoints(x, y, x0, y0)

    while x < y:

        if d < 0:
            d = d + 2 * x + 3
            x = x + 1
        else:
            d = d + 2 * x - 2 * y + 5
            x = x + 1
            y = y - 1
        Circlepoints(x, y, x0, y0)


def eightWayCircle(x, y, radius):
    midPointCircleAlgorithm(x, y, radius)
    midPointCircleAlgorithm(x + (radius / 2), y, radius / 2)
    midPointCircleAlgorithm(x, y + (radius / 2), radius / 2)
    midPointCircleAlgorithm(x, y - (radius / 2), radius / 2)
    midPointCircleAlgorithm(x - (radius / 2), y, radius / 2)
    diff = radius * (1 / 9)
    x0 = x + (radius / 2) - diff
    y0 = y + (math.sin(45) * (radius / 2)) - diff
    midPointCircleAlgorithm(x0, y0, radius / 2)
    x0 = x + (radius / 2) - diff
    y0 = y - (math.sin(45) * (radius / 2)) + diff
    midPointCircleAlgorithm(x0, y0, radius / 2)
    x0 = x - (radius / 2) + diff
    y0 = y - (math.sin(45) * (radius / 2)) + diff
    midPointCircleAlgorithm(x0, y0, radius / 2)
    x0 = x - (radius / 2) + diff
    y0 = y + (math.sin(45) * (radius / 2)) - diff
    midPointCircleAlgorithm(x0, y0, radius / 2)


def iterate():
    glViewport(0, 0, 800, 800)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 1000, 0.0, 1000, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def showscreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 0.25, 1.0)
    # call the draw methods here
    eightWayCircle(500, 500, 400)
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1280, 720)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice")
glutDisplayFunc(showscreen)
glutMainLoop()