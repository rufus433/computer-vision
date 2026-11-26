import cv2
import os
image_path = "sample1.jpeg"
if not os.path.exists("C:\Users\kg736\Downloads\WhatsApp Image 2026-08-25 at 9.52.28 AM (1).jpeg"):
    print("Image not found")
else:
    image = cv2.imread(image_path)
    if image is None:
        print("Could not read image")
    else:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Original Image", image)
        cv2.imshow("Grayscale Image", gray)
        cv2.waitKey(0)
        cv2.destroyAllWindows()