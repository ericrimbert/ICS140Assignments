# 2.6.1 - Compute and average

# variable that is assigned to a list of values
num_sales = [3, 4, 8]
total_sales = 0
counter = 0

# for loop that is getting the total sales people and summing the sales
for sales in num_sales:
    total_sales += sales
    counter += 1

# averaging the sales by dividing the total sales by the sales people
avg_sales = total_sales / counter

# outputting the average sales per person
print(f"Average sales is {avg_sales}")
