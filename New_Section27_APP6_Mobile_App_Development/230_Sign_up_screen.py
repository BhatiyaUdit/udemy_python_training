from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager

Builder.load_file('design2.kv')


class LoginScreen(Screen):
    def on_pre_enter(self):
        super().on_pre_enter()
        print("Before Entering the Screen")

    def sign_up(self):
        print("Sign Up Clicked")
        print(self.manager.__dict__)
        print(self.manager.current)
        self.manager.current = 'signup'


class SignUpScreen(Screen):
    def back(self):
        self.manager.current = 'login'


class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


MainApp().run()
