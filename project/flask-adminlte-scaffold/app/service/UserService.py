import datetime
import time

from app.models import User, Role, UserToken
import logging;
from app.util.PageUtil import PageUtil

logging.basicConfig(level=logging.INFO)


# 根据令牌获取用户信息
def get_user_by_token(token):
    if token == None or token == '':
        raise Exception(msg='token不能为空')
    user_token = UserToken.get_or_none(UserToken.token == token)
    if user_token == None:
        raise Exception(msg='token不存在')
    delta = user_token.expired_time - datetime.datetime.now()
    if delta.days < 0:
        raise Exception(msg='token已过期')
    user = User().get_by_id(user_token.user_id)
    if user == None:
        raise Exception(msg='用户已被删除')
    return user


def find_user_by_name_role_page(name, role_id, current_page):
    # 每页显示的条数
    num_of_one_page = 10
    # 查询条件
    where_condition = build_query_user_condition(name, role_id)
    # 符合的条数
    allCount = User.select().where(*where_condition).count()
    # 查询时偏移的数据量
    off_set = (int(current_page) - 1) * num_of_one_page
    # 本页的数据
    user_list = User.select().order_by(User.update_time.desc()).where(*where_condition).offset(off_set).limit(
        num_of_one_page)
    # 遍历放入数组
    users = []
    for user in user_list:
        users.append(user)
    # 分页信息
    page_util = PageUtil()
    totalPage, firstRecord, lastRecord = page_util.get_current_page_info(current_page, num_of_one_page, allCount)
    return {'records': users, 'totalPage': totalPage, 'currentPage': current_page, 'allCount': allCount}


# 生成动态SQL
def build_query_user_condition(name, role_id):
    where_condition = []
    if name != None and name.strip() != '':
        like_value = '%' + name + '%'
        where_condition.append(User.name % like_value)
    if role_id != None and role_id.strip() != '' and role_id != -1:
        where_condition.append(User.role_id == role_id)
    if len(where_condition) >= 1:
        return where_condition
    return (None,)
