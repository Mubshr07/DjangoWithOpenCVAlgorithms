from django.http import HttpResponse
from django.shortcuts import render, redirect

from DjangoWithOpenCVAlgorithms import forms
from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR3 = Path().resolve()

import cv2
import numpy as np
import matplotlib.pyplot as mplot 


from .models import openCVimages

def homePage(request):
    data = dict()
    data['title'] = "Mubashir Iqbal +92-318-5099232"
    return render(request, 'homePage.html', data)


def imageUpload(request):

    data = dict()
    data['title'] = "Mubashir Iqbal Form"
    data['fileUpload'] = "File needs to be uploaded."
    data['imageUploadingForm'] = forms.imageUploadingForm()

    try:
        if(request.method == "POST"):
            print("\n\n Form Submitted: ")
            #print(request.FILES) 

            acctualFileName = request.FILES.get("image4openCV")
            imgModel = openCVimages()
            imgModel.name = request.POST.get("name")    
            imgModel.image = request.FILES.get("image4openCV")
            imgModel.choice_field = request.POST.get("choice_field")
            print("\n -> imgModel : {} ".format(imgModel))

            imgModel.save()

            fileUrls = imgModel.image.url 
            print("File URL: {} ".format(fileUrls)) 
            
            print(" ------------------------------------- \n\n\n ")
            data['fileUploadList'] = fileUrls
            data['imageSize'] = imgModel.choice_field
 
            dirPath = str(BASE_DIR3)
            #print(dirPath)
            dirPath = dirPath.replace('\\','/')
            #print(dirPath)
            readFilePath = dirPath + fileUrls
            print("readFilePath : {} ".format(readFilePath))

 
            img = cv2.imread(readFilePath)
            print(img.shape)
            '''
            target_width = 300
            target_height = 200
            aspect_ratio = img.shape[1] / img.shape[0]
            if aspect_ratio > 1:
                new_width = target_width
                new_height = int(new_width / aspect_ratio)
            else:
                new_height = target_height
                new_width = int(new_height * aspect_ratio)

            resized = cv2.resize(img, (new_width, new_height)) 
            img = resized
            '''
            grayScaleURL =  "/media/uploads/grayScale.png"
            grayScaleImagePath =  dirPath + grayScaleURL
            print(grayScaleImagePath)

            grayScale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
            cv2.imwrite(grayScaleImagePath, grayScale)
            data['grayScale'] = grayScaleURL
            
            imageURL =  "/media/uploads/blurImage.png"
            imagePath =  dirPath + imageURL
            cv2Image =  cv2.GaussianBlur(img, (5, 5), 0) 
            cv2.imwrite(imagePath, cv2Image)
            data['blurImage'] = imageURL
                        
            imageURL =  "/media/uploads/cannyEdgeDetection.png"
            imagePath =  dirPath + imageURL
            cv2Image =  cv2.Canny(img, 100, 200)
            cv2.imwrite(imagePath, cv2Image)
            data['cannyEdgeDetection'] = imageURL
            
            imageURL =  "/media/uploads/thresholdImage.png"
            imagePath =  dirPath + imageURL
            
             
            _, cv2Image =  cv2.threshold(grayScale, 127, 255, cv2.THRESH_BINARY)
            cv2.imwrite(imagePath, cv2Image)
            data['thresholdImage'] = imageURL
            
            imageURL =  "/media/uploads/DilationImage.png"
            imagePath =  dirPath + imageURL            
            kernel = np.ones((5, 5), np.uint8) 
            cv2Image =  cv2.dilate(img, kernel, iterations=1)
            cv2.imwrite(imagePath, cv2Image)
            data['DilationImage'] = imageURL

            imageURL =  "/media/uploads/erosionImage.png"
            imagePath =  dirPath + imageURL          
            cv2Image =  cv2.erode(img, kernel, iterations=1)
            cv2.imwrite(imagePath, cv2Image)
            data['erosionImage'] = imageURL



 

    except:
        pass

    return render(request, 'imageUpload.html', data)


def contactUs(request):
    data = dict()
    data['title'] = "Contact Us"
    data['form'] = forms.contactUsForm()
    return render(request, 'contactUs.html', data)