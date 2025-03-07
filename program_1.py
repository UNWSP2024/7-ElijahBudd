# Elijah Budd
# 3/3/2025
# Program #1: Rainfall
# Design a program that lets the user enter the total rainfall for each of 12 months into a list.
# The program should calculate and display the total rainfall for the year,
# the average monthly rainfall, # and the months with the highest and lowest amounts.

monthly_rainfall = []

for x in range(1, 13):
    rainfall = float(input("Enter rainfall for month " + str(x) +":"))
    monthly_rainfall.append(rainfall)

def calculate_rainfall():
    total = sum(monthly_rainfall)
    average = total / x

    smallest = min(monthly_rainfall)
    biggest = max(monthly_rainfall)
    highest_month = monthly_rainfall.index(max(monthly_rainfall)) + 1
    lowest_month = monthly_rainfall.index(min(monthly_rainfall)) + 1

    print("Total rainfall for the year:", total)
    print(f"Average monthly rainfall: {average:0.2f}")
    print(f"Lowest monthly rainfall: Month {lowest_month} ({smallest} inches)")
    print(f"Highest monthly rainfall: Month {highest_month} ({biggest} inches)")

if __name__ == '__main__':
    calculate_rainfall()

TestRun:
Enter rainfall for month 1:3.7
Enter rainfall for month 2:4.9
Enter rainfall for month 3:8
Enter rainfall for month 4:14
Enter rainfall for month 5:12
Enter rainfall for month 6:10
Enter rainfall for month 7:5.7
Enter rainfall for month 8:4.9
Enter rainfall for month 9:2.5
Enter rainfall for month 10:5.8
Enter rainfall for month 11:8.7
Enter rainfall for month 12:7.3
Total rainfall for the year: 87.5
Average monthly rainfall: 7.29
Lowest monthly rainfall: Month 9 (2.5 inches)
Highest monthly rainfall: Month 4 (14.0 inches)
