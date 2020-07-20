"""
    :copyright: © 2019 by the Lin team.
    :license: MIT, see LICENSE for more details.
"""
from flask import request, jsonify, json
from lin import login_required, group_required, route_meta
from app.libs.error_code import Success, Failed
from lin.redprint import Redprint
from app.models.platform import Platform

platform_api = Redprint('platform')

#查询全部机器列表
@platform_api.route('/get_all', methods=['POST'])
@login_required
def get_platforms():
    # 获取form参数
    system = request.form.get("data")
    system_Obj = None;
    if (system != None or system != ""):
        system_Obj = json.loads(system)
    # 调用业务代码
    platforms = Platform.get_all_platforms(system_Obj)

    #返回结果
    return Success(data=platforms)
#根据平台id查询某个平台
@platform_api.route('/select', methods=['POST'])
@login_required
def get_platform():
    data = request.form.get("data")
    data_Obj = None
    if (data != None or data != ""):
        data_Obj = json.loads(data)
    platform = Platform.get_platform(data_Obj)

    return Success(data=json.dumps(platform['data']))

#

#根据备注查询平台信息
@platform_api.route('/search_remark', methods=['POST'])
@login_required
def get_search():
    system = request.form.get("data")
    system_Obj = None;
    if (system != None or system != ""):
        system_Obj = json.loads(system)
    remark = Platform.get_remark(system_Obj)
    return Success(msg='查找成功', data=remark['data'])

#新增平台信息
@platform_api.route('/create', methods=['POST'])
@login_required
def create_platform():
    data = request.form.get("data")
    data_Obj = None
    if(data !=None or data != ""):
        data_Obj = json.loads(data)
    Platform.create_platform(data_Obj)
    return Success(msg='添加平台信息成功')


#修改平台信息
@platform_api.route('/edit', methods=['POST'])
@login_required
def edit_platform():
    # 获取form参数
    data = request.form.get("data")
    # print("接收到的参数："+system)
    system_Obj = None;
    if (data != None or data != ""):
        # 转换成dict格式
        system_Obj = json.loads(data)
    ret = Platform.edit_platform(system_Obj)
    if (ret == 1 ):
        return Success(msg="修改成功", data=data)
    else:
        return Failed(msg="未进行修改，请确认", data=data);


#删除平台信息
@platform_api.route('/delect', methods=['POST'])
@group_required
def delect_platform():
    data = request.form.get("data")
    data_Obj = None
    if (data != None or data != ""):
         data_Obj = json.loads(data)
    Platform.delect_platform(data_Obj)
    return Success(msg='删除成功')