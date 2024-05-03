import pandas as pd
import matplotlib.pyplot as plt
import calendar

plt.style.use("ggplot") 

cycle_track_df = pd.read_csv("comptagevelo20152.csv", sep=',', parse_dates=['Date'], dayfirst=True,  index_col='Date')

monthly_sum = cycle_track_df.groupby(cycle_track_df.index.month).sum()

monthly_max = monthly_sum.max().sum()

max_month = calendar.month_name[monthly_sum.idxmax().iloc[0]]

cycle_track_df.plot(figsize=(15, 10), title= "Використання велодоріжок за рік")
plt.ylabel("КІлькість використань", color = "black")

print("Максимальна кількість використань трас за місяць = ", monthly_max)
print("Найбільш популярний у велосипедистів місяць: ", max_month)
print("Викоритання по доріжок в ", max_month, "\n", monthly_sum.max())

plt.show()
