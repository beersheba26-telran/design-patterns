import copy
from loguru import logger
from logging_config import config_logger
config_logger()
protoUser = {"role":"USER", "features":["read"]}
protoAdmin = {"role":"ADMIN", "features": ["read","write"]}
def createUser(*, role:str, name: str)->dict:
    proto = protoUser if role == "USER" else protoAdmin
    res = copy.deepcopy(proto)
    res["name"] = name
    return res

user1 = createUser(name="Vasya", role="USER")
user2 = createUser(name="Olya", role="ADMIN")
logger.info(f"user1 is {user1}")
logger.info(f"user2 is {user2}")
