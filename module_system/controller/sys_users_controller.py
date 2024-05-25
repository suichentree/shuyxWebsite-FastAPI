from fastapi import APIRouter
from config.log_config import logger
from module_system.dto.sys_user_dto import SysUserDTO
from module_system.service.sys_user_service import SysUserService

SysUserController = APIRouter(prefix='/system/user')

@SysUserController.post("/listPage")
async def get_user_list(pageSize:int,pageNum:int):
    logger.info(f'/system/user/list, pageSize = {pageSize} pageNum = {pageNum}')
    try:
        res = SysUserService.get_user_list(pageSize,pageNum)
        return res
    except Exception as e:
        return logger.exception(e)

@SysUserController.post("/listBy")
async def get_user_list_by(dto: SysUserDTO):
    logger.info(f'/system/user/listBy, dto = {dto}')
    try:
        res = SysUserService.get_user_list_by(dto)
        return res
    except Exception as e:
        return logger.exception(e)




