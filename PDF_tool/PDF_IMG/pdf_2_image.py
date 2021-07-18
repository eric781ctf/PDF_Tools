#!/usr/bin/env python
# coding: utf-8

# In[22]:


from pdf2image import convert_from_path, convert_from_bytes
import os
import time
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)

def input_file():
    X = input()
    if check(X) == 0:
        print("檔案錯誤，請重新拖曳!")
        return input_file()
    else:
        return X

def check(name):
    S = name.split('.')
    if S[len(S)-1] != 'pdf':
        return 0
    else:
        return 1

def convert(file_name):
    count_jpg = 0
    #pages = convert_from_path('./'+file_name)
    pages = convert_from_bytes(open(file_name, 'rb').read())
    print("轉換中請稍後")
    for page in pages:
        count_jpg+=1 
        page.save(add+str(count_jpg)+'_'+file_Name+'.jpg', 'JPEG')
        print("第",count_jpg,"頁")
    
    return count_jpg


# In[29]:
print("請拖曳PDF檔案至此")
file = input_file()
str2 = file.split('\\')

add=''
file_Name=''
for x in range(len(str2)):
    if x != len(str2)-1:
        add += str2[x] + '\\'
    else:
        file_Name=str2[x]
print("查找並開啟檔案中")
file_Name = file_Name[:len(file_Name)-4]

convert(file)
print("Finsih")