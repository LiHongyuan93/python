from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, length

from app.form.BaseForm import BaseForm


# 编辑用户
class EditUserForm(BaseForm):
    # 用户名
    role_id = IntegerField(validators=[DataRequired(message='角色ID不允许为空')])
    # 角色ID
    pwd = StringField()
    # 第几页
    id = IntegerField(validators=[DataRequired(message='ID不允许为空')])
