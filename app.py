from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename
import os
from pdf2image import convert_from_path
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files (x86)/Tesseract-OCR/tesseract'
path_to_poopler = r"C:/Users/JOY/Desktop/poppler-21.02.0/Library/bin"
app = Flask(__name__)
# app.config['UPLOAD_FOLDER']
# app.config['MAX_CONTENT_PATH']
@app.route('/upload')
def upload_file():
	with open('upload.html') as file:
		s = file.read()
	return s
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_files():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))

      # check file extension 
      imgs = convert_from_path(f.filename, poppler_path=path_to_poopler)
      img = imgs[0]
      # img to ocr
      s = pytesseract.image_to_string(img)
      # get text

      # return text
      return s
		
if __name__ == '__main__':
   app.run(debug = True)