#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 19:31:26 2024

@author: drasken
"""

days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Concatenate all days without newline
all_days = "".join(days_of_week)

print(all_days)


class Year:
    def __init__(self, year):
        self.year = year
        self.months = {
            'January': 31,
            'February': 28 if not self.is_leap_year() else 29,
            'March': 31,
            'April': 30,
            'May': 31,
            'June': 30,
            'July': 31,
            'August': 31,
            'September': 30,
            'October': 31,
            'November': 30,
            'December': 31
        }
        # self.week_days_names = week_days(self, name_of_day)
    
    def is_leap_year(self):
        if self.year % 4 == 0:
            if self.year % 100 == 0 and self.year % 400 != 0:
                return False
            else:
                return True
        else:
            return False

    def days_in_month(self, month):
        return self.months[month]
    
    def days_in_year(self):
        return sum(self.months.values())
    
def week_days(self, day:str):
    all_year_weekdays = []
    
    index_day = days_of_week.index(day)
    
    for month in self.months:
        for i in range(self.months[month]):
            day_to_add = (i + index_day) % 7
            all_year_weekdays.append(days_of_week[day_to_add])
    
    return all_year_weekdays

# Example usage:
year_2024 = Year(2024)
print("Number of days in February 2024:", year_2024.days_in_month('February'))  # Output: 29
print("Number of days in 2024:", year_2024.days_in_year())

