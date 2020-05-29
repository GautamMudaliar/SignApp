from flask import Flask, render_template,request
#from flask_sqlalchemy import SQLAlchemy
import os
app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI']- 'sqlite:////mnt/c/Users/antho/Documents/database_files/filestorage.db' db - SQLAlchemy(app)
#db = SQLAlchemy(app)

#class FileContents(db.Model):
#    id

#ddb.Column(db. Integer, primary key True) name - db.column(db.String(300)) data - db.column (db.LargeBinary)

@app.route('/')
def index():
    return render_template('index.html' )

app.config["IMAGE_UPLOADS"] = "C:/Users/Gautam/Desktop/Pillow/version 1.1/save"


@app.route('/upload', methods=['POST'])
def upload():
    file=request.files['inputFile']
    file.save(os.path.join(app.config["IMAGE_UPLOADS"],file.filename))
    return file.filename

if __name__ =='__main__':
    app.run(debug=True)
