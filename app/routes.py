#from app import app
#import pdb;pdb.set_trace()
#from forms import LoginForm
from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm
#import pdb;pdb.set_trace()
@app.route("/")
@app.route("/index")
def index():
	user = {'username': 'Miguel', 'title': 'Jik'}
	posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
		},
		{
			'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
	return render_template('index.html', title='Home', user=user, posts=posts)
    #return render_template('index.html', title=None, user=user)

@app.route("/login", methods=['GET', 'POST'])
def login():
	#import pdb;pdb.set_trace()
	form = LoginForm()
	if form.validate_on_submit():
		import pdb;pdb.set_trace()
		flash('Login Requester for user {}, remember me {}'.format(
					form.username.data, form.remember_me.data))
		return redirect('/index')
	return render_template('login.html', title='Sign In', form=form)
