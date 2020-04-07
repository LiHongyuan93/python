from wtforms import StringField
from wtforms.validators import DataRequired, length

from app.form.BaseForm import BaseForm


# 登录表单
class LoginForm(BaseForm):
    userName = StringField(validators=[DataRequired(message='用户名不允许为空'), length(
            min=5, max=32
    )])
    userPw = StringField(validators=[DataRequired(message='密码不允许为空')])
