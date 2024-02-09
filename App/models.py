from .exts import db
# flask db init  初始化
# flask db migrate   数据迁移
# flask db upgrade   改进更新
class User(db.Model):#用户
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, comment="主键ID")
    username = db.Column(db.String(40), unique=False)
    password = db.Column(db.String(40), unique=False)
    name = db.Column(db.String(40), unique=False)
class Login(db.Model):#登录记录
    __tablename__ = 'login'
    id = db.Column(db.Integer, primary_key=True, comment="主键ID")
    ip = db.Column(db.String(40), unique=False) #ip
    address = db.Column(db.Text, unique=False) #地址
    time = db.Column(db.Text, unique=False) #时间
def create_db():
    db.create_all() # 创建所有表
    # print('创建')
    if User.query.count() == 0: # 如果用户表为空
        print('初始化用户表')
        user = User(username='admin',password='21232f297a57a5a743894a0e4a801fc3',name='管理员')
        try:
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            db.session.flush()
            print('错误信息:'+str(e))