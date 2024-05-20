import os
from flask import Flask as f, redirect
from flask import render_template as ren
from flask import  url_for, request
from predict import get_cat_breed
app = f(__name__)

from predict import get_cat_breed
# GET and POST are here because we receive and send data to back-end.
@app.route('/', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		if 'file' not in request.files:
			return redirect(request.url)
		file = request.files.get('file')
		if not file:
			return
		img_bytes = file.read()
		prediction_name, confidence = get_cat_breed(img_bytes)
		return ren('re.html', name=prediction_name, confidence=confidence)#.lower())#, description=diseases[prediction_name])

	return ren('temp.html')

            

if __name__=="__main__":
    app.run(debug=True)
