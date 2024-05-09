from config.database_config import myBase
from config.database_config import myEngine

myBase.metadata.create_all(bind=myEngine)