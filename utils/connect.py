import MetaTrader5 as mt5
import utils.settings as st
from logger.logger import get_logger

logger = get_logger(name = __name__, level = "DEBUG", stream = True)

def initialize(account: int, password: str):

    logger.info("MetaTrader5 package author: " + mt5.__author__)
    logger.info("MetaTrader5 package version: " + mt5.__version__)
    ini = mt5.initialize(login = account, server = st.SERVER, password = password)
    if not ini: 
        logger.error("Initialized() failed")
    authorized = mt5.login(login = account, server = st.SERVER, password = password)
    if authorized:
        logger.info("Connected to account #{}".format(account))
    else: 
        logger.error("Failed to connect to account #{account}, error code {error}".format(account = account, error = mt5.last_error()))


