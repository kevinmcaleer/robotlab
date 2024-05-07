from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.relativelayout import RelativeLayout
from kivy.graphics import Color, Line, Rectangle
from kivy.core.window import Window

class GPIOCanvas(RelativeLayout):
    def __init__(self, **kwargs):
        super(GPIOCanvas, self).__init__(**kwargs)
        with self.canvas:
            Color(0.8, 0.8, 0.8, 1)
            self.bg = Rectangle(size=Window.size)

        self.bind(size=self.adjust_background)

    def adjust_background(self, **args):
        self.bg.size = self.size

class GPIOApp(App):
    def build(self):
        return GPIOCanvas()

if __name__ == '__main__':
    GPIOApp().run()