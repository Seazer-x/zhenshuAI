import turtle as ttl


def drawCircle(x, y, rad, c='red', ps=10):
    ttl.pu()
    ttl.pensize(ps)
    ttl.goto(x, y)
    ttl.pd()
    ttl.color(c)
    ttl.circle(rad, 360)


def drawOlympicRings(x, y, rad, interval: int, pensize: int):
    drawCircle(x, y, rad, 'blue')
    drawCircle(interval, y, rad, 'black')
    drawCircle(interval * 2, y, rad)
    drawCircle(interval / 2, -rad, rad, 'yellow')
    drawCircle(interval * 3 / 2, -rad, rad, 'green')


if __name__ == '__main__':
    drawOlympicRings(0, 0, 60, 90, 7)
