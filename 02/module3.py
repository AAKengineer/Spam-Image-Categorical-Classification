import cv2
import module1 as m1
import csv

def captch_ex(file_name):
    img = cv2.imread(file_name)
    r,c,channels= img.shape
    T_area=r*c
    
    img_final = cv2.imread(file_name)
    img2gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 180, 255, cv2.THRESH_BINARY)
    image_final = cv2.bitwise_and(img2gray, img2gray, mask=mask)
    ret, new_img = cv2.threshold(image_final, 180, 255, cv2.THRESH_BINARY)  # for black text , cv.THRESH_BINARY_INV
    '''
            line  8 to 12  : Remove noisy portion 
    '''
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3,
                                                         3))  # to manipulate the orientation of dilution , large x means horizonatally dilating  more, large y means vertically dilating more
    dilated = cv2.dilate(new_img, kernel, iterations=9)  # dilate , more the iteration more the dilation

    # for cv2.x.x

    _, contours, hierarchy = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)  # findContours returns 3 variables for getting contours

    # for cv3.x.x comment above line and uncomment line below

    #image, contours, hierarchy = cv2.findContours(dilated,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

    area=0
    for contour in contours:
        # get rectangle bounding contour
        [x, y, w, h] = cv2.boundingRect(contour)

        # Don't plot small false positives that aren't text
        if w < 35 and h < 35:
            continue

        # draw rectangle around contour on original image
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)

        cropped = img_final[y :y +  h , x : x + w]
        r,c,channels= cropped.shape
        ar =r*c
        area= area+ar
        '''
        #you can crop image and send to OCR  , false detected will return no text :)

        s = file_name + '/crop_' + str(index) + '.jpg' 
        cv2.imwrite(s , cropped)
        index = index + 1

        '''
    percent  =(area*100)/T_area
    if(percent>=100):
        percent=98
    # write original image with added contours to disk
    return percent

def checkforspam(im):
    string = m1.get_the_string(im)
    string = string.lower()
    string_list= list(string.split(" "))
    
    f = open("Spam.csv","r")

    reader = csv.reader(f)
    spam_list=[]

    for spam_words in reader:
        temp = spam_words[0].lower()
        spam_list.append(temp)

    for item in string_list:
        for item1 in spam_list:
            if item == item1:
                return True

    return False
