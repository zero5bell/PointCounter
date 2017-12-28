#import library - MUST use cv2 if using opencv_traincascade
import cv2

# load detection file (various files for different views and uses)
#faceCascade = cv2.CascadeClassifier(r'C:\opencv\build\share\OpenCV\haarcascades\haarcascade_frontalface_alt.xml')
faceCascade = cv2.CascadeClassifier(r'C:\opencv\build\share\OpenCV\haarcascades\haarcascade_eye.xml')

image = cv2.imread(r'..\image\9.jpg')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.05,
    minNeighbors=5,
    #minSize=(30, 30),
    minSize=(5, 5),
    flags = cv2.cv.CV_HAAR_SCALE_IMAGE
)

#print "Found {0} faces!".format(len(faces))
print "Found {0} Points!".format(len(faces))

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    #cv2.circle(image,((x+x+w)/2,(y+y+h)/2),w/2,(0,255,0),2)
cv2.imshow("Faces found" ,image)
cv2.waitKey(0)

