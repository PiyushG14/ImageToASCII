import cv2

# ascii characters used to build the output text
#Use more chars for more accurate representation of brightness
ASCII_CHARS =  ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

try:
    image = Image.open("test_img.jpg")
except:
    print(path, " is not a valid pathname to an image.")

img = cv2.imread("test_img.jpg", 0)
img = cv2.resize(img, (32,32)) 
width, height = img.shape
for i in range(0, width):
    for j in range(0, height):
        print(ASCII_CHARS[img[i][j]//25], end = "")
    print("")