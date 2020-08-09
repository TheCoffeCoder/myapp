from kivymd.app import MDApp
from screen1 import Boxlay, Card, Navi, Card_popup
from kivymd.uix.button import MDFlatButton
from order import Add_chart
from review import Review
from kivymd.uix.label import MDLabel


class MainApp(MDApp):

    def build(self):
        self.bo = Navi()
        self.nv = self.bo.ids.nav_drawer
        self.manager =self.bo.ids.manager
        return self.bo
    def open_popup(self,*args):
        self.card_pop = Card_popup()
        self.card_pop.open()

    def close_popup(self,*args):
        self.card_pop.dismiss()

    def add_chart(self,*args):
        self.addchart = Add_chart()
        self.bo.ids.kitchen_box.add_widget(self.addchart)


MainApp().run()