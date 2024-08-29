# 1. create a snapchat like  filter 
# 2. track the face
# 3. create a magic eraser(erases extra faces, mostly small faces in pictures)

import cv2


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

while True:
    # Read the frame
    # ret, frame = cap.read()
    # if not ret:
    #     break
    _, frame = cap.read()
    
    # Convert the color frame to a grayscale frame
    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    detections = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=6)

    for face in detections:
        x, y, w, h = face
        k=cv2.imread(r'C:\VANSHIKA\UNIVERSITY\COURSES\YEAR 3\EDGE AI\FACE_DETECTOR_APP\apple.png')
        kk=cv2.imread(r'C:\VANSHIKA\UNIVERSITY\COURSES\YEAR 3\EDGE AI\FACE_DETECTOR_APP\apple.png',cv2.IMREAD_UNCHANGED)

        # Resize the images
        k1 = cv2.resize(k, (w // 4, h // 4))
        kk1 = cv2.resize(kk, (w // 4, h // 4))

        # Calculate the top-left corner to center the image on the face
        center_x = x + (w // 2) - (w // 8)
        center_y = y + (h // 2) - (h // 8)
        
        k1[:,:,0]=cv2.bitwise_and(k1[:,:,0],kk1[:,:,3])
        k1[:,:,1]=cv2.bitwise_and(k1[:,:,1],kk1[:,:,3])
        k1[:,:,2]=cv2.bitwise_and(k1[:,:,2],kk1[:,:,3])
        
        fa=frame[center_y:center_y + h // 4,center_x:center_x + w // 4, :]
        k1m=cv2.bitwise_or(k1,fa)
        
        # Choose the image based on the y-coordinate of the face
        if y > 100:
            frame[center_y:center_y + h // 4, center_x:center_x + w // 4] = k1m

    # Display the frame with the overlaid images
    cv2.imshow("Frame", frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()