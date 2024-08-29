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

    maxa = 0
    ind = 0
    acc = [None] * len(detections)
    lind = 0
    for face in detections:
        x, y, w, h = face
        if w * h > maxa: #if w*h > 500
            maxa = w * h
            acc[lind] = False
            acc[ind] = True
            lind = ind
        else:
            acc[ind] = False
        ind += 1
    ind = 0
    for face in detections:
        x, y, w, h = face
        if not acc[ind]:
            k = frame[y:y+h, x:x+w, :]
            k = cv2.blur(k, (15,15))
            # frame[y:y+h, x:x+w, :] = 0  # black
            frame[y:y+h, x:x+w, :] = k  # blur
        ind += 1

        frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 3)    
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()