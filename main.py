import cv2
import face_recognition

# importing images from file

img=face_recognition.load_image_file("img/Robert-Downey.jpg")
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

# finding face location and encoding of faces
faceLoc=face_recognition.face_locations(img)[0]
encode=face_recognition.face_encodings(img)[0]
cv2.rectangle(img,(faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(255,255,0),2)

# processing on tets image
imgTest=face_recognition.load_image_file('img/test4.jpg')
imgTest=cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)
testLoc=face_recognition.face_locations(imgTest)[0]
testEncode=face_recognition.face_encodings(imgTest)[0]
print(faceLoc)


result=face_recognition.compare_faces([encode],testEncode)
faceDis=face_recognition.face_distance([encode],testEncode)
print(result)

if(result[0]==True):
    c=(24, 245, 24)
    text="IMAGE MATCHED"
else:
    c=(24, 24, 245)
    text="IMAGE NOT MATCHED"

loc=(testLoc[1],testLoc[0])
cv2.rectangle(imgTest,(testLoc[3],testLoc[0]),(testLoc[1],testLoc[2]),c,2)
cv2.putText(imgTest,text,loc,cv2.FONT_HERSHEY_COMPLEX,1,c,2)
cv2.putText(imgTest,str(faceDis[0]),(loc[0],loc[1]+35),cv2.FONT_HERSHEY_COMPLEX,1,c,2)
cv2.imshow('testImage',imgTest)
cv2.waitKey(0)



