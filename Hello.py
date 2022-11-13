from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
	username = StringField(label='用户名', validators=[DataRequired('用户名不能为空')])
	password = PasswordField(label='密  码', validators=[DataRequired('密码不能为空')])
	submit = SubmitField(label='提交')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'aober'

@app.route('/', methods=['GET', 'POST'])
def helloWorld():
	form = LoginForm()
	data = {}
	if form.validate_on_submit():
		data['username'] = form.username.data
		data['password'] = form.password.data
	return render_template('login.html', form = form, data = data)


if __name__ == '__main__':
	app.debug = True
	app.run()