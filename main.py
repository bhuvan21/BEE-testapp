import kivy
kivy.require('1.10.1')

from kivy.app import App
from kivy.lang import Builder
from kivy.config import Config
from kivy.uix.screenmanager import Screen, ScreenManager

from helperbee import helper

APP_NAME = "BEE-testapp"


Builder.load_file(helper.get_app_path() + APP_NAME + "/testapp.kv")
Config.set('graphics', 'width', '480')
Config.set('graphics', 'height', '800')

class MainScreen(Screen):
    pass

controller = ScreenManager()
controller.add_widget(MainScreen(name="Main"))

def get_app():
    return controller

def get_icon():
    return "testicon.png"
