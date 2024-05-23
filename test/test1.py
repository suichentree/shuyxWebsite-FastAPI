from module_system.dao.sys_user_dao import SysUserDao
from module_system.entity.sys_user_eneity import SysUserEntity
from config.database_config import session_maker

with session_maker() as db:
    res = db.query(SysUserEntity).filter(SysUserEntity.userId == 1).all()
    print("result=", res)


