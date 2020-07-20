"""
    :copyright: © 2019 by the Lin team.
    :license: MIT, see LICENSE for more details.
"""

from app.app import create_app
from lin.db import db

# app = create_app()
# with app.app_context():
#     with db.auto_commit():
#         # 添加ECS
#         ecs1 = ECS()
#         ecs1.front_host = '121.199.16.79'
#         ecs1.front_host_local = '10.0.0.1'
#         ecs1.memo = '测试机'
#         db.session.add(ecs1)
#
#         ecs2 = ECS()
#         ecs2.front_host = '121.199.12.8'
#         ecs2.front_host_local = '10.0.0.2'
#         ecs2.memo = '测试机2'
#         db.session.add(ecs2)