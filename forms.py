from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import InputRequired


class DownloadForm(FlaskForm):
    name = StringField("Fullname: ", validators=[InputRequired('Please enter your name.')])
    email = StringField("Email: ", validators=[InputRequired("Please enter your email address.")])
    work_experiences = StringField("Work Experience: ", validators=[InputRequired("Please enter the work experiences.")])
    education = StringField("Education: ", validators=[InputRequired("Please enter education.")])
    skills = StringField("Skills: ", validators=[InputRequired("Please enter the skills.")])
    certifications = StringField("Certifications: ", validators=[InputRequired("Please enter the certifications.")])
    submit = SubmitField("Download")
