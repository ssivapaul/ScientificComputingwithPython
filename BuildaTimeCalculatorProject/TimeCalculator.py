def add_time(start, duration, day=''):
    day = day.lower()
    day = day.capitalize()
    new_time = ''
    # Processing Starting time
    start_time_part, initial_period = start.split()
    hours, minutes = map(int, start_time_part.split(':'))
    start_minutes = 60*hours + minutes

    # Processing Duration
    hours, minutes = map(int, duration.split(':'))
    duration_minutes = 60*hours + minutes
    final_minutes = start_minutes + duration_minutes 
    #---------------------------------------------------------
    # Workout hours
    if (final_minutes//60)%12 == 0:
        final_hrs = str(12)
    else:
        final_hrs = str((final_minutes//60)%12)  
    new_time += final_hrs
    #-----------------------------------------------------------------------   
    # Workout minutes
    final_mts = str(final_minutes%60)  
    new_time += f':{final_mts.zfill(2)} '
    #--------------------------------------------
    # work out period (AM /PM)
    period_identifier = final_minutes//720
    if period_identifier % 2 != 0:
        if initial_period == 'AM':
            final_period = 'PM'
        else:
            final_period = 'AM'
    else:
        final_period = initial_period
    new_time += final_period
    #----------------------------------------------------------------------
    # Workout number of days
    if initial_period == 'PM':
        if final_minutes < 720:
            numberOfDays = 0
        else:
            numberOfDays = 1 + (final_minutes - 720)//1440

    if initial_period == 'AM':
        if final_minutes < 1440:
            numberOfDays = 0
        else:
            numberOfDays = 1 + (final_minutes - 1440)//1440
    #-----------------------------------------------------------------------
     # Workout final day 
    Days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    if day != '':
        index = Days.index(day)
        final_index = (numberOfDays + index)%7
        final_day = Days[final_index]
        new_time += f', {final_day}'
    if numberOfDays == 1:
        new_time += f' (next day)'
    elif numberOfDays > 1:
        new_time += f' ({numberOfDays} days later)'
    #-----------------------------------------------------------------------
    
    return new_time

print(add_time('11:43 PM', '24:20', 'tueSday'))