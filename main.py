from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.properties import StringProperty
import datetime
from datetime import date
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.core.window import Window
from kivy.resources import resource_find
from kivymd.uix.label import MDLabel

Window.size = (350, 600)


class ToDoCard(FakeRectangularElevationBehavior, MDFloatLayout):
    pass

class ToDoApp(MDApp):

    def build(self):
        global screen_manager
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file('Main.kv'))
        screen_manager.get_screen('main').my_task.font_name = 'Poppins-SemiBold.ttf'
        screen_manager.get_screen('main').date.font_name = 'Poppins-Regular.ttf'

        return screen_manager
    def on_start(self):
        today = date.today()
        wd = date.weekday(today)
        days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
        year = str(datetime.datetime.now().year)
        month = str(datetime.datetime.now().strftime('%b'))
        day = str(datetime.datetime.now().strftime('%d'))
        screen_manager.get_screen('main').date.text = f'{days[wd]}, {day} {month} {year}'
        
        #screen_manager.get_screen('main').todo_list.add_widget(ToDoCard())
    def add_todo(self):
        screen_manager.get_screen('main').todo_list.add_widget(ToDoCard())

if __name__ == '__main__':
    ToDoApp().run()
