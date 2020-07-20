from sqlalchemy import Column, String, Integer
from sqlalchemy import text
from lin.interface import InfoCrud as Base
from lin import db



class Platform(Base):
    # 定表名和表结构,注意，数据库里面会比这里多三个字段
    # modified      timestamp    default CURRENT_TIMESTAMP not null on update CURRENT_TIMESTAMP,
    #
    __tablename__ = 'sys_platform';
    rec_id = Column(Integer, primary_key=True, autoincrement=True)
    platform_name = Column(String(40), nullable=False)
    remark = Column(String(255), nullable=False)
    is_disable = Column(Integer, nullable=False)

    # 新增机器
    @classmethod
    def create_platform(cls, data):
        # 提取参数
        data = data['info']
        platform_name = data['platform_name'] if 'platform_name' in data else None;
        remark = data['remark'] if 'remark' in data else None;
        is_disable = data['is_disable'] if 'is_disable' in data else None;

        # 对参数进行判断
        if (platform_name is None or platform_name == ""):
            return "平台名不能为空！"

        if (is_disable is None):
            is_disable = 0;

        if (remark is None):
            remark = "";

        # 生成sql
        sql = "insert into sys_platform(platform_name, is_disable, remark) " \
              "values(:platform_name,:is_disable,:remark)"
        # 拼接sql参数并执行
        db.session.execute(text(sql), {'platform_name': platform_name, 'is_disable': is_disable, 'remark': remark})
        db.session.commit()

        return ""

    # 查询所有的平台列表
    @classmethod
    def get_all_platforms(cls, args):
        # 提取参数
        remark = args['search_remark'];
        platform_name = args['search_platform_name'];

        # 提取参数
        pages = args['pages'];
        counts = args['counts'];

        # 对参数进行判断
        if (pages == "" or pages < 0 or pages > 100):
            pages = 1

        if (counts == "" or counts < 0 or counts > 20):
            counts = 10

        #sql参数列表
        sql_params = {}
        #动态拼接sql
        sql = "select * from sys_platform where true "
        sql_count = "select count(*) from sys_platform where true "
        if (remark != ""):
            sql_params['search_remark'] = '%' + remark + '%'
            sql = sql + " and remark like :search_remark "
            sql_count += " and remark like :search_remark "
        if (platform_name != ""):
            sql_params['search_platform_name'] = platform_name
            sql = sql + " and platform_name = :search_platform_name "
            sql_count += " and platform_name = :search_platform_name "

        sql_params['counts'] = counts
        sql_params['pages'] = (pages-1) * counts
        sql = sql + " limit :pages, :counts "

        # 执行sql
        data_query = db.session.execute(text(sql), sql_params)
        res = data_query.fetchall()
        counts_query = db.session.execute(text(sql_count), sql_params)
        total = counts_query.fetchone()[0]

        # 转换查询结果
        data = {
            'data': res,
            'total': total
        }
        return data

    # 根据id查询某一个平台
    @classmethod
    def get_platform(cls, data_Obj):
        #提取参数
        rec_id = data_Obj['rec_id']
        # 生成sql
        sql = "select * from sys_platform where rec_id = (:rec_id)"
        # 拼接sql参数并执行
        data_query = db.session.execute(text(sql), {'rec_id': rec_id})

        # 转换查询结果
        data = {
            'data': {
                'rec_id': system_row['rec_id'],
                'platform_name': system_row['platform_name'],
                'remark': system_row['remark'],
                'is_disable': system_row['is_disable'],
            } for system_row in data_query.fetchall()
        }
        return data

    # 按照备注查询
    @classmethod
    def search(cls, data):
        platform_name = data["platform_name"] if 'platform_name' in data else None;
        remark = data["remark"] if 'remark' in data else None;

        sql = "select * from sys_platform where platform_name =  (:platform_name) and remark like (:remark) "
        data_query = db.session.execute(text(sql), {'platform_name': platform_name, 'remark': remark})
        data = {
            'data': {
                'rec_id': system_row['rec_id'],
                'platform_name': system_row['platform_name'],
                'remark': system_row['remark'],
                'is_disable': system_row['is_disable'],
            } for system_row in data_query.fetchall()
        }
        return data

    # 编辑平台信息
    @classmethod
    def edit_platform(cls, data):
        # 提取参数
        platform_name = data['platform_name'] if 'platform_name' in data else None;
        remark = data['remark'] if 'remark' in data else None;
        is_disable = data['is_disable'] if 'is_disable' in data else None;
        rec_id = data['rec_id'] if 'rec_id' in data else None;

        # 对参数进行判断
        if (platform_name is None or platform_name == ""):
            return "平台名不能为空！"
        if (is_disable is None):
            is_disable = 0;
        if (remark is None):
            remark = "";
        if (rec_id is None):
            rec_id = data['rec_id']

        # 生成sql
        sql = "update sys_platform set  platform_name = (:platform_name), remark = (:remark), is_disable = (:is_disable)" \
              "where rec_id = (:rec_id)"
        # 拼接sql参数并执行
        data_query = db.session.execute(text(sql), {'platform_name': platform_name, 'is_disable': is_disable,
                                                    'remark': remark, 'rec_id': rec_id})
        print(data_query.rowcount)
        print("1111111")
        db.session.commit()
        #return ""

        print(dir(data_query))

        return data_query.rowcount

    # 删除平台
    @classmethod
    def delect_platform(cls, data):
        rec_id = data["rec_id"] if 'rec_id' in data else None;
        sql = "delete from lin_cms.sys_platform where rec_id = (:rec_id)"
        db.session.execute(text(sql), {'rec_id': rec_id})
        db.session.commit()
        return True
