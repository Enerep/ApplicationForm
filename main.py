from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.properties import ObjectProperty
import os


class WindowManager(ScreenManager):
    pass


class StartWindow(Screen):
    pass


class EndProject(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.message = Label(halign="center", valign="middle", font_size=100)
        self.message.text_size = (self.message.width * 0.9, None)
        if os.path.isfile("submitbutton.txt"):
            with open("submitbutton.txt", "r") as f:
                splt = f.read().split(",")
                nameend = splt[0]
                lastend = splt[1]
                emailend = splt[2]
                self.message = Label(text=f"Hello {nameend} {lastend}!, Your email is currently: {emailend}")
                self.add_widget(self.message)
        else:
            self.message = Label(text="Please Re-Run the code!(Don't press Submit again when you already submitted)")
            self.add_widget(self.message)


class Page(GridLayout, Screen):
    def __init__(self, **kwargs):
        super(Page, self).__init__(**kwargs)
        self.cols = 1

        btn = ObjectProperty(None)

        if os.path.isfile("submitbutton.txt"):
            with open("submitbutton.txt", "r") as f:
                splt = f.read().split(",")
                prev_fname = splt[0]
                prev_lname = splt[1]
                prev_email = splt[2]
        else:
            prev_fname = ""
            prev_lname = ""
            prev_email = ""

        self.inside = GridLayout()
        self.inside.cols = 2
        
        self.inside.add_widget(Label(text="First Name: "))
        self.fname = TextInput(multiline=False, text=prev_fname)
        self.inside.add_widget(self.fname)

        self.inside.add_widget(Label(text="Last Name: "))
        self.lname = TextInput(multiline=False, text=prev_lname)
        self.inside.add_widget(self.lname)

        self.inside.add_widget(Label(text="Email: "))
        self.email = TextInput(multiline=False, text=prev_email)
        self.inside.add_widget(self.email)

        self.add_widget(self.inside)

        self.submit = Button(text="Submit", font_size=40)
        self.submit.bind(on_press=self.submitbutton)
        self.add_widget(self.submit)

    def submitbutton(self, instance):
        name = self.fname.text
        lastname = self.lname.text
        email = self.email.text

        with open("submitbutton.txt", "w") as f:
            f.write(f"{name},{lastname},{email}")


kv = Builder.load_file("my.kv")


class MyApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    MyApp().run()
