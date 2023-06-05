import cv2
import face_recognition

# importing images from file

img=face_recognition.load_image_file("img/Robert-Downey.jpg")
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

# finding face location and encoding of faces
faceLoc=face_recognition.face_locations(img)[0]
encode=face_recognition.face_locations(img)[0]
cv2.rectangle(img,(faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(255,255,0),2)



