from PIL import Image

import cv2
import pytesseract
import os
import numpy as np
import pandas as pd
import re

from pdf2image import convert_from_bytes

# Some help functions 
def get_conf(page_gray):
    '''return a average confidence value of OCR result '''
    df = pytesseract.image_to_data(page_gray,output_type='data.frame')
    df.drop(df[df.conf==-1].index.values,inplace=True)
    df.reset_index()
    return df.conf.mean()
  
def deskew(image):
    '''deskew the image'''
    gray = cv2.bitwise_not(image)
    temp_arr = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    coords = np.column_stack(np.where(temp_arr > 0))
    angle = cv2.minAreaRect(coords)[-1]
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return rotated
  

OCR_dic={} 
root_path = "C:/BeCode/KPMG_data/A/"
for root, dirs, files in os.walk(root_path):      
    for  d in dirs:        
        for root2, dirs2, files2 in os.walk(os.path.join(root,d)): 
            for f in files2:    
                f = "C:/BeCode/KPMG_data/A/100/100-2021-015016.pdf"             
                file = os.path.join(root2,f)
                pdf_file = convert_from_bytes(open(file, 'rb').read()) #pdf to image
                # create a df to save each pdf's text
                pages_df = pd.DataFrame(columns=['conf','text'])
                for (i,page) in enumerate(pdf_file) :
                    try:
                        # transfer image of pdf_file into arraycm
                        page_arr = np.asarray(page)
                        
                        page_arr_gray = cv2.cvtColor(page_arr,cv2.COLOR_BGR2GRAY)#to gray scale
                        
                        page_deskew = deskew(page_arr_gray)#deskew the page
                        # cal confidence value
                        page_conf = get_conf(page_deskew)#confidece value
                        #convert to text and appen to the list 
                        pages_df = pages_df.append({'conf': page_conf,'text': pytesseract.image_to_string(page_deskew)}, ignore_index=True)
                    except:
                        #docs that have problem and unable to convert
                        pages_df = pages_df.append({'conf': -1,'text': 'N/A'}, ignore_index=True)
                        continue
                
                OCR_dic[file]=pages_df #append the file to directory
                print('{} is done'.format(file))
                break
            break
        break
    break
        

with open("C:/BeCode/KPMG_data/data_category/extracted_text_ocr2.txt", 'w+') as f:
    for value in OCR_dic.values():
        f.write('{}\n'.format(value))
    
    f.close()
    


