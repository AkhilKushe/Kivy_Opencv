#This program demonstrates how to get display video from image frames
# stored on your device. This can be integrated with a remote video source
# which sents frames to the sever, to act as a surveilance monitor.

from kivy.app import App
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.lang.builder import Builder
import cv2
import utils

fold = "fold1"     #name of the folder with image frames(should be in the current dir)

kv ='''

BoxLayout:
    orientation:"vertical"

    GridLayout:
        cols:3

        KivyCamera:
            id: cam1
            size_hint: 0.33,0.33
    
        KivyCamera:
            id: cam2
            size_hint: 0.33,0.33
   
        KivyCamera:
            id: cam3
            size_hint: 0.33, 0.33

    
    GridLayout:
        cols:3

        Button:
            text: "Cam 1 start"
            size_hint: 0.1,None
            on_press: root.ids.cam1.start()

    
        Button:
            text: "Cam 2 start"
            size_hint: 0.1,None
            on_press: root.ids.cam2.start()

    
        Button:
            text: "Cam 3 start"
            size_hint: 0.1,None
            on_press: root.ids.cam3.start()

    
        Button:
            text: "Cam 1 stop"
            size_hint: 0.1,None
            on_press: root.ids.cam1.stop()

    
        Button:
            text: "Cam 2 stop"
            size_hint: 0.1,None
            on_press: root.ids.cam2.stop()
    
        Button:
            text: "Cam 3 stop"
            size_hint: 0.1,None
            on_press: root.ids.cam3.stop()
'''

class KivyCamera(Image):
    def __init__(self, fps=30, **kwargs):
        super(KivyCamera, self).__init__(**kwargs)
        self.fps = fps
        self.test = utils.get_frame("fold1", 200)
        
    
    def start(self):
        Clock.schedule_interval(self.update, 1.0/self.fps)
    
    def stop(self):
        Clock.unschedule(self.update)

    def update(self, dt):
        try:
            ret, frame = self.test.__next__()
        except:
            ret = False
            self.stop()

        if ret:
            buf1 = cv2.flip(frame, 0)
            buf = buf1.tostring()
            image_texture =Texture.create(
                size = (640, 480), colorfmt='bgr'
            )
            image_texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')

            self.texture = image_texture

class CamApp(App):
    def build(self):
        return Builder.load_string(kv)
    
    

if __name__ == "__main__":
    CamApp().run()