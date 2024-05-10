from module_system.entity.sys_user_eneity import SysUser
from sqlalchemy.orm import Session

class SysUserDao:

    @classmethod
    def add_user(cls, db: Session, user):
        """
        新增用户数据库操作
        :param db: orm对象
        :param user: 用户对象
        :return: 新增校验结果
        """
        db_user = SysUser(**user.model_dump(exclude={'admin'}))
        db.add(db_user)
        db.flush()

        return db_user