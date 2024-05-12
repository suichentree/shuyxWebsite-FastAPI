from fastapi import APIRouter, Request
from module_system.dto.sys_user_dto import SysUserDTO
from module_system.service.sys_user_service import SysUserService

sysUserController = APIRouter(prefix='/system/user')

@sysUserController.get("/list", response_model=SysUserDTO)
async def get_user_list(dto: SysUserDTO):
    # 获取分页数据
    user_page_query_result = SysUserService.get_user_list(dto)
    return user_page_query_result
