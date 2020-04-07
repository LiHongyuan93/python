from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, length

from app.form.BaseForm import BaseForm


# 新增角色
class NewRoleForm(BaseForm):
    # 角色名
    name = StringField(validators=[DataRequired(message='角色名不允许为空'), length(
            min=2, max=32
    )])
