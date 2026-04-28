from loguru import logger
from logging_config import config_logger
from abc import ABC, abstractmethod
from os import getenv
config_logger()
# abstract class Payment
class Payment(ABC):
    @abstractmethod
    def pay(self, amount: int):
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
# abstract class Risk
class Risk(ABC):
    @abstractmethod
    def score(self)->float:
        pass
 ##################################################
 # different Risk implementations
class RiskPaypal(Risk) :
    def score(self)->float:
        logger.debug("computing risk for PayPal payments")
        return 0.02
class RiskCreditCard(Risk):
    def score(self)->float:
        logger.debug("computing risk for Credit card payments")
        return 0.035
#########################################################
# Abstract Factory
class PaymentFactory(ABC):
    @abstractmethod
    def payment(self)-> Payment :
        pass
    @abstractmethod
    def risk(self) -> Risk:
        pass   
#############################################################
# Factory implementations
class PayPalPaymentFactory(PaymentFactory):
    def payment(self)-> Payment:
        return PayPalPayment()
    def risk(self)->Risk:
        return RiskPaypal()
class CardPaymentFactory(PaymentFactory):
    def payment(self)-> Payment:
        return CardPayment()
    def risk(self)->Risk:
        return RiskCreditCard()   
 #######################################################
 # functionality  
def checkout(paymentFactory: PaymentFactory, amount):
    payment: Payment = paymentFactory.payment() 
    risk: Risk = paymentFactory.risk()
    score = risk.score()
    if amount > 1000 and  score >= 0.03:
        logger.error(f"for {amount} USD risk should be less than {score}")
        raise ValueError(f"for {amount} USD risk should be less than {score}")
    payment.pay(amount)
              
#################################################################
# usage
try:
    checkout(PayPalPaymentFactory(), 5000)
except ValueError:
    pass    

      
  
       
                   