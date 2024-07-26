from pdf2image import convert_from_path
import cv2
import numpy as np 
import easyocr
import pytesseract
from autocorrect import Speller
from google.cloud import vision
import csv
import os

# img =  np.array('one/page_1.jpg')
# success, img_jpg = cv2.imencode('.jpg', img)
# byte_img = img_jpg.tobytes()
# google_img = vision.Image(content=byte_img)

# client = vision.ImageAnnotatorClient()
# resp =  client.text_detection(image=google_img)
# ocr_output = resp.text_annotations[0].description.replace('\n',' ')



# print('-'*10)
# print(ocr_output)
# print('-'*10)

path = 'one/page_1.jpg'
client = vision.ImageAnnotatorClient()
with open(path, "rb") as image_file:
    content = image_file.read()

# Create a CSV file
if not os.path.exists('google'): 
   os.makedirs('google')
csv_file_path = "google/googlecsvresults.csv"
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
  csv_writer = csv.writer(csv_file)

  image = vision.Image(content=content)
  resp =  client.text_detection(image=image)
  ocr_output = resp.text_annotations[0]
# [0].description.replace('\n',' ')
  print(ocr_output)
# Write the text to the CSV file
  csv_writer.writerow([ocr_output])

print(f'CSV file created at: {csv_file_path}')