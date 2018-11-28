import cv2
import os
import module3 as m3

folder = "C:/Users/Aayush/Desktop/Test"  #Directory
#s1= "C:/Users/Aayush/Desktop/1"
#s2= "C:/Users/Aayush/Desktop/2"
images = []
count = 0
dir1='C:/Users/Aayush/Desktop/output/1'
dir2='C:/Users/Aayush/Desktop/output/2'
dir3='C:/Users/Aayush/Desktop/output/3'
os.mkdir(dir1)
os.mkdir(dir2)
os.mkdir(dir3)

for filename in os.listdir(folder):
    #if filename.endswith(".jpg") or filename.endswith(".png"):
    im=os.path.join(folder,filename)
    img = cv2.imread(im)
    if img is not None:
        images.append(img)
        count = count + 1

    r= m3.captch_ex(im)
    print(r)

    if m3.checkforspam(im):
        cv2.imwrite(os.path.join(dir2,filename),img)
    elif(r>=80):
        cv2.imwrite(os.path.join(dir1,filename),img)

    elif(r>=20 and r<80):
        if m3.checkforspam(im):
            cv2.imwrite(os.path.join(dir2,filename),img)
        else:
            cv2.imwrite(os.path.join(dir3,filename),img)



#print("No. of images in folder = " + str(count))
