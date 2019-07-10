import cv2

img = cv2.imread("galaxy.jpg", 0)

print(img)
print(img.shape)

#resizing of the image itself
resized_image=cv2.resize(img,(int(img.shape[1]/3), int(img.shape[0]/3)))

cv2.imshow("Galaxy", resized_image)
#Writing resized image into a new file
cv2.imwrite("Galaxy_resized.jpg", resized_image)
#How the user detroys the window
cv2.waitKey(0)
#What happens when you close the window
cv2.destroyAllWindows()

