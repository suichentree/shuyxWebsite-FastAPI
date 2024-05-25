from module_system.dao.sys_user_dao import SysUserDao
from module_system.dto.sys_user_dto import SysUserDTO
class SysUserService:
    @classmethod
    def get_user_list(cls,pageSize:int,pageNum:int):
        return SysUserDao.get_user_list(pageSize,pageNum)

    @classmethod
    def get_user_list_by(cls,dto:SysUserDTO):
        return SysUserDao.get_user_list_by(dto)

    @classmethod
    def update_user(cls,dto:SysUserDTO):
        return SysUserDao.update_user(dto)

    @classmethod
    def delete_user_by_id(cls,dto:SysUserDTO):
        return SysUserDao.delete_user_by_id(dto)

    @classmethod
    def add_user(cls,dto:SysUserDTO):
        return SysUserDao.add_user(dto)

