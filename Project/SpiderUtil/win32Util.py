import ctypes

from win32api import win32api,win32con


def mouse_down(posX, posY):  # 鼠标按下不放，从一个坐标点直线拖动到另外一个坐标点
    print("down = %d,%d" % (posX, posY))
    ctypes.windll.user32.SetCursorPos(posX, posY)  # 鼠标按下的坐标点
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, posX, posY, posX, posY)


def mouse_move(posX, posY):  # 鼠标按下不放，从一个坐标点直线拖动到另外一个坐标点
    print("move = %d,%d" % (posX, posY))
    win32api.mouse_event(win32con.MOUSEEVENTF_ABSOLUTE + win32con.MOUSEEVENTF_MOVE, posX, posY, 0, 0)
    ctypes.windll.user32.SetCursorPos(posX, posY)  # 鼠标停在最后弹起的坐标点


def mouse_up(posX, posY):  # 鼠标按下不放，从一个坐标点直线拖动到另外一个坐标点
    print("up = %d,%d" % (posX, posY))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, posX, posY, posX, posY)
    ctypes.windll.user32.SetCursorPos(posX, posY)  # 鼠标停在最后弹起的坐标点


mouse_down(670, 880 - 182)
mouse_up(670, 880 - 182)
time.sleep(1)
mouse_down(670, 880 - 182)
time.sleep(1)
for i in range(1, 5):
    time.sleep(1)
    offsetX = random.randint(300, 500)
    mouse_move(670 + offsetX, 880 - 182)

mouse_up(670, 880 - 182)
