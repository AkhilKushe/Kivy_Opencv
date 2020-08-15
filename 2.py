from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout
import time

Builder.load_string(
'''
<CameraClick>:
    orientation: 'vertical'
    Camera:
        id:camera
        resolution: (640, 480)
        play: False

    MDRectangleFlatButton:
        text: "Play"
        on_press: camera.play = not camera.play
        size_hint_y: None
        height: '48dp'
    
    MDRectangleFlatButton:
        text: 'Capture'
        size_hint_y: None
        height: '48dp'
        on_press: root.capture()

'''
)

class CameraClick(BoxLayout):
    def capture(self):
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("IMG_{}.png".format(timestr))
        print("Captured")

class TestCamera(MDApp):
    def build(self):
        return CameraClick()

TestCamera().run()