# app.py
import os
import urllib.parse, json
import base64
import uuid


from flask import Flask, jsonify, request, render_template, redirect, url_for, abort
from jinja2 import Template
import jinja2

from test import get_html

from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif']
app.config['UPLOAD_PATH'] = 'uploads'

STATIC_DIR = os.path.abspath('./templates')
TEMPLATE_DIR = os.path.abspath('./templates')
app = Flask(__name__, static_folder=STATIC_DIR, template_folder=TEMPLATE_DIR)

STAGE = os.environ.setdefault('STAGE', "False")


templateLoader = jinja2.FileSystemLoader(searchpath="./")
templateEnv = jinja2.Environment(loader=templateLoader)

# app.static_folder = 'templates'

@app.route("/")
def upload_html():
    # TEMPLATE_FILE = "templates/index.html"
    # template = templateEnv.get_template(TEMPLATE_FILE)
    
    if (STAGE=='False'):
        action = '/'
    else:
        action = "/{}/".format(STAGE)

    render_object= { "title": "HTML tags", "action":action}
    # ret = template.render(data=render_object)

    return render_template('index.html', data = render_object)



# Usage
@app.route("/", methods=["POST"])
def upload_files():


    uploads_dir = ''

    if (STAGE=='False'):
        uploads_dir = os.path.join(app.instance_path, 'uploads')
        os.makedirs(uploads_dir, exist_ok=True)
    else:
        uploads_dir = '/tmp/'

    uploaded_file = request.files['attachment']

    print('this the uploaded file',uploaded_file)
   
    filename = uploaded_file.filename
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext != ".html" and file_ext != '.txt':
            return "not an html"
            print("not html", file_ext)
        else:
            uploaded_file.save(os.path.join(uploads_dir, secure_filename("htmlTest.html")))

        # uploaded_file.save(os.path.join('temp', filename))
    
    new_str = open('instance/uploads/htmlTest.html', 'r').read()
    returned_obj = {}
    returned_obj['withNoAtt'] = get_html(new_str)
    returned_obj['withAtt'] = get_html(new_str, False)


    return render_template('table.html', data = returned_obj)
    # return get_html(new_str)

# Create a directory in a known location to save files to.

if __name__ == '__main__':
 app.run(host="0.0.0.0", port=5000)