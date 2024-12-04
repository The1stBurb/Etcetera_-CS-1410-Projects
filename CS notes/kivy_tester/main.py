from kivy.app import App
# from kivy.uix.label import Label
from kivy.lang import Builder
class helloApp(App):
    def build(self):
        return Builder.load_file("main.kv")
        #Label(text="Hey App")
helloApp().run()
#label is text on screen
#can set font size, 
# suprise a button is a clicky button!
#also suprise text input is an texty inputter
#hint_text is a hint to what to include

#checkboxes, active true is already checked


#put visual stuff in main.kv