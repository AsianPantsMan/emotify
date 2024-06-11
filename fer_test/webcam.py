import cv2
import time

# initialize webcam
camera = cv2.VideoCapture(0)
cv2.namedWindow("webcam")
img_counter = 0
frame_counter = 0

# delay for camera to start
time.sleep(1)

# set initial time
start_time = time.time()

while True:
    ret, frame = camera.read()

    if not ret:
        print("Failed to grab frame")
        break

    cv2.imshow("webcam", frame)

    key = cv2.waitKey(1)

    # esc to exit
    if key % 256 == 27:
        break
    elif (int(time.time()) - int(start_time)) % 10 == 0:
        # capture 5 images
        while frame_counter < 5:
            # images saved to webcam_images
            img_name = f"webcam_images/opencv_frame{img_counter}.png"
            cv2.imwrite(img_name, frame)
            print(f"{img_name[14:]} written!")

            img_counter += 1
            frame_counter += 1

        # reset frame_counter and start_time for next 5 images
        start_time = time.time()
        frame_counter = 0

cv2.destroyAllWindows()
camera.release()
