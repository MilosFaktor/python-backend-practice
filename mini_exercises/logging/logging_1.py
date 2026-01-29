import logging


"""
    setting logger with 2 handlers
    each handler has set different logging level 
    i_handler -> main.log
    e_handler -> error.log

    """
logger = logging.getLogger(__name__)
logger.setLevel("INFO")  # can be expressed by value 20 instead


info_handler = logging.FileHandler("main.log", mode="w")
info_handler.setLevel("INFO")
formater = logging.Formatter("%(asctime)s - %(name)s -  %(levelname)s - %(message)s")
info_handler.setFormatter(formater)

error_handler = logging.FileHandler("error.log", mode="w")
error_handler.setLevel("ERROR")  # can be expressed by value 40 instead
error_handler.setFormatter(formater)

logger.addHandler(info_handler)
logger.addHandler(error_handler)


logger.info("testing custom logger")
logger.error("testing error")
