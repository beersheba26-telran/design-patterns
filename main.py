from loguru import logger
from logging_config import config_logger
from dataclasses import dataclass

config_logger()
@dataclass
class Report:
    title: str
    body: str
    footer: str
class ReportBuilder:
    def __init__(self):
        self.tl = ""
        self.bd = "" 
        self.ft = ""
    def title(self, title: str):
        self.tl = title 
        return self 
    def body(self, body: str):
        self.bd = body
        return self
    def footer(self, footer: str):
        self.ft = footer 
        return self
    def build(self) -> Report:
        #validating field values with possible raising exceptions in case of invalid report values
        return Report(title=self.tl, body=self.bd, footer=self.ft)
report = ReportBuilder().body("report body").title("report title").footer("report footer").build()    
logger.info(report)
logger.debug(str(report))
               
                 

    
