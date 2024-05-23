from module_system.entity.sys_user_eneity import SysUserEntity
from module_system.dto.sys_user_dto import SysUserDTO
from config.database_config import session_maker

class SysUserDao:

    @classmethod
    def get_user_list(cls,user: SysUserDTO):
        with session_maker() as db_session:
            res = db_session.query(SysUserEntity).filter(SysUserEntity.userId == user.userId,SysUserEntity.userName == user.userName).all()
            print("result=", res)
            return res

    @classmethod
    def update_user(cls, user: SysUserDTO):
        with session_maker() as db_session:
            res = db_session.query(SysUserEntity).filter(SysUserEntity.userId == user.userId).update({'name': 'jack1'})
            print("result=", res)
            return res

    @classmethod
    def delete_user_by_id(cls,user: SysUserDTO):
        with session_maker() as db_session:
            res = db_session.query(SysUserEntity).filter(SysUserEntity.id == user.userId).delete()
            print("result=", res)
            return res

    @classmethod
    def add_user(cls,user:SysUserDTO):
        with session_maker() as db_session:
            one = SysUserEntity(**user)
            res = db_session.add(one)
            print("result=", res)
            return res
