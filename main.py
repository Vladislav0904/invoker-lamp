from yeelight import Bulb
import keyboard
from time import sleep

WEX = 255, 0, 255
QUAS = 0, 30, 154
buffer = []
bulb = Bulb("192.168.1.175")
bulb.turn_on()
bulb.set_rgb(102, 153, 255)
bulb.set_rgb(255, 0, 255)
bulb.set_rgb(255, 139, 0)
bulb.set_brightness(5)


def clear_buffer(buffer):
    buffer.clear()
    bulb.set_rgb(255, 255, 255)


def edit_buffer(button, buffer, call=False):
    if button == 'Q':
        bulb.set_rgb(102, 153, 255)
        if not call:
            if len(buffer) >= 3:
                buffer.pop(0)
            buffer.append('Q')
    elif button == 'W':
        bulb.set_rgb(255, 0, 255)
        if not call:
            if len(buffer) >= 3:
                buffer.pop(0)
            buffer.append('W')
    elif button == 'E':
        bulb.set_rgb(255, 139, 0)
        if not call:
            if len(buffer) >= 3:
                buffer.pop(0)
            buffer.append('E')
    set_brightness(buffer)


def set_brightness(buffer):
    if len(buffer) != 0:
        if buffer.count(buffer[-1]) == 1:
            bulb.set_brightness(50)
        elif buffer.count(buffer[-1]) == 2:
            bulb.set_brightness(75)
        elif buffer.count(buffer[-1]) == 3:
            bulb.set_brightness(100)
    else:
        bulb.set_brightness(50)
    print(buffer)


def invoke(buffer):
    bulb.set_brightness(100)
    bulb.set_rgb(255, 0, 0)
    sleep(0.5)
    if len(buffer) != 0:
        edit_buffer(buffer[-1], buffer, call=True)
    set_brightness(buffer)


keyboard.add_hotkey('+', lambda: clear_buffer(buffer))
keyboard.add_hotkey('Q', lambda: edit_buffer('Q', buffer))
keyboard.add_hotkey('W', lambda: edit_buffer('W', buffer))
keyboard.add_hotkey('E', lambda: edit_buffer('E', buffer))
keyboard.add_hotkey('R', lambda: invoke(buffer))
keyboard.wait('Ctrl + Q')
