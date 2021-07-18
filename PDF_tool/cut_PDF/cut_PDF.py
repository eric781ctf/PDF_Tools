#!/usr/bin/env python
# coding: utf-8

# In[1]:


import PyPDF2
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

print("請拖曳PDF檔案至此")
file = input_file()

str2 = file.split('\\')

add=''
file_name=''
for x in range(len(str2)):
    if x != len(str2)-1:
        add += str2[x] + '\\'
    else:
        file_name=str2[x]

pdfReader = PyPDF2.PdfFileReader(file)
pdfnums = pdfReader.numPages

pdfWriter = PyPDF2.PdfFileWriter()

def input_page():
    a = int(input())
    if a <= pdfnums:
        return a
    else:
        print("輸入頁數不存在，請重新輸入")
        return input_page()

# In[4]:
print("輸入你不要的頁碼(一次一頁):")
delete = input_page()
delete = delete - 1
for i in range(pdfnums): # Defined the page you want
    if i == delete:
        continue
    else:
        pageObj = pdfReader.getPage(i)
        pdfWriter.addPage(pageObj)
with open(add+'1_'+file_name, 'wb') as pdfOutputFile: pdfWriter.write(pdfOutputFile) # Name the file

print("Finish!")
print('另存新檔為:','1_'+file_name)



