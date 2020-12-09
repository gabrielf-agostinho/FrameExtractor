import cv2
import os

def extract(file):
    path = os.getcwd() + r"\frames\\"
    os.mkdir(path)
    capture = cv2.VideoCapture(file)
    i = 1

    while(capture.isOpened()):
        ret, frame = capture.read()
        if ret == False:
            print("Extraction complete!")
            break
        print("Extracting frame" + str(i))
        cv2.imwrite(path + "Frame" + str(i) + ".png", frame)
        i += 1

    capture.release()
    cv2.destroyAllWindows()
    
file = input(r"Please enter the path of the video (Example: C:\Users\user\Videos\video.mp4): ")
extract(file)