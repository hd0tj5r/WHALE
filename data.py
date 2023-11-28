import mysql.connector
from datetime import date, timedelta
import pandas as pd
import shioaji as sj
import pandas as pd
from datetime import datetime
import time 
from tqdm import tqdm
import numpy as np
import mplfinance as mpf
import matplotlib.gridspec as gridspec
import matplotlib.ticker as ticker
import matplotlib.pyplot as plt
from sqlalchemy import create_engine


#串永豐API登入，以下為密鑰勿外流
api = sj.Shioaji()
api.login(
    api_key="3MTPsGHZ8V9rYRcqNQJhR1xVbALXLu5zZL2wWiZ1kw9q", 
    secret_key="3GrcP3EbLdXSHcMFfhyK9mrNEY3j1QVfxNCgo1N1T4kW",
    contracts_timeout=10000
)
#看期貨商品內有什麼資料
api.Contracts.Futures.TXF
#抓取時間區間內kbars
kbars = api.kbars(
    contract=api.Contracts.Futures.TXF.TXFR1
)
#--------------------------------台指---------------------------------------
# #轉換時間格式
import pandas as pd
df = pd.DataFrame({**kbars})
# 將'ts'列轉換為Datetime對象
df['ts'] = pd.to_datetime(df['ts'])
# 設置'ts'列為DataFrame的索引
df.set_index('ts', inplace=True)
# 創建到 MySQL 的連接
engine = create_engine('mysql+mysqlconnector://root:hdsfysfbskj@localhost:3306/whale_base')
# 將 DataFrame 存入 MySQL，if_exists='replace'表示如果表格存在則替換
df.to_sql('tw_main', con=engine, if_exists='replace', index=True)

# 關閉連線
engine.dispose()