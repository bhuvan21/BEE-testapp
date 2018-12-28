import kivy
kivy.require('1.10.1')

from kivy.app import App
from kivy.lang import Builder
from kivy.config import Config
from kivy.uix.screenmanager import Screen, ScreenManager

import helperbee

APP_NAME = "testapp"


Builder.load_file(helperbee.HelperBEE.get_path() + APP_NAME + "/testapp.kv")
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
