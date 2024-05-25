from module_system.entity.sys_user_eneity import SysUserEntity
from module_system.dto.sys_user_dto import SysUserDTO
from config.database_config import session_maker

class SysUserDao:

    @classmethod
    def get_user_list(cls,pageSize:int,pageNum:int):
        with session_maker() as db_session:
            res = db_session.query(SysUserEntity).limit([pageNum,pageSize]).all()
            print("result=", res)
            return res

    @classmethod
    def get_user_list_by(cls, dto: SysUserDTO):
        with session_maker() as db_session:
            res = db_session.query(SysUserEntity).filter(SysUserEntity.userId == dto.userId ).all()
            return res

    @classmethod
    def update_user(cls, dto: SysUserDTO):
        # user.dict() 将user对象转换为字典类型数据
        with session_maker() as db_session:
            res = db_session.query(SysUserEntity).filter(SysUserEntity.userId == dto.userId).update(dto.dict())
            print("result=", res)
            return res

    @classmethod
    def delete_user_by_id(cls,dto: SysUserDTO):
        with session_maker() as db_session:
            res = db_session.query(SysUserEntity).filter(SysUserEntity.id == dto.userId).delete()
            print("result=", res)
            return res

    @classmethod
    def add_user(cls,dto:SysUserDTO):
        with session_maker() as db_session:
            one = SysUserEntity(**dto)
            res = db_session.add(one)
            print("result=", res)
            return res
