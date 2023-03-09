from kivymd.app import MDApp
from kivy.lang import Builder

KV = '''
Screen:

    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'My App'
            left_action_items: [["menu", lambda x: print('Menu button')]]
            right_action_items: [["clock", lambda x: print('Clock button')], ["dots-vertical", lambda x: print('Vertical dots button')]]
            elevation: 10

        MDLabel:
            text: 'Hello, World!'
            halign: 'center'
'''

class MyApp(MDApp):

    def build(self):
        return Builder.load_string(KV)

if __name__ == '__main__':
    MyApp().run()