import cv2

face_cascade = cv2.CascadeClassifier('face_cascad.xml')
#test1.jpg can be replaced with your image file name
img = cv2.imread('test1.jpg')
#making it a single channel
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)
count=0;

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),5)
    count=count+1

print("No.of Human Face detected = ",count)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()