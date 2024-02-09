from flask import Flask
from .exts import init_exts
from .views import blue
from datetime import timedelta
import os
def create_app():
    app = Flask(__name__)
    app.register_blueprint(blueprint=blue)
    path = os.path.dirname(os.path.abspath(__file__))
    db_url = 'sqlite:///' + path + '/link.db'
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config["JWT_SECRET_KEY"] = "link"
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=30)  #30分钟后过期
    app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=15)  #15天后刷新令牌过期
    app.config['TRUSTED_PROXIES'] = ['proxy_ip']
    env = os.environ.get('ENV')
    if env == 'development':
        print(f'你现在处于开发环境{env}')
    else:
        print(f'你现在处于部署环境{env}')
    init_exts(app=app) #第三方插件绑定app
    return app
