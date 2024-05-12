from module_system.entity.sys_user_eneity import SysUserEntity
from module_system.dto.sys_user_dto import SysUserDTO
from config.database_config import mySession

class SysUserDao:

    @classmethod
    def get_user_list(cls,user: SysUserDTO):
        ## dto转换为entity
        sys_user_entity = SysUserEntity(**user)
        res = mySession.query(sys_user_entity).first()
        return res

    @classmethod
    def add_user(cls,user:SysUserDTO):
        ## dto转换为entity
        sys_user_entity = SysUserEntity(**user)
        mySession.add(sys_user_entity)
        mySession.commit()
        return 1