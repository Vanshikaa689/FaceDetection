import cv2

# Load the pre-trained Haar Cascade model for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Start video capture (0 is the device index for the default camera)
cap = cv2.VideoCapture(0)
with open("face.txt", "w") as f:
    while True:
        ret, frame = cap.read()  # Corrected: `ret, frame` instead of `,frame`
        if not ret:
            break  # Exit the loop if the frame was not captured successfully

        gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert to grayscale

        # Detect faces in the grayscale image
        detections = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=6)
        #scale factor - increases window size
        #minsize - size of minimum winow
        #max size - size of maximum window
        

        # Draw rectangles around detected faces
        for face in detections:
            x, y, w, h = face
            f.write("(" + str(x+w//2) + "," + str(y+h//2) + ") ")
            frame = cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 3)
        cv2.imshow("Frame", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cv2.imwrite("face.png", frame)
cap.release()
cv2.destroyAllWindows()

frame = cv2.imread("face.png")
with open("face.txt", 'r') as f:
    a = f.readline()
    p = a.strip().split(" ")

for i in range(1, len(p)-1):
    p0 = p[i-1][1:-1].split(",")
    x0 = int(p0[0])
    y0 = int(p0[1])
    p1 = p[i][1:-1].split(",")
    x1 = int(p1[0])
    y1 = int(p1[1])
    cv2.line(frame, (x0, y0), (x1, y1), (0, 255, 0), 2)
cv2.imshow("Frame with Lines", frame)
cv2.imread("Frame", frame)
cv2.waitKey()

#while counting faces use person detection as face may not be visible
