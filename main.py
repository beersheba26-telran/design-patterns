from observer_pattern import NewsAgency, EmailNotification, NewsPublisher
from logging_config import config_logger
config_logger()
newsCNN = NewsAgency("CNN")
newsBBC = NewsAgency("BBC")
emailNotification = EmailNotification("yuri@gmail.com", "david@tel-ran.co.il")
newsPublisher = NewsPublisher()
newsPublisher.subscribe(newsCNN)
newsPublisher.subscribe(newsBBC)
newsPublisher.subscribe(emailNotification)
newsPublisher.notify("Breaking news")
del newsBBC
newsPublisher.notify("Good news")
