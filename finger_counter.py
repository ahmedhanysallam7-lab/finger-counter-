import cv2 
import time 
import os
import handtracking as ht 


cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

cap.set(3,640)
cap.set(4,480)
ptime=0
path=r"D:\fingers"
list=os.listdir(path)
#print(list)
list1=[]
for imgpath in list:
    img=cv2.imread(f"{path}/{imgpath}")
    list1.append(img)
#print(len(list1))
detector=ht.detect_Hands()
tipIDS=[4,8,12,16,20]
while True:
    success, frame = cap.read()
    if not success:
        break

    frame,lmlist=detector.find_Hands(frame)
    if len(lmlist)!=0:
        fingers=[]

        if lmlist[tipIDS[0]][1]<lmlist[tipIDS[0]-1][1]:
            fingers.append(0)
        else:
            fingers.append(1)

        for i in range(1,5):
                if lmlist[tipIDS[i]][2]<lmlist[tipIDS[i]-2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)

        fingers_count=sum(fingers)

        if fingers_count==0:
            img = list1[5]

            h_frame, w_frame, _ = frame.shape
            img_resized = cv2.resize(img, (w_frame//3, h_frame//3))

            h, w, _ = img_resized.shape
            frame[0:h, 0:w] = img_resized
        else:
        
            img = list1[fingers_count-1]

            h_frame, w_frame, _ = frame.shape
            img_resized = cv2.resize(img, (w_frame//3, h_frame//3))

            h, w, _ = img_resized.shape
            frame[0:h, 0:w] = img_resized
        cv2.rectangle(frame,(20,225),(170,425),(0,255,0),cv2.FILLED)
        cv2.putText(frame,str(fingers_count),(45,375)
                    ,cv2.FONT_HERSHEY_PLAIN,10,(255,0,0),25)

            

        print(fingers)

    

    ctime = time.time()
    fps = 1 / (ctime - ptime) if (ctime - ptime) > 0 else 0
    ptime = ctime

    cv2.putText(frame, str(int(fps)), (400,70), 2, 1, (255, 0, 255), 3)



    cv2.imshow("finger counter ", frame)
  

    if cv2.waitKey(10) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()