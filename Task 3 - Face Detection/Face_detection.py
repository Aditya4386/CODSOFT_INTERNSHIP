import cv2

harcascade=cv2.CascadeClassifier(r"C:\Users\ADITYA PAWAR\AppData\Local\Programs\Python\Python313\Lib\site-packages\cv2\data\haarcascade_frontalface_alt2.xml")

video_input=cv2.VideoCapture(0)

while True:
    _,video_data=video_input.read()

    gray=cv2.cvtColor(video_data,cv2.COLOR_BGR2GRAY)

    faces=harcascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(20,20),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    for (x,y,w,h) in faces:
        cv2.rectangle(video_data,(x,y),(x+w,y+h),(0,0,255),2)

    cv2.imshow("Image Detection",video_data)
    if cv2.waitKey(5) == ord('x'):
        break

video_input.release()
cv2.destroyAllWindows()