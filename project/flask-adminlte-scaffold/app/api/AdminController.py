import hashlib
import time
from flask import render_template, redirect, url_for, request, session
from flask_login import login_required, current_user
from app import get_logger
from app.api import admin
from app.form.EditUserForm import EditUserForm
from app.form.LoadUserForm import LoadUserForm
from app.form.NewRoleForm import NewRoleForm
from app.form.NewUserForm import NewUserForm
from app.models import User, RoleItem, Item, Role
from app.service import UserService
from app.util import Utils

logger = get_logger(__name__)


# 创建角色
@admin.route('/admin/new_role', methods=['POST'])
def new_role():
    token = request.headers.get('token')
    #用来校验令牌是否有效
    UserService.get_user_by_token(token)

    form = NewRoleForm()
    form.validate_for_api()
    name = form.name.data
    # 判断名是否重复
    role = Role.get_or_none(Role.name == name)
    if role is not None:
        return Utils.resp_failure('角色名' + name + '已存在')
    role = Role()
    role.name = name
    role.create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    role.update_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    role.save()
    return Utils.resp_success(role)

# 保存用户编辑
@admin.route('/admin/edit_user', methods=['POST'])
def edit_user():
    token = request.headers.get('token')
    #用来校验令牌是否有效
    user = UserService.get_user_by_token(token)

    form = EditUserForm()
    form.validate_for_api()
    id = form.id.data
    pwd = form.pwd.data
    role_id = form.role_id.data
    user = User.get_by_id(id)
    if pwd != '':
        user.pwd = hashlib.md5(pwd.encode(encoding='UTF-8')).hexdigest()
    user.role_id = role_id
    user.update_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    user.save()
    return Utils.show_alert('保存成功', '/go_edit_user/' + str(id))


# 删除用户
@admin.route('/admin/delete_user/<id>', methods=['POST'])
def delete_user(id):
    token = request.headers.get('token')
    #用来校验令牌是否有效
    user = UserService.get_user_by_token(token)
    user = User.get_by_id(id)
    if user.name == 'admin':
        return Utils.resp_failure('admin不允许删除')
    user.delete_instance()
    return Utils.resp_success()


# 提交创建用户表单
@admin.route('/admin/new_user', methods=['POST'])
def new_user():
    token = request.headers.get('token')
    #用来校验令牌是否有效
    user = UserService.get_user_by_token(token)
    form = NewUserForm()
    form.validate_for_api()
    name = form.name.data
    pwd = form.pwd.data
    role_id = form.roleId.data
    # 判断用户名是否重复
    user = User.get_or_none(User.name == name)
    if user is not None:
        return Utils.resp_failure('用户名' + name + '已存在')
    user = User()
    user.name = name
    user.role_id = role_id
    user.pwd = hashlib.md5(pwd.encode(encoding='UTF-8')).hexdigest()
    user.enabled = 1
    user.create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    user.update_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    user.save()
    return Utils.resp_success(user)


# 获取用户列表
@admin.route('/admin/load_user', methods=['POST'])
def load_user():
    token = request.headers.get('token')
    #用来校验令牌是否有效
    user = UserService.get_user_by_token(token)
    form = LoadUserForm()
    # 第几页
    current_page = form.currentPage.data
    # 用户名模糊查询
    name = form.userName.data
    # 角色模糊查询
    role_id = form.roleId.data
    return Utils.resp_success(UserService.find_user_by_name_role_page(name, role_id, current_page))


# 左边菜单
@admin.route('/admin/get_menus', methods=['POST'])
def left():
    #用来校验令牌是否有效
    user = UserService.get_user_by_token(request.headers.get('token'))
    # 根据角色ID获取对应的权限列表
    role_items = RoleItem.select().where(RoleItem.role_id == user.role_id)
    # 根据菜单ID查出所有的菜单详情
    items = []
    for roleItem in role_items:
        item = Item.get_by_id(roleItem.item_id)
        items.append(item)
    return Utils.resp_success(items)


# 个人信息接口
@admin.route('/admin/me', methods=['POST'])
def index():
    token = request.headers.get('token')
    #用来校验令牌是否有效
    user = UserService.get_user_by_token(token)
    return Utils.resp_success(user)
