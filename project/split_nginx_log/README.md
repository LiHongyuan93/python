# Function realization
operation json log & insert into mysql
# Prerequisite
## mysql
Install mysql & create mysql_user,mysql_db,mysql_table
## python
- python 3.0 or above; 
- install pyton module,excute: "pip install mysql"
## log
json format
# Author
Iris <1073378328@qq.com> 2020/04/07
# NOTE
刚刚和领导开会，这个脚本虽然能实现但基本不可行，还有待优化：
1. 用insert插入数据库时，字段多的时候会很繁琐，容易出错，并且每插入一条数据都要关闭一下数据库连接，很浪费资源。
2. 最好是将json用对象的方式进行调用。
3. for循环中时单线程操作，可以优化为多线程。