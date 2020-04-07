# -*- coding: utf-8 -*-
import time
from peewee import MySQLDatabase, Model, CharField, BooleanField, IntegerField, DateTimeField
import json
from werkzeug.security import check_password_hash
from flask_login import UserMixin
from app import login_manager
from conf.config import config
import os
import hashlib
import logging; logging.basicConfig(level=logging.INFO)

cfg = config[os.getenv('FLASK_CONFIG') or 'default']

db = MySQLDatabase(host=cfg.DB_HOST, user=cfg.DB_USER, passwd=cfg.DB_PASSWD, database=cfg.DB_DATABASE)


class BaseModel(Model):
    class Meta:
        database = db

# 管理员工号
class User(UserMixin, BaseModel):
    class Meta:
        table_name='tb_user'
    id = IntegerField()  # ID
    name = CharField()  # 用户名
    pwd = CharField()  # 密码
    role_id = IntegerField()  # 角色ID
    enabled = IntegerField()  # 是否可用
    create_time = DateTimeField()  # 创建时间
    update_time = DateTimeField()  # 更新时间

    def verify_password(self, raw_password):
        input_password_md5 = hashlib.md5(raw_password.encode(encoding='UTF-8'))
        return self.pwd==input_password_md5.hexdigest()

# 角色表
class Role(BaseModel):
    class Meta:
        table_name='tb_role'
    id = IntegerField()  # ID
    name = CharField()  # 角色名
    create_time = DateTimeField()  # 创建时间
    update_time = DateTimeField()  # 更新时间

# 菜单表
class Item(BaseModel):
    class Meta:
        table_name='tb_item'
    id = IntegerField()  # ID
    name = CharField()  # 菜单名
    parent_id = IntegerField()  # 父ID
    url = CharField()  # 菜单URL
    create_time = DateTimeField()  # 创建时间
    update_time = DateTimeField()  # 更新时间

# 菜单权限表
class RoleItem(BaseModel):
    class Meta:
        table_name='tb_role_item'
    id = IntegerField()  # ID
    role_name = CharField()  # 角色名
    item_name = CharField()  # 菜单名
    role_id = IntegerField()  # 角色ID
    item_id = IntegerField()  # 菜单ID
    create_time = DateTimeField()  # 创建时间
    update_time = DateTimeField()  # 更新时间

# 用户令牌表
class UserToken(BaseModel):
    class Meta:
        table_name='tb_user_token'
    id = IntegerField()  # ID
    user_id = IntegerField()  # 用户ID
    token = CharField()  # 令牌
    expired_time = DateTimeField()  # 过期时间
    create_time = DateTimeField()  # 创建时间
    update_time = DateTimeField()  # 更新时间

@login_manager.user_loader
def load_user(user_id):
    return User.get(User.id == int(user_id))


# 建表
def create_table():
    db.connect()
    db.create_tables([User])


if __name__ == '__main__':
    create_table()
