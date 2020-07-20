"""
    :copyright: © 2019 by the Lin team.
    :license: MIT, see LICENSE for more details.
"""

from app.app import create_app
from flask import render_template

app = create_app(environment='development')


@app.route('/', methods=['GET'], strict_slashes=False)
def lin_slogan():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)


@app.after_request
def apply_caching(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Content-Length, Authorization, Accept, X-Requested-With , yourHeaderFeild"
    response.headers["Content-Type"] = "application/json;charset=utf-8"
    return response