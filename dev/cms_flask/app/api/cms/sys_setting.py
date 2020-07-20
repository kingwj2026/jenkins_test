"""
    :copyright: © 2019 by the Lin team.
    :license: MIT, see LICENSE for more details.
"""
from flask import request, jsonify, json
from lin import login_required, group_required, route_meta
from app.libs.error_code import Success, Failed
from lin.redprint import Redprint
from app.models.sys_setting import SysSetting

sys_setting_api = Redprint('sys_setting')

#新增系统配置项
@sys_setting_api.route('/create', methods=['POST'])
def create_sys_setting():
    data = request.form.get("data")
    data_Obj = None
    if(data !=None or data != ""):
        data_Obj = json.loads(data)
    SysSetting.create_sys_setting(data_Obj)
    return Success(msg='添加系统配置成功')

#查询全部系统配置列表
@sys_setting_api.route('/get_sys_settings', methods=['POST'])
def get_sys_settings():
    # 获取form参数
    system = request.form.get("data")
    system_Obj = None;
    if (system != None or system != ""):
        system_Obj = json.loads(system)
    # 调用业务代码
    sys_settings = SysSetting.get_sys_settings(system_Obj)

    #返回结果
    return Success(data=sys_settings)

#根据配置项key查找配置信息
@sys_setting_api.route('/select', methods=['POST'])
@login_required
def get_sys_setting():
    data = request.form.get("data")
    data_Obj = None
    if (data != None or data != ""):
        data_Obj = json.loads(data)
    platform = SysSetting.get_sys_setting(data_Obj)

    return Success(data=json.dumps(platform['data']))

#修改配置项信息
@sys_setting_api.route('/edit', methods=['POST'])
@login_required
def edit_sys_setting():
    # 获取form参数
    data = request.form.get("data")
    # print("接收到的参数："+system)
    system_Obj = None;
    if (data != None or data != ""):
        # 转换成dict格式
        system_Obj = json.loads(data)
    ret = SysSetting.edit_sys_setting(system_Obj)
    if (ret == 1 ):
        return Success(msg="修改成功", data=data)
    else:
        return Failed(msg="未进行修改，请确认", data=data);

#禁用系统配置项
@sys_setting_api.route('/disabled', methods=['POST'])
@group_required
def disabled_sys_settting():
    data = request.form.get("data")
    data_Obj = None
    if (data != None or data != ""):
         data_Obj = json.loads(data)
    SysSetting.disabled_sys_settting(data_Obj)
    return Success(msg='禁用成功')






