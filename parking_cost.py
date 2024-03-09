#You parked your car in a parking lot and want to compute the total cost of the ticket. The billing rules are as follows:
#The entrance fee of the car parking lot is 2;
#The first full or partial hour costs 3;
#Each successive full or partial hour (after the first) costs 4.
#You entered the car parking lot at time E and left at time L. In this task, times are represented as strings in the format "HH:MM" (where "HH" is a two-digit number between 0 and 23, which stands for hours, and "MM" is a two-digit number between 0 and 59, which stands for minutes).
#Write a function:
##def solution(E, L)
#that, given strings E and L specifying points in time in the format "HH:MM", returns the total cost of the parking bill from your entry at time E to your exit at time L. You can assume that E describes a time before L on the same day.
#For example, given "10:00" and "13:21" your function should return 17, because the entrance fee equals 2, the first hour costs 3 and there are two more full hours and part of a further hour, so the total cost is 2 + 3 + (3 * 4) = 17. Given "09:42" and "11:42" your function should return 9, because the entrance fee equals 2, the first hour costs 3 and the second hour costs 4, so the total cost is 2 + 3 + 4 = 9.
#Assume that:
#strings E and L follow the format "HH:MM" strictly;
#string E describes a time before L on the same day.
#In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.

#My Solution:


from datetime import datetime

def solution(E, L):
    #parsing time strings to datetime objects
    entry_time = datetime.strptime(E, "%H:%M")
    exit_time = datetime.strptime(L, "%H:%M")

    #calculating the duration in minutes
    duration_minutes = (exit_time - entry_time).total_seconds() / 60

    #calculating the total cost based on the billing rules provided
    entrance_fee = 2
    first_hour_cost = 3
    successive_hour_cost = 4

    #for any car that parks the total cost will be the fee + fee for first hour
    total_cost = entrance_fee + first_hour_cost

    #for cars that pack past the first hour the fee will increase regarding how long the go to park
    if duration_minutes > 60:
        full_hours = int(duration_minutes / 60)
        partial_hours_minutes = duration_minutes % 60
        total_cost += successive_hour_cost * (full_hours - 1)

        if partial_hours_minutes > 0:
            total_cost += successive_hour_cost

    return int(total_cost)  # Convert to integer for final result

E = input("Enter entry time(e.g 23:59): ")
L = input("Enter exit time: ")

total_cost = solution(E, L)
print(total_cost)
