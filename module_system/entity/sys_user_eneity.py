# 导入sqlalchemy的Base类
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

# 导入sqlalchemy框架中的相关字段
from sqlalchemy import Column, Integer, String, Date,DateTime, CHAR,func

class SysUser(Base):
    """
    用户表sys_user
    """
    __tablename__ = 'sys_user'

    userId = Column("user_id",Integer, primary_key=True, autoincrement=True, comment='用户ID')
    orgId = Column("org_id",Integer, comment='组织机构ID')
    positionId = Column("position_id",Integer, comment='职位id')
    userName = Column("user_name",String(50),unique=True,nullable=False, comment='用户名称')
    passWord = Column("pass_word",String(50),default='', comment='用户密码')
    gender = Column(CHAR(2),default='0', comment='用户性别 男0女1')
    birthday = Column(Date, comment='生日')
    avatar = Column(String(100), comment='用户头像')
    email = Column(String(50), comment='用户邮箱')
    phone = Column(String(20), comment='手机号码')
    status = Column(CHAR(2), default='0', comment='用户状态 0正常1停用')
    createTime = Column("create_time",DateTime, comment='创建时间', default=func.now())
    updateTime = Column("update_time",DateTime, comment='更新时间', onupdate=func.now(), default=func.now())

