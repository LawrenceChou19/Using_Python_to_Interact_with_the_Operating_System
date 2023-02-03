import requests
response = requests.get("http://www.google.com")
print(len(response.text))

import arrow
date = arrow.get('2020-01-18','YYYY-MM-DD')
date.shift(weeks=+6).format('MMM DD YYYY')
print(date.shift(weeks=+6).format('MMM DD YYYY'))


import pandas
visitors = [1235,6424,9345,8464,2345]
errors = [23,45,33,45,76]
df = pandas.DataFrame({"visitors":visitors,"error":errors}, index=["Mon","Tues","Wed","Thu","Fri"])
print(df)
print(df["error"].mean())
