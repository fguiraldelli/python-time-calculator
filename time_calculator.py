def add_time(start, duration, day_of_the_week=None):
    # Split the start time into hours and minutes
    start_time, period = start.split()
    start_hours, start_minutes = map(int, start_time.split(':'))
    # Split the duration into hours and minutes
    duration_hours, duration_minutes = map(int, duration.split(':'))
    # Convert the start time to 24-hour format
    if period == 'PM':
        start_hours += 12
    # Add the duration to the start time
    end_hours = start_hours + duration_hours
    end_minutes = start_minutes + duration_minutes
    # Handle the case where the minutes exceed 60
    if end_minutes >= 60:
        end_hours += 1
        end_minutes -= 60
    # Handle the case where the hours exceed 24
    days_later = 0
    while end_hours >= 24:
        end_hours -= 24
        days_later += 1
    # Convert the end time back to 12-hour format
    if end_hours >= 12:
        period = 'PM'
        if end_hours > 12:
            end_hours -= 12
    else:
        period = 'AM'
        if end_hours == 0:
            end_hours = 12
    # Format the end time as a string
    end_time = f'{end_hours:1}:{end_minutes:02} {period}'
    # Handle the case where the day of the week is provided
    if day_of_the_week:
        day_of_the_week = day_of_the_week.lower().capitalize()
        days_of_the_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        start_day_index = days_of_the_week.index(day_of_the_week)
        end_day_index = (start_day_index + days_later) % 7
        end_day = days_of_the_week[end_day_index]
        end_time += f', {end_day}'
    # Handle the case where the duration is more than one day
    if days_later == 1:
        end_time += ' (next day)'
    elif days_later > 1:
        end_time += f' ({days_later} days later)'
    return end_time
