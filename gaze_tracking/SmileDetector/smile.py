#https://dev.to/sadmansakib2234/realtime-smile-detector-299e
#https://m.blog.naver.com/PostView.naver?blogId=ljy9378&logNo=221439207705&proxyReferer=https:%2F%2Fwww.google.com%2F
import cv2 

# Face and Smile classifiers
face_detector = cv2.CascadeClassifier('C:/Users/XNOTE/Downloads/opencv/sources/data/haarcascades/haarcascade_frontalface_default.xml')
smile_detector = cv2.CascadeClassifier('C:/Users/XNOTE/Downloads/opencv/sources/data/haarcascades/haarcascade_smile.xml')

# Grab Webcam feed
webcam = cv2.VideoCapture(0)

while True:

    successful_frame_read, frame = webcam.read()

    # if there is an error or abort
    if not successful_frame_read:
        break
    
    # Change to grayscale
    frame_grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces first
    faces = face_detector.detectMultiScale(frame_grayscale, 1.3, 5)

    # Run smile detection within each of those faces
    for (x, y, w, h) in faces:
        # draw a square around smile
        cv2.rectangle(frame, (x, y), (x+w, y+h), (100, 200, 50), 4)

        # Draw a sub image
        face = frame[y:y+h, x:x+w]

        # Grayscale the face
        face_grayscale = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
 
        # Detect Smile in the face 😄
        #smile = smile_detector.detectMultiScale(face_grayscale, 1.7,20)
        smile = smile_detector.detectMultiScale(face_grayscale, 1.8,20)
        # Label the face as smiling 

        if len(smile) > 0:
            cv2.putText(frame, 'Smiling', (x,y+h+40), fontScale=3,
            fontFace=cv2.FONT_HERSHEY_PLAIN, color=(255,255,255))

        # Show the current frame
        cv2.imshow('Smile Detector', frame)

        # Stop if 'Q' is pressed
        key = cv2.waitKey(1)   
        if key == 81 or key==113:
            break

# Clear up!
webcam.release() 
cv2.destroyAllWindows()