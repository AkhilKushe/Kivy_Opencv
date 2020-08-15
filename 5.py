import requests
import numpy as np
import cv2 

fourcc = cv2.VideoWriter_fourcc(*"XVID")
writer = cv2.VideoWriter("1.avi", fourcc, 20, (680,420)) #res same as shape of mat

def save_video(file_name, frame, fps):
    img = frame  #needs to be a three channel mat
    img = cv2.resize(img,(680, 420), interpolation=cv2.INTER_AREA)
        
        #force grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img[:,:,0] = gray
    img[:,:,1] = gray
    img[:,:,2] = gray

    writer.write(img)
    

url = "http://192.168.43.1:667/shot.jpg"

while True:
    r = requests.get(url)
    print(r.status_code)
    if r.status_code == 200:
        img = r.content

        np_img = np.asarray(bytearray(img), np.uint8)
            #print(dir(pro_img))
            #print(pro_img.getvalue())

            #print(np_img)
        final_img = cv2.imdecode(np_img, 1)

            #resize the image
        final_img = cv2.resize(final_img,(649,480), interpolation=cv2.INTER_AREA)

            #show the image
        cv2.imshow("img", final_img)
        save_video("1.avi", final_img, 10)
        cv2.waitKey(1)
            
    if r.status_code !=200:
        writer.release()
        break
    
    
writer.release()