from loguru import logger
from logging_config import config_logger
from abc import ABC, abstractmethod
from os import getenv
config_logger()
# abstract class Payment
class Payment(ABC):
    @abstractmethod
    def pay(amount: int):
        pass
    ###############################
    # Classes implemting method pay of abstract Payment
class PayPalPayment(Payment):
    def pay(self,amount: int):
        logger.info(f"paypal payment of amount {amount} USD")
class CardPayment(Payment):
    def pay(self, amount: int):
        logger.info(f"credit card payment of amount {amount} USD") 
    #######################################
    # Identification of different Payment classes - FACTORY
FACTORY: dict[str, Payment] = {
        "card": CardPayment,
        "paypal": PayPalPayment
}   
# Factory method
def createPayment(paymentName: str) -> Payment:
    res: Payment|None = None
    try:
        res: Payment = FACTORY[paymentName]()
        logger.debug(f"{paymentName} class instance is returned")
    except KeyError:
        logger.error(f"{paymentName} not implemented as Payment class")
    return res 
################################################################
# creating Payment 
paymentName: str =  getenv("PAYMENT_TYPE") 
payment: Payment = createPayment(paymentName) 
############################################################
# using in many code lines
payment.pay(500)
       
                   