import datetime
import glob
import random

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from pathlib import Path
from hoverable import HoverBehavior
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image

import json

Builder.load_file('design.kv')
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
        self.manager.transition.direction = 'left'
        self.manager.current = 'signup'

    def login_handler(self):
        uname = self.ids.username.text
        upass = self.ids.password.text
        print("Handling Login User with details :: ", uname, upass)
        if uname in users and users[uname]['password'] == upass:
            self.manager.transition.direction = 'left'
            self.manager.current = 'home'
        else:
            self.ids.errorMsg.text = "Incorrect Combination !!"


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
        self.manager.current = 'signup_success'

    def back(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'login'


class SignUpSuccess(Screen):
    def login(self):
        print("Redirecting to Login")
        self.manager.current = 'login'


class HomeScreen(Screen):
    def logout(self):
        print("Logging Out")
        self.manager.transition.direction = 'right'
        self.manager.current = 'login'

    def show_quote(self):
        print("Showing Quote")
        feeling = self.ids.feeling.text.strip().lower()
        print("Feeling ::: ", feeling)
        available_feelings = glob.glob("./quotes/*txt")
        print(available_feelings)
        available_feelings = [Path(feeling).stem for feeling in available_feelings]
        print(available_feelings)

        if feeling in available_feelings:
            with open(f"./quotes/{feeling}.txt") as file:
                data = file.readlines()
                print("Random number", random.randint(0, len(data)))
                quote = data[random.randint(0, len(data) - 1)]
                print(quote)
                # or quote = random.choice(data)
                self.ids.quote.text = quote

        else:
            print("Please try something else")
            self.ids.quote.text = "Please try something else"


class CustomImageButton(ButtonBehavior, HoverBehavior, Image):
    pass


if __name__ == '__main__':
    MainApp().run()
