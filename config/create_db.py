from database_config import myEngine

from module_system.entity.sys_org_entity import Base as Base1
from module_system.entity.sys_dict_entity import Base as Base2
from module_system.entity.sys_menu_entity import Base as Base3
from module_system.entity.sys_user_eneity import Base as Base4
from module_system.entity.sys_role_eneity import Base as Base5
from module_system.entity.sys_position_eneity import Base as Base6

# 单独运行该文件的时候，会创建数据库
if __name__ == "__main__":
    Base1.metadata.create_all(myEngine)
    Base2.metadata.create_all(myEngine)
    Base3.metadata.create_all(myEngine)
    Base4.metadata.create_all(myEngine)
    Base5.metadata.create_all(myEngine)
    Base6.metadata.create_all(myEngine)
