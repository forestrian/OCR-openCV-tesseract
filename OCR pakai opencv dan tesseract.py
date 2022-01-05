#!/usr/bin/env python
# coding: utf-8

# In[1]:


#pip install opencv pytesseract di anaconda prompt
import cv2
import numpy as np
import pytesseract


# In[2]:


# Install Tesseract OCR di local link> https://github.com/UB-Mannheim/tesseract/wiki
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe" #copy path tempat tesseract terinstall


# In[3]:


# Muat Gambar
img = cv2.imread("download.jpg")


# In[4]:


# 2. Ubah ukuran Gambar
img = cv2.resize(img, None, fx=1, fy=1)


# In[5]:


# 3. Ubah gambar ke grayscale (konversi warna)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# In[6]:


# 4. konversi gambar ke hitam putih (menggunakan adaptive threshold)
adaptive_threshold = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 25, 11)


# In[ ]:


config = "--psm 3" #psm (page segmentation mode)
"""Page segmentation modes:
  0    Orientation and script detection (OSD) only.
  1    Automatic page segmentation with OSD.
  2    Automatic page segmentation, but no OSD, or OCR.
  3    Fully automatic page segmentation, but no OSD. (Default)
  4    Assume a single column of text of variable sizes.
  5    Assume a single uniform block of vertically aligned text.
  6    Assume a single uniform block of text.
  7    Treat the image as a single text line.
  8    Treat the image as a single word.
  9    Treat the image as a single word in a circle.
 10    Treat the image as a single character.
 11    Sparse text. Find as much text as possible in no particular order.
 12    Sparse text with OSD.
 13    Raw line. Treat the image as a single text line, bypassing hacks that are Tesseract-specific."""

text = pytesseract.image_to_string(adaptive_threshold, config=config, lang="eng")
print(text)

cv2.imshow("gray", gray)
cv2.imshow("adaptive th", adaptive_threshold)
cv2.waitKey(0)

