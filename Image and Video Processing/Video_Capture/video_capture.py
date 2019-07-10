import cv2
import time


video = cv2.VideoCapture(0)

num_frames = 0

while True:
    check, frame = video.read()

    print(check)
    print(frame)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Frame", gray)

    key = cv2.waitKey(1)
    num_frames += 1

    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
print(num_frames)
