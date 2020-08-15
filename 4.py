from kivymd.app import MDApp
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.lang.builder import Builder
import cv2
from intro_cv import *




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
        size_hint:1,None

        MDRectangleFlatButton:
            text: "Cam 1 start"
            size_hint: 0.1,None
            on_press: root.ids.cam1.start()

    
        MDRectangleFlatButton:
            text: "Cam 2 start"
            size_hint: 0.1,None
            on_press: root.ids.cam2.start()

    
        MDRectangleFlatButton:
            text: "Cam 3 start"
            size_hint: 0.1,None
            on_press: root.ids.cam3.start()

    
        MDRectangleFlatButton:
            text: "Cam 1 stop"
            size_hint: 0.1,None
            on_press: root.ids.cam1.stop()

    
        MDRectangleFlatButton:
            text: "Cam 2 stop"
            size_hint: 0.1,None
            on_press: root.ids.cam2.stop()
    
        MDRectangleFlatButton:
            text: "Cam 3 stop"
            size_hint: 0.1,None
            on_press: app.button()
'''

class KivyCamera(Image):
    def __init__(self, capture = None, fps=30, **kwargs):
        super(KivyCamera, self).__init__(**kwargs)
        self.capture = capture
        self.fps = fps
        self.test = get_frame("fold1", 200)
        
    
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

class CamApp(MDApp):
    def build(self):
        self.capture = None
        return Builder.load_string(kv)
    
    def button(self):
        test = get_frame("fold1", 200)
        ret, frame = next(test)
        print(frame)
    
    def on_stop(self):
        self.capture.release()

if __name__ == "__main__":
    CamApp().run()