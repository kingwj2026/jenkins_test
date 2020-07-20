"""
    :copyright: © 2019 by the Lin team.
    :license: MIT, see LICENSE for more details.
    重写APIException，返回值中添加data字段
"""
from flask import json, request
from werkzeug.exceptions import HTTPException
from werkzeug._compat import text_type


class APIException(HTTPException):
    code = 500
    msg = '抱歉，服务器未知错误'
    error_code = 999

    def __init__(self, msg=None, code=None, error_code=None,data=None,
                 headers=None):
        if code:
            self.code = code
        if error_code:
            self.error_code = error_code
        if msg:
            self.msg = msg
        if data:
            self.data = data
        if headers is not None:
            headers_merged = headers.copy()
            headers_merged.update(self.headers)
            self.headers = headers_merged

        super(APIException, self).__init__(msg, None)

    def get_body(self, environ=None):
        body = dict(
            msg=self.msg,
            error_code=self.error_code,
            data = self.data,
            request=request.method + '  ' + self.get_url_no_param()
        )
        text = json.dumps(body)
        return text_type(text)

    @staticmethod
    def get_url_no_param():
        full_path = str(request.full_path)
        main_path = full_path.split('?')
        return main_path[0]

    def get_headers(self, environ=None):
        return [('Content-Type', 'application/json')]

class NotFound(APIException):
    code = 404  # http状态码
    msg = '未找到'  # 异常信息
    data = ''
    error_code = 80010  # 约定的异常码

class BookNotFound(APIException):
    code = 404  # http状态码
    msg = '没有找到相关图书'  # 异常信息
    error_code = 80010  # 约定的异常码

class RefreshException(APIException):
    code = 401
    msg = "refresh token 获取失败"
    error_code = 10100

#成功返回值
class Success(APIException):
    code = 201  # http状态码
    msg = '成功'  # 异常信息
    data = ''
    error_code = 0  # 约定的异常码

class Failed(APIException):
    code = 400   # http状态码
    msg = '失败'   # 异常信息
    data = ''
    error_code = 9999  # 约定的异常码