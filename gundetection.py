import cv2
import imutils as us

gun_cascade=cv2.CascadeClassifier("C:/Users/zi954/AppData/Local/Programs/Python/Python310/Lib/site-packages/cv2/data/cascade.xml")
vid_cap=cv2.VideoCapture(0)

gun_exit=True
first_frame=None

while True:

    ret,frame=vid_cap.read()
    frame=us.resize(frame,width=500)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gun=gun_cascade.detectMultiScale(
        gray,
        scaleFactor=1.5,
        minNeighbors=5,
        minSize=(100,100)
    )

    for (x,w,y,h) in gun:
        frame=cv2.rectangle(frame,(x,y),(x+w,y+h),(0,250,0),5)

    cv2.imshow("Security Camera",frame)

    if cv2.waitKey(1) == ord("q"):
        break
vid_cap.release()
cv2.destroyAllWindows()
#shawaiz hassan