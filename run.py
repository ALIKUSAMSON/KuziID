from flask import *
from forms import *
from models import *
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from passlib.hash import sha256_crypt
from flask_sqlalchemy import SQLAlchemy
import os
from functools import wraps
from werkzeug import secure_filename
import xlrd
import pandas as pd
import PyPDF2








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
UPLOAD_FOLDER1 =  'static/files'
app.config['UPLOAD_FOLDER1'] = UPLOAD_FOLDER1



db=SQLAlchemy(app)
login_manager =  LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'index'


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == int(user_id)).first()


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.',1)[1] in app.config['ALLOWED_EXTENSIONS']


@app.route("/", methods=['GET','POST'])
@app.route("/index", methods=['GET','POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None:
            if sha256_crypt.verify(form.password.data,user.password):
                user.authenticated = True
                session['logged_in'] = True
                session['username'] = form.username.data
                login_user(user)
                flash('You are now logged in', 'success')
                return redirect(url_for('home_page'))
            else:
                flash("Wrong Password, Try again", 'danger')
                return redirect(url_for('index'))
        else:
            flash("Username not found, enter correcct username",'danger')
            return redirect(url_for('index'))           
    return render_template("index.html", form=form)


@app.route("/about")
def about():

    stores = Import.query.all()

    #file = open(stores)
    #reader  = csv.reader(file)
    #for row in reader:
        #print(row)
    #file.close()
    return render_template('about.html',stores=stores)

    #filename = 'static/contents.csv'#replace filename with your csv file

@app.route("/chairman")
def chairman():
    people = Excelpost.query.all()
    return render_template('chairman.html', people=people)


@app.route("/dashboard", methods=['POST','GET'])
def dashboard():
    form = ImportForm(request.form)
    if request.method == 'POST' and form.validate():
        exceldoc = request.files['importname']
        filename = ' ';

        if exceldoc and allowed_file(exceldoc.filename):
            filename = secure_filename(exceldoc.filename)
            exceldoc.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        else:
            flash('Please upload the files with the extentions below !!!','danger')
            return redirect(url_for("dashboard"))

        imp = Import(importname = exceldoc )
        db.session.add(imp)
        db.session.commit()

        document = Import.query.filter_by(id=id).first()
        if document==filename:
            data = pd.read_excel(filename)
            workbook = xlrd.open_workbook('data', on_demand = True)
            sheet = workbook.sheets()

            for shet in sheet:

                for r in range(shet.nrows):
                    name = shet.cell_value(r,0)
                    email = shet.cell_value(r,1)
                    position = shet.cell_value(r,2)
                    year    = shet.cell_value(r,3)
                    contact = shet.cell_value(r,4)

                    ent = Leaders(name=name,email=email,position=position,year=year,contact=contact) 
                    db.session.add(ent)
                    db.session.commit()

        return redirect(url_for('chairman', filename=filename))
    return render_template("dashboard.html",form=form)


@app.route("/home_page")
def home_page():
    people = Excelpost.query.all()



    #check=send_from_directory(app.config['UPLOAD_FOLDER1'], 'ADMIN.pdf')

    check= send_from_directory(directory='static/files/ADMIN.pdf',filename=filename,mimetype='application/pdf')

    with open(check) as f:
        file_content = f.read()

        response = make_response(file_content, 200)
        response.headers['Content-type'] = 'application/pdf'
        response.headers['Content-disposition'] = ...

        return response



    return render_template("home_page.html",fileReader=fileReader)


@app.route('/upload', methods=['POST','GET'])
def upload():
    form = UploadForm()
    if form.validate_on_submit():
        entry = Leader(name = form.name.data, email=form.email.data, position=form.position.data, year=form.year.data,contact=form.contact.data,category=form.category.data)
        db.session.add(entry)
        db.session.commit()
        flash('leader uploaded successfully','success')
        return redirect(url_for('chairman'))

    return render_template('upload.html',form=form)


@app.route('/register', methods=['POST','GET'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, email=form.email.data, password=sha256_crypt.encrypt(str(form.password.data)))
        db.session.add(new_user)
        db.session.commit()
        flash('New user added successfully','success')
        return redirect(url_for('chairman'))
    return render_template('register.html', form=form)



@app.route('/others',methods=['POST','GET'])
def others():
    form = OtherForm()
    if form.validate_on_submit():
        new = Choice(namecategory=form.category.data)
        db.session.add(new)
        db.session.commit()
        flash('chairman uploaded successfully','success')
        return redirect(url_for('chairman'))
    return render_template('others.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)

