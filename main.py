from loguru import logger
from composite_nodes import Text, Group
from logging_config import config_logger
config_logger()
text1: Text = Text("Hello ")
text2: Text = Text("World")
text3: Text = Text("!!!")
group1: Group = Group(text2, text3)
group2: Group = Group(text1, group1)
logger.info(group2.render())
