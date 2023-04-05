from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def draw_points(x, y):
    glPointSize(10)  # pixel size.
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


def print_id():

    # 7
    draw_line(100, 200, 200, 200)
    draw_line(200, 200, 135, 100)

    # 9
    draw_line(250, 200, 350, 200)
    draw_line(250, 100, 350, 100)
    draw_line(350, 100, 350, 200)
    draw_line(250, 150, 250, 200)
    draw_line(250, 150, 350, 150)

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
    print_id()
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)  # window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice")  # window name
glutDisplayFunc(showscreen)

glutMainLoop()
