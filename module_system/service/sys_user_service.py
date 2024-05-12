from module_system.dao.sys_user_dao import SysUserDao
from module_system.dto.sys_user_dto import SysUserDTO
class SysUserService:

    @classmethod
    def get_user_list(cls,dto: SysUserDTO):
        return SysUserDao.get_user_list(dto)
