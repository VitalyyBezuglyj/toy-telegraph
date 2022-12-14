from flask import Flask, render_template, url_for, redirect, flash

from flask_mdeditor import MDEditor
import os



app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['MDEDITOR_FILE_UPLOADER'] = os.path.join(basedir, 'uploads')
app.config['SECRET_KEY'] = "6ac134d3a4f29c752d82b9a2122a4af9"
mdeditor = MDEditor(app)


from toy_telegraph import routes