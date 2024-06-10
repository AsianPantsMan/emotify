import cv2
import time

camera = cv2.VideoCapture(0)
cv2.namedWindow("webcam")
img_counter = 0
# Set the initial time
start_time = time.time()

while True:
    ret, frame = camera.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("webcam", frame)

    key = cv2.waitKey(1)
    if key%256 == 27:
        break
    #spacebar for ss
    elif key%256 == 32 or (int(time.time()) - int(start_time)) % 10 == 0:
        img_name = f"opencv_frame{img_counter}.png"
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

cv2.destroyAllWindows()
camera.release()
