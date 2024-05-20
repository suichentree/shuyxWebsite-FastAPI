from module_system.entity.sys_user_eneity import SysUserEntity
from config.database_config import mySession

class SysUserDao:

    @classmethod
    def get_user_list(cls,user: SysUserEntity):
        res = mySession.query(SysUserEntity).filter(SysUserEntity.userId == user.userId,SysUserEntity.userName == user.userName).all()
        return res

    @classmethod
    def add_user(cls,user:SysUserEntity):
        mySession.add(user)
        mySession.commit()
        return 1