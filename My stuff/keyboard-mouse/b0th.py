import mouse as ms
import keyboard as kb
from time import sleep,perf_counter
kb.wait("esc")
s=perf_counter()
for i in range(10000):
    ms.click("left")
    # ms.move(-10,-10,absolute=False,duration=10)
    # sleep(0.01)
    # kb.press
print("waps",perf_counter()-s)