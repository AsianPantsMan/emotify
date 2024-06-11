import cv2
import time

# initialize
camera = cv2.VideoCapture(0)
cv2.namedWindow("webcam")
img_counter = 0
frame_counter = 0
capture = True

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
        if capture:
            while frame_counter < 5:
                # images saved to fer_test/webcam_images
                img_name = f"fer_test/webcam_images/opencv_frame{
                    img_counter}.png"
                cv2.imwrite(img_name, frame)
                print(f"{img_name[23:]} written!")

                img_counter += 1
                frame_counter += 1

            # reset for next 5 images
            capture = False
            start_time = time.time()
            frame_counter = 0
    else:
        capture = True

cv2.destroyAllWindows()
camera.release()
