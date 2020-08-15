#Simple program to show how to integrate webcam into kivy textures
#You can set the video sourse as any external device by changing the parameters of VideoCapture
#function.
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.lang.builder import Builder
import cv2



kv ='''

BoxLayout:
    orientation: 'vertical'

    KivyCamera:
        id: cam
        size_hint: 0.5,0.5
        pos_hint: {"x":0.1,"top":1}
    
    KivyCamera:
        id: cam
        size_hint: 0.5,0.5
        pos_hint: {"x":0.1,"top":1}
    
    KivyCamera:
        id: cam
        size_hint: 0.5,0.5
        pos_hint: {"x":0.1,"top":1}
    
    KivyCamera:
        id: cam
        size_hint: 0.5,0.5
        pos_hint: {"x":0.1,"top":1}
        
    MDRectangleFlatButton:
        text: "Nothing"
        on_press: app.button()
'''

class KivyCamera(Image):
    def __init__(self, capture = cv2.VideoCapture(0), fps=30, **kwargs):
        super(KivyCamera, self).__init__(**kwargs)
        self.capture = capture
        Clock.schedule_interval(self.update, 1.0/fps)

    def update(self, dt):
        ret, frame = self.capture.read()
        if ret:
            buf1 = cv2.flip(frame, 0)
            buf = buf1.tostring()
            image_texture =Texture.create(
                size = (frame.shape[1], frame.shape[0]), colorfmt='bgr'
            )
            image_texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')

            self.texture = image_texture

class CamApp(MDApp):
    def build(self):
        self.capture = cv2.VideoCapture(0)
        return Builder.load_string(kv)
    
    def button(self):
        print(self.root.ids)
    
    def on_stop(self):
        self.capture.release()

if __name__ == "__main__":
    CamApp().run()