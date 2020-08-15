import cv2
import concurrent.futures
from io import BytesIO
import numpy as np
import time
import os

print(os.getcwd())
# show video from webcam in normal color
def show_vid():
    vid = cv2.VideoCapture(0)
    while True:
        ret, frame = vid.read()
        cv2.imshow("image", frame)
        k = cv2.waitKey(1)
        if k == ord('q'):
            vid.release()
            break

    cv2.destroyAllWindows()


#show image(bytearray) from given path 
def show_image(img_path):
    with open(img_path, "rb") as f:
        img = f.read()

    pro_img = BytesIO(img)
    np_img = np.asarray(bytearray(img), np.uint8)
    final_img = cv2.imdecode(np_img, 0)
    print(final_img)
    final_img = cv2.flip(final_img, 0)
    final_img = cv2.resize(final_img,(680,420), interpolation=cv2.INTER_AREA)
    cv2.imshow("img", final_img)
    cv2.waitKey(0)


#save webcam video as frames(image) in a folder as grayscale
def save_frames(folder_name, num_frames):
    vid = cv2.VideoCapture(0)
    for i in range(num_frames):
        ret, frame = vid.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        file_name = f"{folder_name}/img_{i}.png"
        cv2.imwrite(file_name, frame, )
        time.sleep(0.001)


#show frames stored in a folder
def show_frames(folder_name, num_frames):
    for i in range(num_frames):
        img = cv2.imread(f"Kivy and OpenCv/{folder_name}/img_{i}.png", 0)
        cv2.imshow("image", img)
        cv2.waitKey(10)


#save video from frames(images) as grayscale only
def save_video(folder_name, num_frames, file_name, fps):
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    writer = cv2.VideoWriter(file_name, fourcc, fps, (680,420)) #res same as shape of mat
    for i in range(num_frames):
        img = cv2.imread(f"{folder_name}/img_{i}.png", 1)  #needs to be a three channel mat
        img = cv2.resize(img,(680, 420), interpolation=cv2.INTER_AREA)
        
        #force grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img[:,:,0] = gray
        img[:,:,1] = gray
        img[:,:,2] = gray

        writer.write(img)
    writer.release()


#record live stream from webcam as grayscale
def live_record(file_name, fps):
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    writer = cv2.VideoWriter(file_name, fourcc, fps, (640, 480))
    cap = cv2.VideoCapture(0)
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            np.reshape(frame, (640, 480, 3))

            # make 3 channel grayscale
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frame[:,:,0] = gray
            frame[:,:,1] = gray
            frame[:,:,2] = gray

            writer.write(frame)
            cv2.imshow("img", frame)

            if cv2.waitKey(1) == ord("q"):
                break
        else:
            break

def get_frame(fold_name, frames):
    for i in range(frames):
        img = cv2.imread(f"Kivy and OpenCv/{fold_name}/img_{i}.png", 1)
        
        #force grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img[:,:,0] = gray
        img[:,:,1] = gray
        img[:,:,2] = gray

        yield (True, img)



#multiple processes of live_record or show_video wont work as the webcam will be busy in one process

# if __name__ == "__main__":
    
#     with concurrent.futures.ProcessPoolExecutor() as executor:
#         f2 = executor.submit(show_image)
#         f1 = executor.submit(show_vid)


# if __name__ == "__main__":
#     with concurrent.futures.ProcessPoolExecutor() as executor:
#         f1 = executor.submit(show_frames, "./fold1", 200)
#         f2 = executor.submit(show_frames, "./fold2", 200)


# if __name__ == "__main__":
#     with concurrent.futures.ProcessPoolExecutor() as executor:
#         f1 = executor.submit(save_video, "./fold1", 200)
#         f2 = executor.submit(save_video, "./fold2", 200)
#         f3 = executor.submit(show_frames, "./fold1", 200)
