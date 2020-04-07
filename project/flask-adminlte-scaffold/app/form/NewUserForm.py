from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, length

from app.form.BaseForm import BaseForm


# 新增用户
class NewUserForm(BaseForm):
    # 用户名
    name = StringField(validators=[DataRequired(message='用户名不允许为空'), length(
            min=6, max=32
    )])
    # 角色ID
    pwd = StringField(validators=[DataRequired(message='密码不允许为空')])
    # 第几页
    roleId = IntegerField(validators=[DataRequired(message='角色不允许为空')])
