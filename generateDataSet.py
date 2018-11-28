import cv2 
import numpy as np
import urllib

url='http://192.168.201.2:8080/shot.jpg'

def generate():
    Id=0
    face_cascade =cv2.CascadeClassifier('C:\\Users\\Abhishek\\Anaconda3\\pkgs\\libopencv-3.4.1-h875b8b8_3\\Library\\etc\\haarcascades\\haarcascade_frontalface_default.xml')    
    print("Starting Creating Face Recognition dataset" )
    while(True):
        imgResponse = urllib.request.urlopen(url)
 
        # Numpy to convert into a array
        imgNp = np.array(bytearray(imgResponse.read()),dtype=np.uint8)
 
        # Decode the array to OpenCV usable format
        img = cv2.imdecode(imgNp,-1)
        
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
        faces=face_cascade.detectMultiScale(gray,1.3,5)
        
        for x,y,w,h in faces:
            newImg=cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            f=cv2.resize(gray[y:y+h,x:x+w],(200,200))
            Id=Id+1
            cv2.imwrite('C:\\Users\\Abhishek\\Local data\\'+str(Id)+'.jpg',f)
        cv2.imshow("camera",img)
        if cv2.waitKey(int(1000/12)) & 0xff==ord("q"):
            break
        
    cv2.destroyAllWindows()
    print("Dataset is created successfully and saved at C:\\Users\\Abhishek\\face dataset")

if __name__=="__main__":
    generate()