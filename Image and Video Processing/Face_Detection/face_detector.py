# Search haarcascades if you want to get other cascades for recognitions such as body, eye, or car faces

import cv2

# Imports the cascade to read the face
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Download as a colour image
img = cv2.imread("news.jpg")
# Creates a greyscale version of that image
grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(grey_img,
                                      scaleFactor=1.1,
                                      minNeighbors=5)

print(faces)

for x, y, w, h in faces:
    img = cv2.rectangle(img, (x, y), ((x+w), (y+h)), (0, 255, 0), 3)

#resized_img = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))

cv2.imshow("Grey", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


