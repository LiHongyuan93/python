#!/usr/bin/python3
# -*- coding: utf-8 -*-

#实现功能：将已json格式的日志转化为字典格式，并逐行读入数据库中
import re
import simplejson as json
import MySQLdb

# 将格式转化为字典
def exchagetoDict(line):
    #line = bytes(line, 'utf-8').decode('unicode_escape')    # change output format
    str = re.sub(r'\\','\\\\',line)        # reslove error :simplejson.errors.JSONDecodeError: Invalid \X escape sequence '\\'
    dict = eval(str)                        # string exchange to dict
    return dict

# 数据库中插入数据
def insertData(dict):
    #print(dict['request_id'],dict['username'],dict['centre'],dict['status'],dict['request_body'],dict['upstr_addr'],dict['remote_addr'],dict['body_bytes_sent'],dict['request_time'],dict['resp_body'],dict['ups_resp_time'],dict['request_uri'],dict['@timestamp'])

    # 打开数据库连接
    db = MySQLdb.connect("localhost", "root", "XXX", "nginx_log", charset='utf8')

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    sql = """INSERT INTO log06
            (request_id,username,centre,status,request_body,upstr_addr,remote_addr,body_bytes_sent,request_time,resp_body,ups_resp_time,request_uri,timestamp) 
            VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')""" % \
            (dict['request_id'],dict['username'],dict['centre'],dict['status'],dict['request_body'],dict['upstr_addr'],dict['remote_addr'],dict['body_bytes_sent'],dict['request_time'],dict['resp_body'],dict['ups_resp_time'],dict['request_uri'],dict['@timestamp'])
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        # Rollback in case there is any error
        db.rollback()
    # 关闭数据库连接
    db.close()

if __name__ == "__main__":
    log_path = '.'
    log_name = 'nginx.json'
    # 遍历json格式的日志文件，将每一行数据转换成字典格式插入到数据库中
    for line in open(log_name):
        dict = exchagetoDict(line)
        insertData(dict)
        print("数据已入库："+str(dict))