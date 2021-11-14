import datetime

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager

import json

Builder.load_file('design4.kv')
users = json.load(open('user.json'))

print(users)


class MainApp(App):
    def build(self):
        return RootWidget()


class RootWidget(ScreenManager):
    pass


class LoginScreen(Screen):
    def sign_up(self):
        print("Sign Up Button Clicked --> Navigating to Signup Screen")
        self.manager.current = 'signup'


class SignUpScreen(Screen):
    def sign_up_handler(self, uname, wpass):
        print("Signing Up User with details : ", uname, wpass)
        users[uname] = {
            "username": uname,
            "password": wpass,
            "created": datetime.datetime.now().__format__('%Y-%m-%d %H:%M:%S')
        }

        print(users)
        json.dump(users, open('user.json', 'w'))


MainApp().run()
