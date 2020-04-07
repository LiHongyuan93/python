from wtforms import StringField, IntegerField
from app.form.BaseForm import BaseForm


# 获取用户列表
class LoadUserForm(BaseForm):
    # 用户名
    userName = StringField()
    # 角色ID
    roleId = StringField()
    # 第几页
    currentPage = IntegerField(default=1)
