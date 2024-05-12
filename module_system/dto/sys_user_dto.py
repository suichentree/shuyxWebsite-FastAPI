from pydantic import BaseModel
from typing import Optional

# 定义Addr模型类型
class SysUserDTO(BaseModel):
    userId:Optional[int] = None             #  Optional[int] = None 类型可以是int,也可以是 None
    orgId:Optional[int] = None
    positionId:Optional[int] = None
    userName:Optional[str] = None
    passWord:Optional[str] = None
    gender:Optional[str] = None
    birthday:Optional[str] = None
    avatar:Optional[str] = None
    email:Optional[str] = None
    phone:Optional[str] = None
    status:Optional[str] = None

    page_num: Optional[int] = None
    page_size: Optional[int] = None
    total: int



