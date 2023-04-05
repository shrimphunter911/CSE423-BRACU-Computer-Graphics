from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import time
import numpy as np

user_input = (input("Enter B for Kick or A for Punch: "))
n = 0
xt = 250
yt = 1

def draw_points(x, y):
    glPointSize(1)  # pixel size.
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()


def findZone(dx, dy):
    if abs(dx) > abs(dy):
        if dx >= 0 and dy >= 0:
            return 0
        elif dx <= 0 <= dy:
            return 3
        elif dx <= 0 and dy <= 0:
            return 4
        elif dx >= 0 >= dy:
            return 7
    elif abs(dx) < abs(dy):
        if dx >= 0 and dy >= 0:
            return 1
        elif dx <= 0 <= dy:
            return 2
        elif dx <= 0 and dy <= 0:
            return 5
        elif dx >= 0 >= dy:
            return 6


def convertZero(zone, x, y):
    if zone == 0:
        return x, y
    elif zone == 1:
        return y, x
    elif zone == 2:
        return y, -x
    elif zone == 3:
        return -x, y
    elif zone == 4:
        return -x, -y
    elif zone == 5:
        return -y, -x
    elif zone == 6:
        return -y, x
    elif zone == 7:
        return x, -y


def convertOriginal(zone, x, y):
    if zone == 0:
        return x, y
    elif zone == 1:
        return y, x
    elif zone == 2:
        return -y, x
    elif zone == 3:
        return -x, y
    elif zone == 4:
        return -x, -y
    elif zone == 5:
        return -y, -x
    elif zone == 6:
        return y, -x
    elif zone == 7:
        return x, -y


def midPoint(x1, y1, x2, y2, zone):
    dx = x2 - x1
    dy = y2 - y1
    d = (2 * dy) - dx
    x = x1
    y = y1
    for x in range(x, x2):
        px, py = convertOriginal(zone, x, y)
        draw_points(px, py)
        if d < 0:
            d = d + 2 * dy
        else:
            y += 1
            d = d + 2 * (dy - dx)


def draw_line(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    zone = findZone(dx, dy)
    x1, y1 = convertZero(zone, x1, y1)
    x2, y2 = convertZero(zone, x2, y2)
    midPoint(x1, y1, x2, y2, zone)


def circle_points(x, y, xi, yi):
    draw_points(x + xi, y + yi)
    draw_points(y + xi, x + yi)
    draw_points(y + xi, -x + yi)
    draw_points(x + xi, -y + yi)
    draw_points(-x + xi, -y + yi)
    draw_points(-y + xi, -x + yi)
    draw_points(-y + xi, x + yi)
    draw_points(-x + xi, y + yi)


def draw_circle(x0, y0, radius):
    d = 1 - radius
    x = 0
    y = radius
    circle_points(x, y, x0, y0)

    while x < y:

        if d < 0:
            d = d + 2 * x + 3
            x = x + 1
        else:
            d = d + 2 * x - 2 * y + 5
            x = x + 1
            y = y - 1
        circle_points(x, y, x0, y0)


def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 800, 0.0, 800, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def draw_player():
    # Head
    for i in range(50, 0, -1):
        draw_circle(150, 500, i)
    # User Stick Figure
    draw_line(150, 350, 150, 450)
    # User Hand
    draw_line(75, 400, 150, 400)
    draw_line(225, 400, 150, 400)
    # User Leg
    draw_line(75, 100, 150, 350)
    draw_line(225, 100, 150, 350)


def player_punch():
    # Head
    for i in range(50, 0, -1):
        draw_circle(150, 500, i)
    # User Stick Figure
    draw_line(150, 350, 150, 450)
    # User Hand
    draw_line(75, 400, 150, 400)
    draw_line(150, 400, 300, 500)
    # User Leg
    draw_line(75, 100, 150, 350)
    draw_line(225, 100, 150, 350)


def player_kick():
    # Head
    for i in range(50, 0, -1):
        draw_circle(150, 500, i)
    # User Stick Figure
    draw_line(150, 350, 150, 450)
    # User Hand
    draw_line(75, 400, 150, 400)
    draw_line(225, 400, 150, 400)
    # User Leg
    draw_line(75, 100, 150, 350)
    draw_line(300, 450, 150, 350)


def draw_computer():
    # Head
    for j in range(50, 0, -1):
        draw_circle(350, 500, j)
    # Computer Stick Figure
    draw_line(350, 350, 350, 450)
    # CPU Hand
    draw_line(275, 400, 350, 400)
    draw_line(350, 400, 425, 400)
    # CPU Leg
    draw_line(275, 100, 350, 350)
    draw_line(425, 100, 350, 350)


def fallen_computer():


    global xt
    for j in range(50, 0, -1):
        draw_circle(xt+100, 500, j)
    # Computer Stick Figure
    draw_line(xt+100, 350, xt+100, 450)
    # CPU Hand
    draw_line(xt+25, 400, xt+100, 400)
    draw_line(xt+100, 400, xt+175, 400)
    # CPU Leg
    draw_line(xt+25, 100, xt+100, 350)
    draw_line(xt+175, 100, xt+100, 350)



def showscreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 0.25, 1.0)
    # call the draw methods here
    global n
    global user_input
    if user_input == "A":
        if n % 2 == 0:
            draw_player()
            glColor3f(0.0, 1.0, 0.0)
            draw_computer()
        else:
            player_punch()
            glColor3f(1.0, 0.0, 0.0)
            fallen_computer()
    elif user_input == "B":
        if n % 2 == 0:
            draw_player()
            glColor3f(0.0, 1.0, 0.0)
            draw_computer()
        else:
            player_kick()
            glColor3f(1.0, 0.0, 0.0)
            fallen_computer()


    glFlush()
    glutSwapBuffers()


def idle():
    global n, angle, xt, yt
    n += 1
    xt += 25
    yt = yt/1.2
    time.sleep(0.7)
    glutPostRedisplay()


glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(600, 600)  # window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice")  # window name
glutDisplayFunc(showscreen)
glutIdleFunc(idle)
glClearColor(0.0, 0.0, 0.0, 0.0)
glEnable(GL_DEPTH_TEST)
glutMainLoop()
