import pandas as pd
import time
from GetBitcoin import get_bitcoin_df
from GetCommodities import get_commodities_df

SLEEP_SECONDS = 60

df_btc = get_bitcoin_df()
df_comm = get_commodities_df()

while True:
    # Junta tudo
    df = pd.concat([df_btc, df_comm], ignore_index=True)

    time.sleep(SLEEP_SECONDS)