# 导入sqlalchemy框架中的各个工具
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# 导入module_system的模型类
# from module_system import SysUser

# mysql数据库的连接URL
MYSQL_DATABASE_URL = "mysql+pymysql://root:123456@localhost:3306/shuyx_website_db"

# 创建数据库引擎
my_engine = create_engine(MYSQL_DATABASE_URL,echo=True)

# 创建会话对象Session
Session = sessionmaker(my_engine)
db_session = Session()

# 导入sqlalchemy的Base类
from sqlalchemy.ext.declarative import declarative_base
my_Base = declarative_base()

my_Base.metadata.create_all(my_engine)

