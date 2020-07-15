import cv2
import math

#load image

path= 'angle.jpg'
img = cv2.imread(path)
pointList = []
#getting mouse point
def mousePoints(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN:
        size = len(pointList)
        if size !=0 and size %3!=0:
            cv2.line(img,tuple(pointList[round((size-1)/3)*3]),(x,y),(0,0,255),2)
        cv2.circle(img,(x,y),5,(0,0,255),cv2.FILLED)
        pointList.append([x,y])

def gradient(pt1,pt2):
    try:
        result=((pt2[1]-pt1[1])/(pt2[0]-pt1[0]))
        return result
    except:
        return 0

def getAngle(pointList):
    pt1,pt2,pt3 =pointList[-3:]
    m1= gradient(pt1,pt2)
    m2=gradient(pt1,pt3)
    if m1!=0 and m2!=0:

        angleR=math.atan((m2-m1)/(1+m2*m1))
        angleD=round(math.degrees(angleR))
    else:
        angleD=90
    cv2.putText(img,str(angleD),(pt1[0]-40,pt1[1]-20),cv2.FONT_HERSHEY_COMPLEX,
                1.5,(0,0,225),2)

while True:

    if len(pointList) %3==0 and len(pointList)!=0:
        getAngle(pointList)

    cv2.imshow("test window",img)
    cv2.setMouseCallback("test window",mousePoints)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        pointList =[]
        img= cv2.imread(path)



cv2.waitKey(1)