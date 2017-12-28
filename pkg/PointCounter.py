#-*- coding: UTF-8 -*- 
#import library - MUST use cv2 if using opencv_traincascade
import cv2

# load detection file (various files for different views and uses)
#pointCascade = cv2.CascadeClassifier(r'C:\opencv\build\share\OpenCV\haarcascades\haarcascade_frontalface_alt.xml')
pointCascade = cv2.CascadeClassifier(r'.\cascade\haarcascade_point.xml')

image = cv2.imread(r'.\image\9.jpg')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect points in the image
points = pointCascade.detectMultiScale(
    gray,
    
    #被检测对象的尺度变化。尺度越大，越容易漏掉检测的对象，但检测速度加快；尺度越小，检测越细致准确，但检测速度变慢；
    #scaleFactor=1.1,
    #数值越大，检测到对象的条件越苛刻，反之检测到对象的条件越宽松；
    #minNeighbors=5,
    #检测的对象最小尺寸，单位是像素*像素，使对象落在检测器的大小范围内；
    #minSize=(30, 30),
    
    scaleFactor=1.001,
    minNeighbors=5,
    minSize=(20, 20),

    flags = cv2.cv.CV_HAAR_SCALE_IMAGE
)

#print "Found {0} Points!".format(len(points))

# Draw a rectangle around the points
for (x, y, w, h) in points:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    #cv2.circle(image,((x+x+w)/2,(y+y+h)/2),w/2,(0,255,0),2)
#cv2.namedWindow("{0} Points found".format(len(points)))
cv2.imshow("{0} points found".format(len(points)),image)
cv2.waitKey(0)

