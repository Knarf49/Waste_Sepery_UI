from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.videoplayer import VideoPlayer
from kivy.clock import Clock
from kivymd.app import MDApp
from kivy.core.text import LabelBase
from kivymd.icon_definitions import md_icons
from kivy.uix.camera import Camera


#button
from kivymd.uix.button import MDFloatingActionButton,MDFlatButton

#cooper
LabelBase.register(name='Cooper-B', fn_regular='fonts/cooper/CooperHewitt-Bold.otf')
LabelBase.register(name='Cooper-M', fn_regular='fonts/cooper/CooperHewitt-Medium.otf')

#prompt
LabelBase.register(name='prompt-R', fn_regular='fonts/Prompt/Prompt-Regular.ttf')
LabelBase.register(name='prompt-B', fn_regular='fonts/Prompt/Prompt-Bold.ttf')
LabelBase.register(name='prompt-Semi', fn_regular='fonts/Prompt/Prompt-SemiBold.ttf')


# Load the KV files
Builder.load_file("home.kv")
Builder.load_file("page2.kv")
Builder.load_file("result.kv")

class HomeScreen(Screen):
    pass


#TODO: แก้บัค vdo in carousel ด้วยการใช้ vdo player
class Page2Screen(Screen):
    def on_enter(self):
        # Start spinner on entering the screen
        self.ids.loading_spinner.active = True
        Clock.schedule_once(self.show_button, 1)  # Schedule the button to appear after 2 seconds

    def show_button(self, dt):
        # Stop the spinner and show the button
        self.ids.loading_spinner.active = False
        self.ids.loading_spinner.opacity = 0
        self.ids.delayed_button.opacity = 1
        self.ids.delayed_button.disabled = False


class ResultScreen(Screen):
    pass

class MyScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Add screens to the ScreenManager
        self.add_widget(HomeScreen(name="home"))
        self.add_widget(Page2Screen(name="page2"))
        self.add_widget(ResultScreen(name="result"))

class MyApp(MDApp):
    def build(self):
        return MyScreenManager()

if __name__ == "__main__":
    MyApp().run()
