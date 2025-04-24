from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.behaviors import ButtonBehavior
from kivy.utils import get_color_from_hex
import threading
from detection3 import run_voice2vision
from kivy.app import App
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle

# Set window size for desktop testing (remove this line for mobile app)
Window.size = (400, 600)

# Set background color (light gray)
Window.clearcolor = get_color_from_hex("#a3a3b3")  # soft grayish-purple

class MicrophoneButton(ButtonBehavior, Image):
    pass

class MainScreen(BoxLayout):
    def _init_(self, **kwargs):
        super(MainScreen, self)._init_(orientation='vertical', **kwargs)

        with self.canvas.before:
            Color(1, 1, 1, 1)  # Set background color to white
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.bind(size=self._update_rect, pos=self._update_rect)

        self.label = Label(
            text='Voice2Vision',
            font_size='28sp',
            bold=True,
            color=(0, 0, 0, 1),  # Black text
            size_hint=(1, 0.2)
        )

        self.mic_icon = Image(
            source='mic_blue.png',
            size_hint=(None, None),
            size=(150, 150),
            allow_stretch=True,
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        self.mic_icon.bind(on_touch_down=self.on_mic_press)

        self.status = Label(
            text='Tap the mic to start',
            font_size='20sp',
            color=(0, 0, 0, 1),  # Black text
            size_hint=(1, 0.2)
        )

        self.add_widget(Widget(size_hint=(1, 0.1)))  # Spacer
        self.add_widget(self.label)
        self.add_widget(self.mic_icon)
        self.add_widget(self.status)
        self.add_widget(Widget(size_hint=(1, 0.1)))  # Spacer

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def on_mic_press(self, *args):
        self.status.text = "Listening... "
        threading.Thread(target=run_voice2vision).start()

class Voice2VisionApp(App):
    def build(self):
        return MainScreen()

if __name__ == '_main_':
    Voice2VisionApp().run()