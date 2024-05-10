# 导入sqlalchemy框架中的相关字段
from sqlalchemy import Column, Integer, String ,DateTime,CHAR,func
# 导入sqlalchemy的Base类
from sqlalchemy.ext.declarative import declarative_base
# 创建基类Base
Base = declarative_base()

class SysRole(Base):
    """
    角色表 sys_role
    """
    __tablename__ = 'sys_role'

    roleId = Column("role_id",Integer, primary_key=True, autoincrement=True, comment='角色ID')
    parentId = Column("parent_id",Integer, comment='上级角色id')
    roleCode = Column("role_code",String(50),unique=True,nullable=False, comment='角色编码')
    roleName = Column("role_name",String(50),unique=True,nullable=False, comment='角色名称')
    status = Column(CHAR(2), default='0', comment='角色状态 0正常1停用')
    createTime = Column("create_time",DateTime, comment='创建时间', default=func.now())
    updateTime = Column("update_time",DateTime, comment='更新时间', onupdate=func.now(), default=func.now())
    

