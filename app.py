from pdf2image import convert_from_path
import pytesseract
import csv
from pytesseract import Output
import os

file = 'one.pdf'
file_folder = 'sample_files/'
file_name = file_folder + file
# Convert PDF to images
images = convert_from_path(file_name)
file_prefix = file.split('.')[0]
print(file_prefix)

# Create a CSV file
if not os.path.exists(file_prefix): 
   os.makedirs(file_prefix)
csv_file_path = f"{file_prefix}/{file_prefix}.csv"
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
  csv_writer = csv.writer(csv_file)

  # Iterate over each image
  for i, image in enumerate(images):
    # Save the image
    image_path = f'{file_prefix}/page_{i}.jpg'
    image.save(image_path, 'PNG')

#   for i, image in enumerate(images):
#     # Save the image
#     image_path = f'{file_prefix}/page_{i}.png'
#     image.save(image_path, 'PNG')

    # Use pytesseract to extract text from the image
    text = pytesseract.image_to_string(image_path, output_type=Output.STRING)

    # Print the extracted text
    print(text)

    # Write the text to the CSV file
    csv_writer.writerow([text])

print(f'CSV file created at: {csv_file_path}')