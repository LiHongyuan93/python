import json
import logging;
from flask import request, Response
from app.api import auth
from app.util import Utils

logging.basicConfig(level=logging.INFO)

# 测试
@auth.route('/auth/a', methods=['GET', 'POST'])
def test():
    # header_name=request.headers.get('name',default="empty")
    # form_name=request.form.get('name',default="empty")
    # args_name=request.args.get('name',default="empty")
    # data=request.get_data()
    # data = json.loads(data)
    # json_name = data['name']
    #
    # logging.info("header_name:"+header_name)
    # logging.info("form_name:"+form_name)
    # logging.info("args_name:"+args_name)
    # logging.info("json_name:"+json_name)
    #return Response('<h1>Hello World!</h2>', status=200, mimetype='text/html')
    a= Utils.resp_failure("用户名密码错误")
    return a
