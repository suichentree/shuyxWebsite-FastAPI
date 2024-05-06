# 导入sqlalchemy的Base类
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

# 导入sqlalchemy框架中的相关字段
from sqlalchemy import Column, Integer, String ,DateTime,CHAR,func

class SysPosition(Base):
    """
    职位表 sys_position
    """
    __tablename__ = 'sys_position'

    positionId = Column("position_id",Integer, primary_key=True, autoincrement=True, comment='职位ID')
    positionCode = Column("position_code",String(50),unique=True,nullable=False, comment='职位编码')
    positionName = Column("position_name",String(50),unique=True,nullable=False, comment='职位名称')
    status = Column(CHAR(2), default='0', comment='状态 0正常1停用')
    createTime = Column("create_time",DateTime, comment='创建时间', default=func.now())
    updateTime = Column("update_time",DateTime, comment='更新时间', onupdate=func.now(), default=func.now())

