# 导入sqlalchemy框架中的相关字段
from sqlalchemy import Column, Integer, String ,DateTime,CHAR,func
# 导入sqlalchemy的Base类
from sqlalchemy.ext.declarative import declarative_base
# 创建基类Base
Base = declarative_base()

class SysMenu(Base):
    """
    菜单表 sys_menu
    """
    __tablename__ = 'sys_menu'

    menuId = Column("menu_id",Integer, primary_key=True, autoincrement=True, comment='菜单id')
    parentId = Column("parent_id",Integer, comment='上级菜单id')
    menuName = Column("menu_name",String(50),unique=True,nullable=False, comment='菜单名称')
    menuPath = Column("menu_path",String(50),comment='菜单路径')
    menuPage = Column("menu_page",String(50),comment='菜单页面')
    icon = Column("icon",String(50),comment='菜单图标')
    menuType = Column("menu_type",CHAR(2),default="1",comment='菜单类型 0目录 1菜单')
    visible = Column(CHAR(2),default="0",comment='菜单是否侧边栏可见（0可见1不可见）')
    isLink = Column("is_link",CHAR(2),default="0",comment='菜单是否是外链（0是1不是）')
    status = Column(CHAR(2), default='0', comment='状态 0正常1停用')
    createTime = Column("create_time",DateTime, comment='创建时间', default=func.now())
    updateTime = Column("update_time",DateTime, comment='更新时间', onupdate=func.now(), default=func.now())
