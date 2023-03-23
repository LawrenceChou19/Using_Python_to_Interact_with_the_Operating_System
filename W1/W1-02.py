import arrow
date = arrow.get('2020-01-18','YYYY-MM-DD')
date.shift(weeks=+6).format('MMM DD YYYY')
print(date.shift(weeks=+6).format('MMM DD YYYY'))
