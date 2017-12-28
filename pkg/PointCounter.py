#import library - MUST use cv2 if using opencv_traincascade
import cv2

# load detection file (various files for different views and uses)
#pointCascade = cv2.CascadeClassifier(r'C:\opencv\build\share\OpenCV\haarcascades\haarcascade_frontalface_alt.xml')
pointCascade = cv2.CascadeClassifier(r'C:\opencv\build\share\OpenCV\haarcascades\haarcascade_eye.xml')

image = cv2.imread(r'..\image\91.jpg')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect points in the image
points = pointCascade.detectMultiScale(
    gray,
    #scaleFactor=1.1,
    #minNeighbors=5,
    #minSize=(30, 30),
    
    scaleFactor=1.001,
    minNeighbors=2,
    minSize=(20, 20),

    flags = cv2.cv.CV_HAAR_SCALE_IMAGE
)

print "Found {0} Points!".format(len(points))

# Draw a rectangle around the points
for (x, y, w, h) in points:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    #cv2.circle(image,((x+x+w)/2,(y+y+h)/2),w/2,(0,255,0),2)
cv2.imshow("Points found" ,image)
cv2.waitKey(0)

