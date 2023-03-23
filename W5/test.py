import pandas as pd
import requests
from io import StringIO

# 設定日期
date = '20220304'

# 下載三大法人買賣超資料
url = f'https://www.twse.com.tw/fund/T86?response=csv&date={date}&selectType=ALLBUT0999'
res = requests.get(url)
data = res.text.replace('=', '').split('\n')

# 將資料轉換成DataFrame格式
df = pd.read_csv(StringIO(res.text), header=1).dropna(how='all', axis=1).dropna(how='any')

# df.columns = data[0].replace(' ', '').split(',')

# df = df.dropna(thresh=4)  # 刪除無效的資料列
print(df)

# # 篩選三大法人買賣超股票
# df_buy = df.loc[df['買賣超別'] == '買超']
# df_sell = df.loc[df['買賣超別'] == '賣超']

# # 依照買賣超金額排序
# df_buy = df_buy.sort_values(by=['買賣超金額'], ascending=False)
# df_sell = df_sell.sort_values(by=['買賣超金額'], ascending=False)

# # 顯示買賣超前10名的股票
# print(f"三大法人買超前10名股票：\n{df_buy.head(10)}\n")
# print(f"三大法人賣超前10名股票：\n{df_sell.head(10)}")
