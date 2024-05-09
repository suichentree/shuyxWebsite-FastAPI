# 导入sqlalchemy框架中的各个工具
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# mysql数据库的连接URL
MYSQL_DATABASE_URL = "mysql+pymysql://root:123456@localhost:3306/shuyx_website_db"

# 创建数据库引擎myEngine
myEngine = create_engine(MYSQL_DATABASE_URL,echo=True)

# 创建会话对象mySession
mySession = sessionmaker(autocommit=False, autoflush=False, bind=myEngine)

# 创建基类myBase
myBase = declarative_base()


