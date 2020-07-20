"""
    :copyright: © 2019 by the Lin team.
运维管理系统代码逻辑

    :license: MIT, see LICENSE for more details.
"""
from lin.interface import InfoCrud as Base
from sqlalchemy import Column, String, Integer
from lin import db
from sqlalchemy import text


class PlatformUser(Base):
    __tablename__ = 'sys_platform_account'
    rec_id = Column(Integer, primary_key=True, autoincrement=True)
    platform_id = Column(Integer, nullable=False)
    user_account = Column(String(40), nullable=False)
    user_passwd = Column(String(128), nullable=False)
    phone_number = Column(String(128), nullable=False, default='')
    email = Column(String(128), nullable=False, default='')
    remark = Column(String(255), nullable=False, default='')

    #查询指定账户
    @classmethod
    def get_platform_user(cls, data):
        rec_id = data["rec_id"]
        sql = "select * from lin_cms.sys_platform_account where rec_id = (:rec_id)"
        data_query = db.session.execute(text(sql), {'rec_id': rec_id})
        data = {
            'data': {
                'platform_id': system_row['platform_id'],
                'user_account': system_row['user_account'],
                'user_passwd': system_row['user_passwd'],
                'phone_number': system_row['phone_number'],
                'email': system_row['email'],
                'remark': system_row['remark'],
            } for system_row in data_query.fetchall()
        }
        return data

    #查询所有账户
    @classmethod
    def get_all(cls, data):
        platform_id = data["platform_id"] if 'platform_id' in data else None
        user_account = data["user_account"] if 'user_account' in data else None
        remark = data["remark"] if 'remark' in data else None
        pages = int(data["pages"]) if 'pages' in data else None
        counts = int(data["counts"]) if 'counts' in data else None
        if(pages is None or pages < 0 or pages > 100 ):
            pages = 1
        if (counts is None or counts < 0 or counts > 20):
            counts = 10
        sql_data = {}
        sql_data["counts"] = counts
        sql_data["pages"] = (pages - 1) * counts
        sql = "select * from lin_cms.sys_platform_account where true"
        sql_counts = "select count(*) from lin_cms.sys_platform_account where true"
        sql_platform_id = "select * from lin_cms.sys_platform where true"
        if platform_id != '':
            sql = sql + " and platform_id = (:platform_id)"
            sql_counts = sql_counts + " and platform_id = (:platform_id)"
            sql_data["platform_id"] = int(platform_id)
        if user_account != '':
            sql = sql + " and user_account = (:user_account)"
            sql_counts = sql_counts + " and user_account = (:user_account)"
            sql_data["user_account"] = user_account
        if remark != '':
            sql = sql + " and remark like (:remark)"
            sql_counts = sql_counts + " and remark like (:remark)"
            sql_data["remark"] = '%' + remark + '%'
        sql = sql + " limit :pages,:counts"
        data_query_counts = db.session.execute(text(sql_counts), sql_data)
        data_query = db.session.execute(text(sql), sql_data)
        data_query_platform_id = db.session.execute(text(sql_platform_id))
        count = data_query_counts.fetchone()[0]
        data = data_query.fetchall()
        data_platform_id = data_query_platform_id.fetchall()
        res = {
            'data': data,
            'count': count,
            'data_platform_id': data_platform_id
        }
        return res

   # 新增账户
    @classmethod
    def create_platform_user(cls, data):
        #提取参数
        platform_id = data["platform_id"] if 'platform_id' in data else None
        user_account = data["user_account"] if 'user_account' in data else None
        user_passwd = data["user_passwd"] if 'user_passwd' in data else None
        phone_number = data["phone_number"] if 'phone_number' in data else None
        email = data["email"] if 'email' in data else None
        remark = data["remark"] if 'remark' in data else None
        # 对参数进行判断
        if (platform_id is None or platform_id == ""):
            return "平台ID不能为空！"
        if (user_account is None or user_account == ""):
            return "账户名不能为空！"
        if (user_passwd is None or user_passwd == ""):
            return "密码不能为空！"
        if (phone_number is None or phone_number == ""):
            return "手机号不能为空！"
        if (email is None or email == ""):
            return "邮箱不能为空！"
        if (remark is None or remark == ""):
            remark = ""
        sql = "insert into lin_cms.sys_platform_account(platform_id,user_account,user_passwd,phone_number,email,remark)" \
        "values(:platform_id,:user_account,:user_passwd,:phone_number,:email,:remark)"
        db.session.execute(text(sql), {'platform_id': platform_id, 'user_account': user_account, 'user_passwd': user_passwd, 'phone_number': phone_number, 'email': email, 'remark': remark})
        db.session.commit()
        return True

    # 更新
    @classmethod
    def edit_platform_user(cls, data):
        rec_id = data["rec_id"] if 'rec_id' in data else None
        platform_id = data["platform_id"] if 'platform_id' in data else None
        user_account = data["user_account"] if 'user_account' in data else None
        user_passwd = data["user_passwd"] if 'user_passwd' in data else None
        phone_number = data["phone_number"] if 'phone_number' in data else None
        email = data["email"] if 'email' in data else None
        remark = data["remark"] if 'remark' in data else None
        # 对参数进行判断
        if (platform_id is None or platform_id == ""):
            return "平台ID不能为空！"
        if (user_account is None or user_account == ""):
            return "账户名不能为空！"
        if (user_passwd is None or user_passwd == ""):
            return "密码不能为空！"
        if (phone_number is None or phone_number == ""):
            return "手机号不能为空！"
        if (email is None or email == ""):
            return "邮箱不能为空！"
        if (remark is None or remark == ""):
            remark = ""
        sql = "update lin_cms.sys_platform_account set platform_id = (:platform_id), user_account = (:user_account), user_passwd = (:user_passwd), phone_number = (:phone_number), email = (:email), remark = (:remark)" \
        "where rec_id = :rec_id"
        db.session.execute(text(sql), {'rec_id': rec_id, 'platform_id': platform_id, 'user_account': user_account, 'user_passwd': user_passwd, 'phone_number': phone_number, 'email': email, 'remark': remark})
        db.session.commit()
        return True

    # 删除
    @classmethod
    def remove_platform_user(cls, data):
        rec_id = data["rec_id"] if 'rec_id' in data else None
        sql = "delete from lin_cms.sys_platform_account where rec_id= (:rec_id)"
        db.session.execute(text(sql), {'rec_id': rec_id})
        db.session.commit()
        return True
