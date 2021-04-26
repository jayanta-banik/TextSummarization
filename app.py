from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename
import os

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

      # img to ocr

      # get text

      # return text
      return redirect('https://www.google.com')
		
if __name__ == '__main__':
   app.run(debug = True)