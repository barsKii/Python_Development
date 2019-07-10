import cv2
import pandas
from datetime import datetime

first_frame = None
status_list = [None, None]
times = []
df = pandas.DataFrame(columns=["Start", "End"])

video = cv2.VideoCapture(0)

while True:
    check, frame = video.read()
    # Binary of whether there is motion or no motion
    status = 0
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Makes the image blurry so easier to identify the differences
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    if first_frame is None:
        first_frame = gray
        # continue goes back to the beginning of the loop
        continue

    # Delta frame to identify the differences between the two images.
    delta_frame = cv2.absdiff(first_frame, gray)

    # Threshold frame identifies frames above threshold of second condition and changes the pixels to white there
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]

    # Dilates the threshold frame. Reduces the effects of the white spaces in the background
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)

    # Contours. Stores it somehow but I don't exactly follow
    (cnts, _) = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Drawning rectangles around the shapes larger than specified size
    for contour in cnts:
        if cv2.contourArea(contour) < 10000:
            continue
        status = 1
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), ((x + w), (y + h)), (0, 255, 0), 3)

    status_list.append(status)
    if status_list[-1] == 1 and status_list[-2] == 0:
        times.append(datetime.now())
    if status_list[-1] == 0 and status_list[-2] == 1:
        times.append(datetime.now())

    # Displaying of the frames on the screen
    cv2.imshow("Capturing", gray)
    cv2.imshow("Delta Frame", delta_frame)
    cv2.imshow("Threshold Frame", thresh_frame)
    cv2.imshow("Colour Frame", frame)

    key = cv2.waitKey(1)

    if key == ord('q'):
        if status == 1:
            times.append(datetime.now())
        break

print(status_list)
print(times)

# Iterates through the times and adds them to the data frame at the end of the program. Potential loophole of program
# crashing and losing all the code without it saving the motion detections
for i in range(0, len(times), 2):
    df = df.append({"Start": times[i], "End": times[i+1]}, ignore_index=True)

df.to_csv("times.csv")

video.release()
cv2.destroyAllWindows()
