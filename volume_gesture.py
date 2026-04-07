import cv2
import time 
import numpy as np 
import handtracking as ht
import math

from pycaw.pycaw import AudioUtilities
device = AudioUtilities.GetSpeakers()
volume = device.EndpointVolume
minvalume=volume.GetVolumeRange()[0] 
maxvolume=volume.GetVolumeRange()[1]




def main ():
    cap = cv2.VideoCapture(0)
    cap.set(3,640)
    cap.set(4,480)
    detector=ht.detect_Hands()

    ptime = 0
    vol=0
    volbar=400
    volper=0
    while True :
        success, frame = cap.read()
        if not success:
            print("error while opening the camera")
            break


        frame,lmlist=detector.find_Hands(frame)

        if len(lmlist)!=0:
            #print(lmlist[4],lmlist[8])
            x1,y1=lmlist[4][1],lmlist[4][2]
            x2,y2=lmlist[8][1],lmlist[8][2]
            cx,cy=(x1+x2)//2,(y1+y2)//2
            cv2.circle(frame,(x1,y1),10,(255,0,0),-1)
            cv2.circle(frame,(x2,y2),10,(255,0,0),-1)
            cv2.line(frame,(x1,y1),(x2,y2),(155,0,0),5)
            cv2.circle(frame,(cx,cy),10,(255,0,0),-1)
            length=math.hypot(x2-x1,y2-y1)
            #handrange 40  170
            #volume range -74  0
            vol=np.interp(length,[40,190],[minvalume,maxvolume])
            volbar=np.interp(length,[40,190],[400,150])
            volper=np.interp(length,[40,190],[0,100])
            #print(length,vol)
            volume.SetMasterVolumeLevel(vol, None)
            #print(length)
            if length<40:
                cv2.circle(frame,(cx,cy),10,(0,255,0),-1)
        cv2.rectangle(frame,(50,150),(85,400),(0,255,0),3)
        cv2.rectangle(frame,(50,int(volbar)),(85,400),(0,255,0),-1)
    
        ctime = time.time()
        fps = 1 / (ctime - ptime) if (ctime - ptime) > 0 else 0
        cv2.putText(frame, f"FPS: {int(fps)}", (10, 80), 2, 1, (0,255,0), 2)
        ptime = ctime
        cv2.putText(frame, f"{int(volper)} %", (10, 50), 2, 1, (255, 0, 255), 3)
        cv2.imshow("volume gesture ", frame)
        if cv2.waitKey(10) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
if __name__=="__main__":
    main()