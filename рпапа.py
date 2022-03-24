from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class testApp(MDApp):
    def buid(self):
        return MDLabel(text="Привет, я гид Ракитянского района", halign="center")


testApp().run()