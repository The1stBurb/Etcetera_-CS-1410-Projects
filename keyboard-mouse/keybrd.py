import keyboard as kb
from random import randint
kys=list("qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM")
kys2=list("qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM")
print(kys2)
for i in kys:
    ch2=kys[randint(0,len(kys)-1)]
    kys.remove(ch2)
    ch=kys2[randint(0,len(kys2)-1)]
    kys2.remove(ch)
    kb.remap_key(ch, ch2)
kb.wait(hotkey="esc")
# quit()
# # kb.add_abbreviation(source_text, replacement_text, match_suffix=False, timeout=2)
# # kb.add_abbreviation(source_text, replacement_text, match_suffix=False, timeout=2)
# # kb.add_abbreviation(source_text, replacement_text, match_suffix=False, timeout=2)
# rec=kb.record(until="esc")
# kb.play(rec,speed_factor=100)
# print("yops")
# print(kb.read_event())
# #Rtq rg lqis isj'l igiji ypry iggo!