from sqlalchemy import Column, String, Integer
from sqlalchemy import text
from lin.interface import InfoCrud as Base
from lin import db



class SysSetting(Base):
    # 定表名和表结构,注意，数据库里面会比这里多三个字段
    # modified      timestamp    default CURRENT_TIMESTAMP not null on update CURRENT_TIMESTAMP,
    #
    __tablename__ = 'sys_setting';
    set_key = Column(String(64), primary_key=True)
    set_value = Column(String(256), nullable=False)
    set_name = Column(String(40), nullable=False)
    log_type = Column(Integer, nullable=False)
    value_type = Column(Integer, nullable=False)
    value_desc = Column(String(255), nullable=False)
    is_disable = Column(Integer, nullable=False)

    # 新增系统配置项
    @classmethod
    def create_sys_setting(cls, data):
        # 提取参数
        data = data['info']
        set_key = data['set_key'] if 'set_key' in data else None;
        set_value = data['set_value'] if 'set_value' in data else None;
        set_name = data['set_name'] if 'set_name' in data else None;
        log_type = data['log_type'] if 'log_type' in data else None;
        value_type = data['value_type'] if 'value_type' in data else None;
        value_desc = data['value_desc'] if 'value_desc' in data else None;
        is_disable = data['is_disable'] if 'is_disable' in data else None;

        # 对参数进行判断
        if (set_key is None or set_key == ""):
            return "系统配置key不能为空！"

        if (set_value is None or set_value == ""):
            return "系统配置值不能为空！"

        if (set_name is None or set_name == ""):
            return "系统配置名称不能为空！"

        if (value_desc is None or value_desc == ""):
            return "系统配置说明不能为空！"


        if (log_type is None):
            log_type = 5;

        if (value_type is None):
            value_type = 0;

        if (is_disable is None):
            is_disable = 0;


        # 生成sql
        sql = "insert into sys_setting(set_key, set_value, set_name, log_type, value_type, value_desc, is_disable) " \
              "values(:set_key,:set_value,:set_name,:log_type,:value_type,:value_desc,:is_disable)"
        # 拼接sql参数并执行
        db.session.execute(text(sql), {'set_key': set_key, 'set_value': set_value, 'set_name': set_name,
                                       'log_type': log_type, 'value_type': value_type, 'value_desc': value_desc,
                                       'is_disable':is_disable})
        db.session.commit()

        return ""

    # 查询所有的平台列表
    @classmethod
    def get_sys_settings(cls, args):
        # 提取参数
        set_key = args['set_key'];
        set_name = args['set_name'];
        value_desc = args['value_desc'];

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
        sql = "select * from sys_setting where true "
        sql_count = "select count(*) from sys_setting where true "
        if (set_name != ""):
            sql_params['set_name'] = '%' + set_name + '%'
            sql = sql + " and set_name like :set_name "
            sql_count += " and set_name like :set_name "
        if (set_key != ""):
            sql_params['set_key'] = set_key
            sql = sql + " and set_key = :set_key "
            sql_count += " and set_key = :set_key "

        if (value_desc != ""):
            sql_params['value_desc'] = '%' + value_desc + '%'
            sql = sql + " and value_desc like :value_desc "
            sql_count += " and value_desc like :value_desc "

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

    # 根据配置项key查询配置项信息
    @classmethod
    def get_sys_setting(cls, data_Obj):
        #提取参数
        set_key = data_Obj['set_key']
        # 生成sql
        sql = "select * from sys_setting where set_key = (:set_key)"
        # 拼接sql参数并执行
        data_query = db.session.execute(text(sql), {'set_key': set_key})

        # 转换查询结果
        data = {
            'data': {
                'set_key': system_row['set_key'],
                'set_value': system_row['set_value'],
                'set_name': system_row['set_name'],
                'log_type': system_row['log_type'],
                'value_type': system_row['value_type'],
                'value_desc': system_row['value_desc'],
                'is_disable': system_row['is_disable'],
            } for system_row in data_query.fetchall()
        }
        return data

    @classmethod
    def edit_sys_setting(cls, data):
        # 提取参数
        set_key = data['set_key'] if 'set_key' in data else None;
        set_value = data['set_value'] if 'set_value' in data else None;
        set_name = data['set_name'] if 'set_name' in data else None;
        log_type = data['log_type'] if 'log_type' in data else None;
        value_type = data['value_type'] if 'value_type' in data else None;
        value_desc = data['value_desc'] if 'value_desc' in data else None;
        is_disable = data['is_disable'] if 'is_disable' in data else None;

        # 对参数进行判断

        if (set_value is None or set_value == ""):
            return "系统配置值不能为空！"

        if (set_name is None or set_name == ""):
            return "系统配置名称不能为空！"

        if (value_desc is None or value_desc == ""):
            return "系统配置说明不能为空！"

        if (is_disable is None or is_disable == ""):
            return "是否停用不能为空！"


        if (log_type is None):
            log_type = 5;

        if (value_type is None):
            value_type = 0;

        # 生成sql
        sql = "update sys_setting set  set_value = (:set_value), set_name = (:set_name), log_type = (:log_type), " \
              "value_type = :value_type, value_desc = :value_desc, is_disable = :is_disable where set_key = (:set_key)"

        # 拼接sql参数并执行
        data_query = db.session.execute(text(sql), {'set_value': set_value, 'set_name': set_name,
                                                    'log_type': log_type, 'value_type': value_type,
                                                    'value_desc':value_desc, 'is_disable':is_disable,
                                                    'set_key':set_key})
        db.session.commit()
        #return ""
        return data_query.rowcount

    # 禁用系统配置项
    @classmethod
    def disabled_sys_settting(cls, data):
        set_key = data["set_key"] if 'set_key' in data else None;
        is_disable = data["is_disable"] if 'is_disable' in data else None;

        if (is_disable == '否'):
            is_disable = 1;

        sql = "update sys_setting set is_disable = :is_disable  where set_key = (:set_key)"
        db.session.execute(text(sql), {'set_key': set_key, 'is_disable': is_disable})
        db.session.commit()
        return True




