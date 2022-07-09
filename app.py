import utils.settings as st
from utils.connect import initialize
from utils.info import get_info, get_account_info
from utils.pull import pull_data
import MetaTrader5 as mt5

# Get account.
account = st.accounts[0]

# Enter to account.
initialize(account["account"], account["password"])

# Get account info.
get_info()
get_account_info()

pull_data()

# Shutdown.
mt5.shutdown()


