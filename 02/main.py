import cv2
import os
import module3 as m3
import module4 as m4

folder = "C:/Users/Aayush/Desktop/Test"  #Directory
images = []
count = 0
dir1='C:/Users/Aayush/Desktop/output/Docs'
dir2='C:/Users/Aayush/Desktop/output/Spam'
dir3='C:/Users/Aayush/Desktop/output/Quotes'
dir4='C:/Users/Aayush/Desktop/output/withFaces'
dir5='C:/Users/Aayush/Desktop/output/Misc'
os.mkdir(dir1)
os.mkdir(dir2)
os.mkdir(dir3)
os.mkdir(dir4)
os.mkdir(dir5)

for filename in os.listdir(folder):
    #if filename.endswith(".jpg") or filename.endswith(".png"):
    im=os.path.join(folder,filename)
    img = cv2.imread(im)
    
    r= m3.captch_ex(im)
    print(r)
    if r>25:
        spam,nlines=m3.checkforspam(im)
        #print(spam)
        if spam:
            cv2.imwrite(os.path.join(dir2,filename),img)
        elif(r>=80 and nlines>7):
            cv2.imwrite(os.path.join(dir1,filename),img)
        elif nlines>1:
            cv2.imwrite(os.path.join(dir3,filename),img)
        else:
            r=25

    if r<=25:
        if m4.checkforface(img):
            cv2.imwrite(os.path.join(dir4,filename),img)
        else:
            cv2.imwrite(os.path.join(dir5,filename),img)
            

#print("No. of images in folder = " + str(count))
