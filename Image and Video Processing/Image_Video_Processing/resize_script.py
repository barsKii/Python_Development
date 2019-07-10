import cv2
import glob

# Glob gets all the files with the same suffix into the images variable
images = glob.glob("*.jpg")

# Loops through the images in the variable
for image in images:
    # Load
    img = cv2.imread(image, 1)
    # Resize
    resized = cv2.resize(img, (100, 100))
    # Display and Destroy
    cv2.imshow("Hey", resized)
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    # Write to file
    cv2.imwrite("resized_"+image, resized)