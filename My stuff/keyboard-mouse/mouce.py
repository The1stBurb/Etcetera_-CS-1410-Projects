from time import sleep
from random import randint
import mouse as ms
# for i in range(2):
#     x=randint(0,200)
#     y=randint(0,200)
#     mouse.move(x,y,duration=10,steps_per_second=5)
# while True:
#     print(ms.get_position())
#     sleep(0.5)
#399,290
#y is ~20, x is ~10
#below is 350
#akb Dfg Hvq
ms.move(372,350)
ms.press("left")
ms.move(20,0,absolute=False)
ms.release("left")
# ms.move(-10,0,absolute=False)
# ms.click("right")