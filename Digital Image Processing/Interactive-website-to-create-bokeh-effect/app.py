import os
from flask import Flask, render_template, request, redirect,send_file
from werkzeug.utils import secure_filename
from bokeh import Bokeh_image


app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_and_display():
    if request.method == 'POST':
        
        if 'file' not in request.files:
            return redirect(request.url)

        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_name = 'Submit_image' + '.' + 'jpg'
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file_name))
            image_path =Bokeh_image()
            return send_file(image_path, mimetype='image/jpg')

    return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
