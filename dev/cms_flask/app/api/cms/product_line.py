"""
    Likui
"""

# 产品线接口
import json
from app.libs.error_code import Success, Failed
from app.libs.date_encoder import DateEncoder
from app.models.product_line import ProductLine
from lin.jwt import login_required
from lin.redprint import Redprint
from flask import request

product_line_api = Redprint('product_line')

# 查询全部产品线列表
@product_line_api.route('/get_all', methods=['POST','GET'])
@login_required
def get_all():
    # 获取form参数
    system = request.form.get("data")
    print(system)
    system_obj = None
    if(system != None or system != ""):
        # 转换成dict格式
        system_obj = json.loads(system)
    # 调用业务代码
    product_line = ProductLine.get_all(system_obj)
    # 返回结果
    return Success(msg='成功', data=product_line)

# 新增产品线
@product_line_api.route('/create', methods=['POST'])
@login_required
def new_product_line():
    # 获取form参数
    system = request.form.get("data")
    system_obj = None
    if (system != None or system != ""):
        # 转换成dict格式
        system_obj = json.loads(system)
    ProductLine.new_product_line(system_obj)
    return Success(msg='添加账户成功')

# 修改产品线
@product_line_api.route('/edit', methods=['POST'])
@login_required
def edit_product_line():
    system = request.form.get("data")
    system_obj = None
    if (system != None or system != ""):
        system_obj = json.loads(system)
    ProductLine.edit_product_line(system_obj)
    return Success(msg='更新产品线成功')

# 获取某个产品线信息
@product_line_api.route('/select', methods=['POST'])
@login_required
def get_product_line():
    system = request.form.get("data")
    system_obj = None
    if (system != None or system != ""):
        system_obj = json.loads(system)
    product_line = ProductLine.get_product_line(system_obj)
    return Success(data=json.dumps(product_line['data']))
