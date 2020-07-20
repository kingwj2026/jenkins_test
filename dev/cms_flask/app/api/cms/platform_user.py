from lin import group_required
from app.models.platform_user import PlatformUser

from lin.core import route_meta
from lin.jwt import login_required
from lin.redprint import Redprint
from flask import request
import json
from app.libs.error_code import Success, Failed

platform_user_api = Redprint('platform_user') #创建host红图

#指定查找
@platform_user_api.route('/select', methods=['POST'])
@login_required
def get_platform_user():
    system = request.form.get("data")
    system_obj = None
    if (system != None or system != ""):
        system_obj = json.loads(system)
    platform_user = PlatformUser.get_platform_user(system_obj)
    return Success(data=json.dumps(platform_user['data']))

#查询所有
@platform_user_api.route('/get_all', methods=['POST','GET'])
@login_required
def get_all():
    system = request.form.get("data")
    system_obj = None
    if (system != None or system != ""):
        system_obj = json.loads(system)
    platform_user = PlatformUser.get_all(system_obj)
    return Success(msg='成功', data=platform_user)

#新增
@platform_user_api.route('/create', methods=['POST'])
@group_required
def create_platform_user():
    system = request.form.get("data")
    system_obj = None
    if(system !=None or system != ""):
        system_obj = json.loads(system)
    PlatformUser.create_platform_user(system_obj)
    return Success(msg='添加账户成功')

#更新
@platform_user_api.route('/edit', methods=['POST'])
@group_required
def edit_platform_user():
    system = request.form.get("data")
    system_obj = None
    if (system != None or system != ""):
        system_obj = json.loads(system)
    PlatformUser.edit_platform_user(system_obj)
    return Success(msg='更新账户成功')

#删除
@platform_user_api.route('/remove', methods=['POST'])
@route_meta(auth='删除账户', module='HOST')
@group_required
def remove_platform_user():
    system = request.form.get("data")
    system_obj = None
    if (system != None or system != ""):
        system_obj = json.loads(system)
    PlatformUser.remove_platform_user(system_obj)
    return Success(msg='删除账户成功')
