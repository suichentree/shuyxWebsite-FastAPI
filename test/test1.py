from module_system.dao.sys_user_dao import SysUserDao
from module_system.entity.sys_user_eneity import SysUserEntity

one = SysUserEntity(userId=1,userName="xiaoming")

result = SysUserDao.get_user_list(one)

print("result=",result)