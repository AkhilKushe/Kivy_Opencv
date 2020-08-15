#Simple camera app which which can capture pictures from your webcam 
#and display and store it in the current directory

from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout
import time
import os
os.chdir(os.path.dirname(__file__))

Builder.load_string(
'''
<CameraClick>:
    orientation: 'vertical'
    Camera:
        id:camera
        resolution: (640, 480)
        play: False

    Button:
        text: "Play"
        on_press:
            camera.play = not camera.play
            self.text = 'pause' if camera.play else 'play'
        size_hint_y: None
        height: '48dp'
    
    Button:
        text: 'Capture'
        size_hint_y: None
        height: '48dp'
        on_press:root.capture()

'''
)

class CameraClick(BoxLayout):
    def capture(self):
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("IMG_{}.png".format(timestr))
        print("Captured")

class TestCamera(App):
    def build(self):
        return CameraClick()

if __name__ == "__main__":
    TestCamera().run()