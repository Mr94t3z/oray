import requirement
import pathlib
import calendar
import datetime
from io import BytesIO
from flask import Flask, flash, redirect, render_template, url_for, send_file
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from wtforms.validators import InputRequired
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'static/files'

db = SQLAlchemy(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite"
now = datetime.datetime.now()


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    date_upload = db.Column(db.DateTime, server_default=db.func.now())
    data = db.Column(db.LargeBinary)


class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload File")


@app.route('/', methods=["GET", "POST"])
@app.route('/home', methods=["GET", "POST"])
def home():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data
        new_file = Item(name=file.filename, data=file.read())
        db.session.add(new_file)
        db.session.commit()

        flash('File berhasil diupload!')
        return redirect(url_for('home'))

    items = Item().query.all()

    return render_template('index.html', form=form, items=items)


@app.route('/delete/<int:id>', methods=["GET", "POST"])
def delete(id):
    item = Item().query.filter_by(id=id).first()

    db.session.delete(item)
    db.session.commit()

    flash('File berhasil dihapus!')
    return redirect(url_for('home'))


@app.route('/download/<int:id>', methods=["GET"])
def download(id):
    item = Item().query.filter_by(id=id).first()
    day = now.strftime("%A").upper()
    this_time = datetime.datetime.now()
    this_time = calendar.timegm(this_time.timetuple())
    unix_time = str(this_time)

    get_name = item.name
    file_extension = pathlib.Path(get_name).suffix

    filename = day + '-' + unix_time + file_extension

    return send_file(BytesIO(item.data), as_attachment=True, attachment_filename=filename)


if __name__ == '__main__':
    app.run(debug=True)
