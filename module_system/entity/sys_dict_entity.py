# 导入sqlalchemy的Base类
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

# 导入sqlalchemy框架中的相关字段
from sqlalchemy import Column, Integer, String ,DateTime,CHAR,func

class SysDict(Base):
    """
    字典表 sys_dict
    """
    __tablename__ = 'sys_dict'

    dictId = Column("dict_id",Integer, primary_key=True, autoincrement=True, comment='字典id')
    dictName = Column("dict_name",String(50),unique=True,nullable=False, comment='字典名称')
    dictCode = Column("dict_code",String(20),unique=True,nullable=False, comment='字典编码')
    dictLabel = Column("dict_label",String(20), comment='字典标签')
    dictValue = Column("dict_value",String(20), comment='字典值')
    remark = Column("remark",String(100),comment='备注')
    status = Column(CHAR(2), default='0', comment='状态 0正常1停用')
    createTime = Column("create_time",DateTime, comment='创建时间', default=func.now())
    updateTime = Column("update_time",DateTime, comment='更新时间', onupdate=func.now(), default=func.now())
