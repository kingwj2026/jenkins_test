from sqlalchemy import Column, String, Integer
from sqlalchemy import text
from lin.interface import InfoCrud as Base
from lin import db

# 产品线实体类,内部操作数据库
class ProductLine(Base):
    __tablename__ = 'sys_huice_system'
    # 自增主键
    rec_id = Column(Integer, primary_key=True, autoincrement=True, comment="自增主键")
    # 产品线编号
    system_no = Column(String(40), nullable=False, comment="产品线编号")
    # 产品线名称
    system_name = Column(String(255), nullable=False, comment="产品线名称")
    # 产品线负责人
    principal_user = Column(Integer, nullable=False, comment="产品线负责人")
    # 产品线负责团队
    principal_team = Column(String(40), nullable=False, comment="产品线负责团队")
    # 是否停用
    is_disable = Column(String(40), nullable=False, comment="是否停用")
    # 备注
    remark = Column(String(40), nullable=False, comment="备注")

    #查询指定产品线
    @classmethod
    def get_platform_user(cls, data):
        rec_id = data["rec_id"]
        sql = "select * from lin_cms.sys_huice_system where rec_id = (:rec_id)"
        data_query = db.session.execute(text(sql), {'rec_id': rec_id})
        data = {
            'data': {
                'system_no': system_row['system_no'],
                'system_name': system_row['system_name'],
                'principal_user': system_row['principal_user'],
                'principal_team': system_row['principal_team'],
                'is_disable': system_row['is_disable'],
                'remark': system_row['remark'],
            } for system_row in data_query.fetchall()
        }
        return data

    # 获取全部产品线,支持查询条件
    @classmethod
    def get_all(cls, data):
        system_no = data["system_no"] if 'system_no' in data else None
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
        sql = "select * from lin_cms.sys_huice_system where true"
        sql_counts = "select count(*) from lin_cms.sys_huice_system where true"
        sql_system_no = "select * from lin_cms.sys_huice_system where true"
        if system_no != '':
            sql = sql + " and system_no = (:system_no)"
            sql_counts = sql_counts + " and system_no = (:system_no)"
            sql_data["system_no"] = int(system_no)
        if remark != '':
            sql = sql + " and remark like (:remark)"
            sql_counts = sql_counts + " and remark like (:remark)"
            sql_data["remark"] = '%' + remark + '%'
        sql = sql + " limit :pages,:counts"
        data_query_counts = db.session.execute(text(sql_counts), sql_data)
        data_query = db.session.execute(text(sql), sql_data)
        data_query_system_no = db.session.execute(text(sql_system_no))
        count = data_query_counts.fetchone()[0]
        data = data_query.fetchall()
        data_system_no = data_query_system_no.fetchall()
        res = {
            'data': data,
            'count': count,
            'data_system_no': data_system_no,
        }
        return res

    # 新增产品线
    @classmethod
    def new_product_line(cls, data):

        # 提取参数
        system_no = data['system_no'] if 'system_no' in data else None
        system_name = data['system_name'] if 'system_name' in data else None
        principal_user = data['principal_user'] if 'principal_user' in data else None
        principal_team = data['principal_team'] if 'principal_team' in data else None
        is_disable = data['is_disable'] if 'is_disable' in data else None
        remark = data['remark'] if 'remark' in data else None

        # 对参数进行判断
        if (system_no is None or system_no == ""):
            return "产品线编号不能为空！"
        if (system_name is None or system_name == ""):
            return "产品名称不能为空！"
        if (principal_user is None or principal_user == ""):
            return "产品线负责人不能为空！"
        if (principal_team is None or principal_team == ""):
            return "产品线负责团队不能为空！"
        if (is_disable is None):
            is_disable = 0
        if (remark is None ):
            remark = ""

        # 生成sql
        sql = "insert into sys_huice_system(system_no,system_name,principal_user,principal_team,is_disable,remark)" \
        "values(:system_no,:system_name,:principal_user,:principal_team,:is_disable,:remark)"
        # 拼接sql参数并执行
        db.session.execute(text(sql), {'system_no': system_no, 'system_name': system_name, 'principal_user': principal_user, 'principal_team': principal_team, 'is_disable': is_disable, 'remark': remark})
        db.session.commit()
        return True

    #修改某个产品线
    @classmethod
    def edit_product_line(cls, data):
        rec_id = data["rec_id"] if 'rec_id' in data else None
        system_no = data['system_no'] if 'system_no' in data else None
        system_name = data['system_name'] if 'system_name' in data else None
        principal_user = data['principal_user'] if 'principal_user' in data else None
        principal_team = data['principal_team'] if 'principal_team' in data else None
        is_disable = data['is_disable'] if 'is_disable' in data else None
        remark = data['remark'] if 'remark' in data else None
        # 对参数进行判断
        if (system_no is None or system_no == ""):
            return "产品线编号不能为空！"
        if (system_name is None or system_name == ""):
            return "产品名称不能为空！"
        if (principal_user is None or principal_user == ""):
            return "产品线负责人不能为空！"
        if (principal_team is None or principal_team == ""):
            return "产品线负责团队不能为空！"
        if (is_disable is None):
            is_disable = 0
        if (remark is None ):
            remark = ""
        sql = "update sys_huice_system set system_no = (:system_no), system_name = (:system_name), principal_user = (:principal_user), principal_team = (:principal_team), is_disable = (:is_disable), remark = (:remark)" \
        "where rec_id = :rec_id"
        db.session.execute(text(sql), {'rec_id': rec_id, 'system_no': system_no, 'system_name': system_name, 'principal_user': principal_user, 'principal_team': principal_team, 'is_disable': is_disable, 'remark': remark})
        db.session.commit()
        return True