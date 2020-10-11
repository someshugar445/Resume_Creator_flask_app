from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import InputRequired


class DownloadForm(FlaskForm):
    name = StringField("Fullname: ", validators=[InputRequired('Please enter your name.')])
    email = StringField("Email: ", validators=[InputRequired("Please enter your email address.")])
    projects = StringField("Projects: ", validators=[InputRequired("Please enter a the projects.")])
    education = StringField("Education: ", validators=[InputRequired("Please enter education.")])
    skills = StringField("Skills: ", validators=[InputRequired("Please enter the skills.")])
    submit = SubmitField("Download")
