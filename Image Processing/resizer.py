import cv2
import glob

images = glob.glob("*.jpg")

resolution_height = int(input("Type the height: "))
resolution_width = int(input("Type the width: "))

for image in images:
    img = cv2.imread(image, 0)
    resize = cv2.resize(img, (resolution_height, resolution_width))
    print("Resizing...")
    cv2.imshow("Resizer", resize)
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    cv2.imwrite("Resized_"+image, resize)
    print("Resized!")