from email import message
from tarfile import LENGTH_NAME
import wtforms
from wtforms.validators import Email, Length, EqualTo
from models import UserModel, EmailCaptchaModel
# The validator to verify if your email is valid


class RegisterFrom(wtforms.Form):
    # validate the format of email address
    email = wtforms.StringField(
        validators=[Email(message="The format of email is wrong")])
    # validate the length of verification code
    captcha = wtforms.StringField(
        validators=[Length(min=4, max=4, message="The format of captcha is wrong")])
    # validate the password, require the length has to be between 6 - 10
    password = wtforms.StringField(
        validators=[Length(
            min=6, max=20, message="The length of password has to be between 6 to 20")]
    )
    password_confirm = wtforms.StringField(validators=[EqualTo("password")])
    username = wtforms.StringField(
        validators=[Length(min=3, max=20, message="The format of username is wrong")])

    # validate if the email has been used (already in the database)
    def validate_email(self, field):
        email = field.data
        user = UserModel.query.filter_by(email=email).first()
        if user:
            raise wtforms.ValidationError(message="the email address exists")

     # validate if the verification code is correct
    def validate_captcha(self, field):
        captcha = field.data
        email = self.email.data
        captcha_model = EmailCaptchaModel.query.filter_by(
            email=email, captcha=captcha).first()
        if not captcha_model:
            raise wtforms.ValidationError(
                message="the email address or the captcha is wrong")
        # TODO: Delete captcha_model


class LoginForm(wtforms.Form):
    # validate the email and password
    email = wtforms.StringField(
        validators=[Email(message="The format of email is wrong")])
    password = wtforms.StringField(
        validators=[Length(
            min=6, max=20, message="The length of password has to be between 6 to 20")]
    )


class QuestionForm(wtforms.Form):
    title = wtforms.StringField(
        validators=[Length(
            min=6, max=200, message="The length of title is wrong")]
    )
    content = wtforms.StringField(
        validators=[Length(
            min=3, message="The content format is wrong")]
    )
    
