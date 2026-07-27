####################################################################################
import matplotlib.pyplot as plt

### Dataset ###
months =['january', 'Fabruary', 'March', 'April', 'May', 'June']
sales = [120, 150, 170, 160, 200, 220]
profit = [20,35, 40, 30, 50, 60]
ad = [5, 8, 10, 7, 12, 15]

### Answer 1 ###
plt.plot(months, sales, color = "green", linestyle = "--", marker = "o")
plt.title("Sales of Each Months")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid()
plt.show()

### Answer 2 ###
plt.plot(months, profit, color = "red")
plt.title("Profit of Each months")
plt.xlabel("Month")
plt.ylabel("Profit")
plt.grid()
plt.show()

### Answer 3 ###
plt.plot(months, sales, marker = "x")
plt.title("Sales of Each Months")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid()
plt.show()

### Answer 4 ###
plt.bar(months, sales)
plt.title("Sales of Each Months")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.show()

### Answer 5 ###
plt.bar(months, ad, color = "green")
plt.title("Ads of Each Months")
plt.xlabel("Months")
plt.ylabel("Ads")
plt.show()

### Answer 6 ###
plt.pie(sales, labels = months, autopct= "%1.1f%%")
plt.title("pie chart of Sales")
plt.show()

### Answer 7 ###
plt.subplot(1, 2, 1)
plt.scatter(months, ad)
plt.title("Graph 1: Ads")
plt.xlabel("Months")
plt.ylabel("Ads")

plt.subplot(1, 2, 2)
plt.scatter(months, sales)
plt.title("Graph 2: Sales")
plt.xlabel("Months")
plt.ylabel("Sales")

plt.show()

### Answer 8 ###
plt.scatter(ad, profit, color = "red", s = 100)
plt.title("Graph of Ads and Profit")
plt.xlabel("Ad")
plt.ylabel("Profit")
plt.show()

### Answer 9 ###
plt.subplot(1, 2, 1)
plt.plot(months, sales)
plt.title("Graph1: Sales of Each Months")
plt.xlabel("Months")
plt.ylabel("Sales")

plt.subplot(1, 2, 2)
plt.bar(months, ad)
plt.title("Graph2: Ads of Each Months")
plt.xlabel("Months")
plt.ylabel("Ad")

plt.show()

### ANswer 10 ###
plt.subplot(2, 2, 1)
plt.plot(months, sales)
plt.title("Graph1: Sales of Each Months")
plt.xlabel("Months")
plt.ylabel("Sales")

plt.subplot(2, 2, 2)
plt.bar(months, profit)
plt.title("Graph2: Profits of Each Months")
plt.xlabel("Months")
plt.ylabel("Profit")

plt.subplot(2, 2, 3)
plt.scatter(ad, sales)
plt.title("Graph3: Sales and Ads")
plt.xlabel("Ad")
plt.ylabel("Sales")

plt.subplot(2, 2, 4)
plt.pie(sales, labels= months)
plt.title("Graph4: Pie Chart of Each Months")

plt.show()
