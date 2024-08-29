import cv2
file_name = r"C:\VANSHIKA\UNIVERSITY\COURSES\YEAR 3\EDGE AI\FACE_DETECTOR_APP\plant.jpg"

src = cv2.imread(file_name, 1)
src1 = 255 - src #negative image, used when backgound is white
tmp = cv2.cvtColor(src1, cv2.COLOR_BGR2GRAY)
#we can threshold a colored image too but we need to threshold all the three channels separately and then merge them
_ ,alpha = cv2.threshold(tmp, 50, 255, cv2.THRESH_BINARY)# threshold is 50
#using split to split channels
#split into 3 2D matrices
b, g, r = cv2.split(src1)

#add the alpha channel
rgba = [b, g, r, alpha]
dst = cv2.merge(rgba, 4)

cv2.imwrite("plant.png", dst)



