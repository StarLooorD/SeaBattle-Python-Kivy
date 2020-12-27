import atexit

import kivy
from kivy.app import App
from kivy.config import Config
from kivy.core.text import LabelBase
from kivy.lang import Builder
from kivy.core.audio import SoundLoader
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager

import app.screen
from app.screen.highscores import Highscores
from app.screen.level import Level

kivy.require('1.9.1')
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

LabelBase.register(name="Bright Young Things",
                   fn_regular="assets/fonts/bright_young_things/Bright Young Things.ttf",
                   fn_bold="assets/fonts/bright_young_things/Bright Young Things.ttf",
                   fn_italic="assets/fonts/bright_young_things/Bright Young Things.ttf",
                   fn_bolditalic="assets/fonts/bright_young_things/Bright Young Things.ttf")

LabelBase.register(name="Old",
                   fn_regular="assets/fonts/old/OLDSH___.TTF",
                   fn_bold="assets/fonts/old/OLDSSCH_.TTF",
                   fn_italic="assets/fonts/old/OLDSIH__.TTF",
                   fn_bolditalic="assets/fonts/old/OLDSSCH_.TTF")


class ScreenManagement(ScreenManager):
    pass


class ShipyApp(App):
    screen_manager = ObjectProperty(None)
    game = None
    highscores = None

    def __init__(self, **kwargs):
        super(ShipyApp, self).__init__(**kwargs)
        self.screen_manager = Builder.load_file('app/screen/kv/screenmanager.kv')
        self.sound = SoundLoader.load('soundfile/main_theme.mp3')
        self.highscores = Highscores()
        self.level = Level()
        atexit.register(self.highscores.write_to_file)

    def build(self):
        self.sound.play()
        return self.screen_manager


if __name__ == "__main__":
    app_instance = ShipyApp()
    app_instance.run()
