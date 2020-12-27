from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen

Builder.load_file('app/screen/kv/level.kv')


def level_init():
    difficulties = App.get_running_app().level
    screen = App.get_running_app().screen_manager.get_screen('level')


class LevelScreen(Screen):
    score_list = ObjectProperty(None)
    iterator = 0


class Level:

    def __init__(self):
        pass
