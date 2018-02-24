from flask import *
from forms import *
from models import *
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from passlib.hash import sha256_crypt
from flask_sqlalchemy import SQLAlchemy
import os
from werkzeug import secure_filename
import csv

app = Flask(__name__, instance_relative_config=True)
WTF_CSRF_ENABLED = True
app.secret_key = "national resistance movement"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:dengima@localhost/logbook'
app.config['SQLALCHEMY_ECHO'] = True  # Show SQL commands created
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

app.config['ALLOWED_EXTENSIONS'] = set(['xls', 'xlsx', 'ods', 'csv', 'tsv', 'csvz', 'tsvz'])
app.config['MAX_CONTENT_LENGTH'] = 1000 * 1024 * 1024 
app.config['UPLOAD_FOLDER'] = os.path.realpath('.') +'/static/uploads/doc'

db=SQLAlchemy(app)
login_manager =  LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'index'

class FileContent(db.Model):
    __tablename__ = 'filecontent'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300))
    data = db.Column(db.LargeBinary)

@app.route("/chairman")
def chairman():
	return render_template("chairman.html")

@app.route('/dashboard',methods=['POST','GET'])
def dashboard():
    form = ImportForm()
    if form.validate_on_submit():
        file = request.files['importname']
        new = FileContent(name=form.importname.data, data=file.read())
        db.session.add(new)
        db.session.commit()
        return redirect(url_for('chairman'))
        return 'saved' + file.filename + 'to the database!'
    return render_template('dashboard.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)



#category = SelectField('Category', choices=[('lc5','LC5 chairperson'),('womanmp','Woman MP'),('Womanc','Woman Counsellor'),
    #                                ('nrm','NRM Chairperson'),
    #           ('special','Special GPs'),('er','ER MPs'),('army','ARMY MPs'),('const','Constituency Leaders'),
    #                ('ledge','Ledges'),('other','Others leaders')])
    #opts = QuerySelectField('Select category', query_factory=choice_query, allow_blank=True,get_label='namecategory')