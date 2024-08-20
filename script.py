hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]
total_price = 0

for p in prices:
  print(p)
  total_price += p
print(total_price)
average_price = total_price/len(prices)
print(average_price)

new_prices = [i - 5 for i in prices ]
print(new_prices)

total_revenue = 0
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
  i+=1
print(total_revenue)
average_daily_revenue = total_revenue/7
print(average_daily_revenue)

cuts_under_30 = [i for i in new_prices if i < 30]
print(cuts_under_30)