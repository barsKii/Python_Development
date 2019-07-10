import cv2
import glob

# Glob gets all the files with the same suffix into the images variable
images = glob.glob("*.jpg")

# Loops through the images in the variable
for image in images:
    # Load
    img = cv2.imread(image, 0)
    # Display and Destroy
    cv2.imshow("Hey", img)
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    # Write to file
    cv2.imwrite("greyscale_"+image, img)