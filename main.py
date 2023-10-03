from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout


class MyApp(App):
    fontsize = '60'
    background = 'cyan'
    color = 'cyan'
    def build(self):
        self.mainLayout = BoxLayout(orientation='vertical')
        self.text = TextInput(multiline = False,font_size = '115')
        self.mainLayout.add_widget(self.text)
        cl1 = BoxLayout()
        btn9 = Button(text='9',font_size=MyApp.fontsize,background_color=MyApp.background,color=MyApp.color, on_press=self.press)
        btn8 = Button(text='8',font_size=MyApp.fontsize,background_color=MyApp.background,color=MyApp.color, on_press=self.press)
        btn7 = Button(text='7',font_size=MyApp.fontsize,background_color=MyApp.background,color=MyApp.color, on_press=self.press)
        btnmult = Button(text='X',font_size=MyApp.fontsize,background_color=MyApp.background,color=MyApp.color, on_press=self.press)

        cl1.add_widget(btn9)
        cl1.add_widget(btn8)
        cl1.add_widget(btn7)
        cl1.add_widget(btnmult)
        cl2 = BoxLayout()
        btn6 = Button(text='6',font_size=MyApp.fontsize,background_color=MyApp.background,color=MyApp.color, on_press=self.press)
        btn5 = Button(text='5',font_size=MyApp.fontsize,background_color=MyApp.background,color=MyApp.color, on_press=self.press)
        btn4 = Button(text='4',font_size=MyApp.fontsize,background_color=MyApp.background,color=MyApp.color, on_press=self.press)
        btndiv = Button(text='/',font_size=MyApp.fontsize,background_color=MyApp.background,color=MyApp.color, on_press=self.press)

        cl2.add_widget(btn6)
        cl2.add_widget(btn5)
        cl2.add_widget(btn4)
        cl2.add_widget(btndiv)
        cl3 = BoxLayout()
        btn3 = Button(text='3',font_size=MyApp.fontsize,background_color=MyApp.background,color=MyApp.color, on_press=self.press)
        btn2 = Button(text='2',font_size=MyApp.fontsize,background_color=MyApp.background,color=MyApp.color, on_press=self.press)
        btn1 = Button(text='1',font_size=MyApp.fontsize,background_color=MyApp.background,color=MyApp.color, on_press=self.press)
        btnsubt = Button(text='-',font_size=MyApp.fontsize,background_color=MyApp.background,color=MyApp.color, on_press=self.press)

        cl3.add_widget(btn3)
        cl3.add_widget(btn2)
        cl3.add_widget(btn1)
        cl3.add_widget(btnsubt)
        cl4 = BoxLayout()
        btndot = Button(text='.',font_size=MyApp.fontsize,background_color=MyApp.background,color=MyApp.color, on_press=self.press)
        btn0 = Button(text='0',font_size=MyApp.fontsize,background_color=MyApp.background,color=MyApp.color, on_press=self.press)
        btnplus = Button(text='+',font_size=MyApp.fontsize,background_color=MyApp.background,color=MyApp.color, on_press=self.press)
        btnequ = Button(text='=',font_size=MyApp.fontsize,background_color=MyApp.background,color=MyApp.color, on_press=self.press)

        cl4.add_widget(btndot)
        cl4.add_widget(btn0)
        cl4.add_widget(btnplus)
        cl4.add_widget(btnequ)

        self.mainLayout.add_widget(cl1)
        self.mainLayout.add_widget(cl2)
        self.mainLayout.add_widget(cl3)
        self.mainLayout.add_widget(cl4)
        return self.mainLayout
    def press(self,event):
        self.text.text = f'{self.text.text}{event.text}'

kv = MyApp()
kv.run()

