"""
这是一个创表脚本。执行该脚本会自动在对应数据库中创建表。
前提：
1. 所有表的orm模型需要提前创建好，然后导入到这里。
2. 只有当数据库中不存在表的时候，才会自动创建表。否则无动作

"""

# 导入配置类的配置
from database_config import myEngine
# 导入各个表的基类
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
