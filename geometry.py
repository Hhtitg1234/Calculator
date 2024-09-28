import math


def sin(angle):
    return math.sin(angle)


def cos(angle):
    return math.cos(angle)


def tan(angle):
    return math.tan(angle)


def s_triangle(a, h):
    return 0.5*a*h


def p_triangle(a, b, c):
    return a+b+c


def s_circle(r):
    return 3.14*(r**2)


def p_circle(r):
    return 2*3.14*r


def s_prym(a, b):
    return a*b


def p_prym(a, b):
    return (a+b)*2
