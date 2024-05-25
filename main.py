# 导入FastAPI
from fastapi import FastAPI
import uvicorn
from module_system.controller.sys_users_controller import SysUserController
# 创建FastAPI应用实例
app = FastAPI()
# 通过include_router函数，把各个模块的路由实例加入到FastAPI应用实例中
app.include_router(SysUserController,prefix="/module01",tags=["system模块的接口"])

if __name__ == "__main__":
    uvicorn.run(
        app='main:app',
        port=38500,
        reload=True
    )