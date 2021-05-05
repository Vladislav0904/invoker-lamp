from yeelight import Bulb
import keyboard


WEX = 255, 0, 255
QUAS = 0, 30, 154

bulb = Bulb("192.168.1.175")
bulb.turn_on()
bulb.set_rgb(102, 153, 255)
bulb.set_rgb(255, 0, 255)
bulb.set_rgb(255, 139, 0)

keyboard.add_hotkey('Q', lambda: bulb.set_rgb(102, 153, 255))
keyboard.add_hotkey('W', lambda: bulb.set_rgb(255, 0, 255))
keyboard.add_hotkey('E', lambda: bulb.set_rgb(255, 139, 0))

keyboard.wait('Ctrl + Q')