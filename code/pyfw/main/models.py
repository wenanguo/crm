from lib2to3.pytree import Base

from flask_login import UserMixin, AnonymousUserMixin
from sqlalchemy import Table, Column, Integer, ForeignKey
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

from datetime import datetime
from flask import current_app, request, url_for

from pyfw import db, login_manager

#用户角色多对多关系表
user_role_mapper = db.Table('user_role_mapper',
                         db.Column('user_id', db.Integer, db.ForeignKey('common_user_info.id') , nullable=False, primary_key=True),
                         db.Column('role_id', db.Integer, db.ForeignKey('common_role_info.id') , nullable=False, primary_key=True)
                         )


class CommonUserInfo(UserMixin,db.Model):
    """
    用户表
    """
    __tablename__ = 'common_user_info'
    id = db.Column(db.Integer, primary_key=True)
    #账户
    login_account = db.Column(db.String(64),unique=True)
    #密码
    login_password = db.Column(db.String(128))

    # 真实名称
    user_name = db.Column(db.String(64))
    # 用户编号
    user_no = db.Column(db.String(64))
    # 账号状态
    user_status=db.Column(db.Integer)
    # 所属系统
    user_sys = db.Column(db.Integer)
    # 手机号码
    user_phone = db.Column(db.String(64))
    # 邮箱
    user_email = db.Column(db.String(64))
    # 用户性别（1:男性，0:女性）
    user_sex = db.Column(db.Integer)
    # 用户分类（1：内部人员；2：外部人员）
    user_type=db.Column(db.Integer)
    # 备注
    user_remark = db.Column(db.String(64))

    #所属组织机构
    user_org = db.Column(db.Integer)


    roles = db.relationship('CommonRoleInfo',
                              secondary=user_role_mapper,
                              lazy='dynamic')

    #extend
    # 头像
    icon = db.Column(db.String(64))

    #最后登录时间
    last_login=db.Column(db.DateTime(), default=datetime.utcnow)

    #用户状态
    status = db.Column(db.Integer)
    #操作人
    operate_user_id=db.Column(db.Integer)
    #操作时间
    operate_time = db.Column(db.DateTime(), default=datetime.utcnow)


    def __repr__(self):
        return '<common_user_info %r>' % self.login_account

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.login_password = generate_password_hash(password)

    def verify_password(self, password):
        """
        密码验证方法
        :param password: 需要验证的密码
        :return:
        """
        return check_password_hash(self.login_password, password)

    @login_manager.user_loader
    def load_user(user_id):
        return CommonUserInfo.query.get(int(user_id))

    def to_json(self):
        json = {
            'id': self.id,
            'login_account': self.login_account,
            'login_password': self.login_password,
            'user_name':self.user_name,
            'user_no':self.user_no,
            'user_status':self.user_status,
            'user_sys':self.user_sys,
            'user_phone': self.user_phone,
            'user_email': self.user_email,
            'user_sex': self.user_sex,
            'user_type': self.user_type,
            'user_remark': self.user_remark,
            'user_org': self.user_org,
            'last_login': self.last_login,
            'status': self.status,
            'operate_user_id': self.operate_user_id,
            'operate_time': self.operate_time
        }

        return json

    @staticmethod
    def generate_fake(count=100):
        from sqlalchemy.exc import IntegrityError

        from random import seed
        import forgery_py
        seed()
        for i in range(count):
            u = CommonUserInfo(user_email=forgery_py.internet.email_address(),
                               login_account=forgery_py.internet.user_name(True),
                                password=forgery_py.lorem_ipsum.word(),
                               icon="images/2.jpg"
                                )
            db.session.add(u)
            try:
                db.session.commit()
            except IntegrityError:
                db.session.rollback()






class CommonRoleInfo(db.Model):
    """
        角色表
    """
    __tablename__ = 'common_role_info'
    id = db.Column(db.Integer, primary_key=True)
    #角色代码
    role_code = db.Column(db.String(64), unique=True)
    #角色名称
    role_name = db.Column(db.String(64), unique=True)
    #角色顺序
    role_order=db.Column(db.Integer)
    #备注
    role_remark=db.Column(db.Text)
    # 用户状态
    status = db.Column(db.Integer)
    # 操作人
    operate_user_id = db.Column(db.Integer)
    # 操作时间
    operate_time = db.Column(db.DateTime(), default=datetime.utcnow)



    def __repr__(self):
        return '<common_role_info %r>' % self.role_name





class CommonOrgInfo(db.Model):
    """
        组织机构表
    """
    __tablename__ = 'common_org_info'
    id = db.Column(db.Integer, primary_key=True)
    #组织机构代码
    org_code = db.Column(db.String(64), unique=True)
    #组织机构全称
    org_fullname = db.Column(db.String(64), unique=True)
    # 组织机构名称
    org_name = db.Column(db.String(64), unique=True)

    #顺序
    org_order=db.Column(db.Integer)
    #父节点编号
    org_pid = db.Column(db.Integer)

    #备注
    role_remark=db.Column(db.Text)

    # 状态
    status = db.Column(db.Integer)
    # 操作人
    operate_user_id = db.Column(db.Integer)
    # 操作时间
    operate_time = db.Column(db.DateTime(), default=datetime.utcnow)





    def __repr__(self):
        return '<common_org_info %r>' % self.role_name





class CommonMenuInfo(db.Model):
    """
        菜单表
    """
    __tablename__ = 'common_menu_info'
    id = db.Column(db.Integer, primary_key=True)
    #菜单样式
    menu_cls = db.Column(db.String(64), unique=True)
    #菜单代码
    menu_code = db.Column(db.String(64), unique=True)

    #菜单级别
    menu_level=db.Column(db.Integer)
    #菜单名称
    menu_name=db.Column(db.String(64))
    #菜单导航
    menu_nav=db.Column(db.String(64))
    #菜单排序
    menu_order=db.Column(db.Integer)
    #父节点
    menu_pid=db.Column(db.String(64))
    #备注
    menu_remark=db.Column(db.String(64))
    #所属系统
    menu_sysid=db.Column(db.String(64))
    #类别
    menu_type=db.Column(db.Integer)
    #url
    menu_url=db.Column(db.String(64))

    # 状态
    status = db.Column(db.Integer)
    # 操作人
    operate_user_id = db.Column(db.Integer)
    # 操作时间
    operate_time = db.Column(db.DateTime(), default=datetime.utcnow)



    def __repr__(self):
        return '<common_org_info %r>' % self.role_name
