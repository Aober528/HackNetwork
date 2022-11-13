from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, EqualTo
import os

class LoginForm(FlaskForm):
	users = list(os.walk('.\\Game\\Saves'))[0][1]
	username = SelectField(label='用户名', choices=users)
	password = PasswordField(label='密　码', validators=[DataRequired('密码不能为空')])
	submit = SubmitField(label='登录')

class RegisterForm(FlaskForm):
	username = StringField(label='　用户名', validators=[DataRequired('密码不能为空')])
	password = PasswordField(label='　密　码', validators=[DataRequired('密码不能为空')])
	password_ = PasswordField(label='确认密码', validators=[EqualTo('password', message='密码不同')])
	submit = SubmitField(label='注册')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'aober'

@app.route('/', methods=['GET', 'POST'])
def Index():
	return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def Login():
	users = list(os.walk('.\\Game\\Saves'))[0][1]
	if users == []:
		return redirect(url_for('Register'))
	else:
		form = LoginForm()
		data = {}
		if form.validate_on_submit():
			data['username'] = form.username.data
			data['password'] = form.password.data
		return render_template('login.html', form = form, data = data)

@app.route('/register', methods=['GET', 'POST'])
def Register():
	form = RegisterForm()
	data = {}
	if form.validate_on_submit():
		data['username'] = form.username.data
		data['password'] = form.password.data
		data['password_'] = form.password_.data
	return render_template('register.html', form = form)

if __name__ == '__main__':
	app.run(debug = True, host='0.0.0.0', port=52800)