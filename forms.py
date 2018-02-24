from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, BooleanField, ValidationError, SelectField, IntegerField, FileField, DateField
from wtforms.validators import Required, Email, Length, EqualTo, AnyOf, Regexp, Optional
from models import *
from wtforms.ext.sqlalchemy.fields import QuerySelectField
import datetime


class RegistrationForm(Form):
    username = StringField('Username',validators=[Required(), Length(min=4,max=18)])
    email = StringField('Email',validators=[Required(),Email(message='Invalid address'),Length(min=1,max=64)])
    password = PasswordField('Password',validators=[Required(), Length(min=6, message="Password must be 6 characters as and more"),EqualTo('confirm',message='Passwords do not match')])
    confirm = PasswordField('Confirm Password')
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')

class LoginForm(Form):
    username = StringField('Username',validators=[Required(),Length(min=5,max=25)])
    password = PasswordField('Password',validators=[Required(), Length(min=6, message="Password must be 6 characters as and more")])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')


class UploadForm(Form):
    
    name = StringField('FUll Name',validators=[Required()])
    email = StringField('Email',validators=[Required(),Email(message='Invalid address'),Length(min=1,max=64)])
    position = StringField('Position',validators=[Required()])
    year = DateField('Year of duty',validators=[Required()])
    contact = StringField('Contact',validators=[Required()])
    #category = StringField('Category Name', validators=[Required()])
    category = SelectField('Category', choices=(('lc5','LC5 chairperson'),('womanmp','Woman MP'),('Womanc','Woman Counsellor'),
                                    ('nrm','NRM Chairperson'),
                ('special','Special GPs'),('er','ER MPs'),('army','ARMY MPs'),('const','Constituency Leaders'),
                    ('ledge','Ledges'),('other','Others leaders')))
    submit = SubmitField('upload')


class OtherForm(Form):
    #namecategory = StringField('Category Name', validators=[Required()])
    category = SelectField('Category', choices=[('lc5','LC5 chairperson'),('womanmp','Woman MP'),('Womanc','Woman Counsellor'),
                                    ('nrm','NRM Chairperson'),
                ('special','Special GPs'),('er','ER MPs'),('army','ARMY MPs'),('const','Constituency Leaders'),
                    ('ledge','Ledges'),('other','Others leaders')])
    submit = SubmitField('upload')

class ImportForm(Form):
    importname = FileField('Browser here')
    submit = SubmitField('upload')

class ChoiceForm(Form):
    opts = QuerySelectField(query_factory=choice_query, allow_blank=True,get_label='namecategory')



