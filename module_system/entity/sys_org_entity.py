# 导入sqlalchemy框架中的相关字段
from sqlalchemy import Column, Integer, String ,DateTime,CHAR,func
# 导入sqlalchemy的Base类
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class SysOrg(Base):
    """
    组织机构表 sys_org
    """
    __tablename__ = 'sys_org'

    orgId = Column("org_id",Integer, primary_key=True, autoincrement=True, comment='组织机构ID')
    parentId = Column("parent_id",Integer, comment='上级组织机构id')
    orgName = Column("org_name",String(50),unique=True,nullable=False, comment='组织机构名称')
    orgPath = Column("org_path",String(50),unique=True,nullable=False, comment='组织机构路径')
    status = Column(CHAR(2), default='0', comment='状态 0正常1停用')
    createTime = Column("create_time",DateTime, comment='创建时间', default=func.now())
    updateTime = Column("update_time",DateTime, comment='更新时间', onupdate=func.now(), default=func.now())
