from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

Window.clearcolor = (42 / 256, 54 / 256, 59 / 256, 1)

Builder.load_string('''



<MyOwnLabel@Label>
    color: (255/256, 132/256, 124/256)
    font_size: '25sp'
    haling: 'left'
    yaling: 'middle'
    text_size: self.size
    font_name: "Comic"

<Container>:
    color: (42/256, 54/256, 59/256, 1)
    rows: 3
    text_input: text_input
    text_week: text_week
    text_hour: text_hour
    text_min: text_min
    text_sec: text_sec
    text_msec: text_msec

    AnchorLayout:
        anchor_y: 'top'
        size_hint: 1, 0.4
        padding: 30

        TextInput:
            text: ''
            id: text_input
            font_size: '45sp'
            input_filter: 'int'
            inpit_type: 'number'
            multiline: False
            font_name: "Comic"
            hint_text: "Введите количество дней"

    GridLayout:
        cols: 2
        padding: [40,-50,0,0]

        BoxLayout:
            orientation: 'vertical'

            MyOwnLabel:
                text: 'Недели'

            MyOwnLabel:
                text: 'Часы'

            MyOwnLabel:
                text: 'Минуты'

            MyOwnLabel:
                text: 'Секунды'

            MyOwnLabel:
                text: 'Милисекунды'

        BoxLayout:
            orientation: 'vertical'
            size_hint: 0.5, 1

            MyOwnLabel:
                text: '0'
                color: (254/256, 206/256, 168/256)
                id: text_week

            MyOwnLabel:
                text: '0'
                color: (254/256, 206/256, 168/256)
                id: text_hour

            MyOwnLabel:
                text: '0'
                color: (254/256, 206/256, 168/256)
                id: text_min

            MyOwnLabel:
                text: '0'
                color: (254/256, 206/256, 168/256)
                id: text_sec

            MyOwnLabel:
                text: '0'
                color: (254/256, 206/256, 168/256)
                id: text_msec

    BoxLayout:
        size_hint: 0.9, 0.3
        padding: [30,20,30,20]

        Button:
            background_color: ((153/256, 184/256, 152/256,1))
            background_normal: ''
            font_name: "Comic"
            text: 'Начать сложный расчёт'
            size_hint: 1, 0.9
            font_size: '25sp'
            on_press:
                self.text = '*машинные звуки думония'
            on_release:
                self.text = 'Начать сложный расчёт'
                root.convert()

''')


class Container(GridLayout):
    def convert(self):
        try:
            number = int(self.text_input.text)
        except Exception:
            number = 0

        self.text_hour.text = str(number * 24)
        self.text_min.text = str(number * 1440)
        self.text_sec.text = str(number * 86400)
        self.text_msec.text = str(number * 864000000)
        self.text_week.text = str("%.2f" % round(number / 7, 2))


class DuckyApp(App):
    pass

    def build(self):
        return Container()


if __name__ == "__main__":
    DuckyApp().run()