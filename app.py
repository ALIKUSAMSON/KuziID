from flask import Flask , render_template
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import Form
from wtforms.ext.sqlalchemy.fields import QuerySelectField


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:dengima@localhost/logbook'
app.config['SECRET_KEY'] = 'secret'

db = SQLAlchemy(app)

class Choice(db.Model):
	__tablename__ ="category"
	id = db.Column(db.Integer, primary_key=True)
	namecategory = db.Column (db.String(50))

	def __repr__(self):
		return '{}'.format(self.namecategory)

def choice_query():
	return Choice.query

class ChoiceForm(Form):
	opts = QuerySelectField(query_factory=choice_query, allow_blank=True,get_label='namecategory')


@app.route('/check', methods=["POST",'GET'])
def check():
	form = ChoiceForm()
	if form.validate_on_submit():
		return '<html><h1></html>{}</h1>'.format(form.opts.data)

	return render_template('check.html',form=form)

if __name__ == '__main__':
	app.run(debug=True)