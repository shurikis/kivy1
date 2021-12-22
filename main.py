from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label

from kivy.uix.gridlayout import GridLayout

# from kivy.config import Config
# Config.set('graphics', 'width', 400)
# Config.set('graphics', 'height', 500)


class CalculatorApp(App):
    def __init__(self):
        super(CalculatorApp, self).__init__()
        self.lbl = Label(text="0", font_size=40, size_hint=(1, .40), halign="right", valign="center", text_size=(400-50, 500*.4))
        self.formula = "0"

    def build(self):
        ml = GridLayout(rows=1000, padding=25)
        gl = GridLayout(cols=4, spacing=3, size_hint=(1, .60))
        ml.add_widget(self.lbl)
        gl.add_widget(Button(text='7', on_press=self.add_number))
        gl.add_widget(Button(text='8', on_press=self.add_number))
        gl.add_widget(Button(text='9', on_press=self.add_number))
        gl.add_widget(Button(text='X', on_press=self.add_operation))

        gl.add_widget(Button(text='4', on_press=self.add_number))
        gl.add_widget(Button(text='5', on_press=self.add_number))
        gl.add_widget(Button(text='6', on_press=self.add_number))
        gl.add_widget(Button(text='-', on_press=self.add_operation))

        gl.add_widget(Button(text='1', on_press=self.add_number))
        gl.add_widget(Button(text='2', on_press=self.add_number))
        gl.add_widget(Button(text='3', on_press=self.add_number))
        gl.add_widget(Button(text='+', on_press=self.add_operation))

        gl.add_widget(Button(text='+/-'))
        gl.add_widget(Button(text='0', on_press=self.add_number))
        gl.add_widget(Button(text='.', on_press=self.add_operation))
        gl.add_widget(Button(text='=', on_press=self.add_operation))

        ml.add_widget(gl)
        return ml

    def add_number(self, instance):
        if self.formula == "0":
            self.formula = ''
        self.formula += str(instance.text)
        self.lbl.text = self.formula

    def add_operation(self, instance):
        if str(instance.text.lower()) == 'x':
            self.formula += '*'
        else:
            self.formula += str(instance.text)
        self.lbl.text = self.formula


if __name__ == '__main__':
    CalculatorApp().run()
