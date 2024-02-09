from datetime import datetime
from flask import Blueprint,request
from .models import *
import json,requests
from flask_jwt_extended import jwt_required,get_jwt_identity,create_access_token,create_refresh_token
blue = Blueprint('blue',__name__)
def save_ip_address(): # 获取ip地址
    ip_address = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    params = {
        'ip':ip_address,
        'json':'true'
    }
    res = requests.get('https://whois.pconline.com.cn/ipJson.jsp', params=params)
    # print(res.url)
    if res.status_code == 200:
        res_text = res.text
        if res_text:
            js = json.loads(res_text)
            timer =datetime.now().strftime('%Y-%m-%d %H:%M')
            address = js.get('addr')
            login = Login(ip=ip_address,address=address,time=timer)
            try:
                db.session.add(login)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                db.session.flush()
                print('错误信息:'+str(e))
            # print(res_text,type(js))
    print(res.status_code)
@blue.route('/')
def index():
    return '今天天气不错'