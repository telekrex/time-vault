#!/usr/bin/env python3
# Time Vault | Written by telekrex | Public domain

# Edit the values in this file as you like, then
# run it in your terminal of choice, or compile
# it using build tooling of choice...

# We start by defining your lifespan. I've chosen
# based on an the average human lifespan as of 2024,
# of 73 years. This calculation we are doing isn't
# going to be accurate, it's just a thought experiment.

birth = "1997-04-17 12:00:00" # Birth date and time
death = "2070-04-17 12:00:00" # Death date and time,
# where death is 73 years from birth, based on the
# 73 years I chose. Change this as you like.
# 12 O'clock is an arbitrary choice of mine,
# change this as you like as well.

# Convert these dates
from datetime import datetime
format_string = "%Y-%m-%d %H:%M:%S"
# from strings into datetime objects.
birth = datetime.strptime(birth, format_string)
death = datetime.strptime(death, format_string)

# Calculate the difference
# between death and birth
lifetime = death - birth
# as datetime objects,
# then convert the difference to hours

current_datetime = datetime.now()
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
x = datetime.strptime(formatted_datetime, format_string)
time_remaining = death - x
remaining_hours = time_remaining.total_seconds() / 3600

# Here we define the factors that impact
# net usable time; your responsibilities.
# These values, again like lifespan and the
# hours of birth and death, can be adjusted
# however you see fit;
sleep_hours = 8 # hours of sleep per 24 hours
work_hours = 8 # hours of work per 24 hours
resp_hours = 3 # hours of responsibilities per 24 hours
daily_debt_hours = sleep_hours + work_hours + resp_hours
days = remaining_hours / 24
usable_hours_per_day = 24 - daily_debt_hours
# We end up with "t", the hours you have left.
t = usable_hours_per_day * days

# Show this output.
print(f'Est. {round(t)} usable hours until death.')
