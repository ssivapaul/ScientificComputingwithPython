def add_time(start, duration):
    time_part, period = start.split()
    start_minutes = convert_Time_To_Minutes(time_part)
    duration_minutes = convert_Time_To_Minutes(duration)
    total_minutes = start_minutes + duration_minutes
    hours = str(total_minutes//60)
    minutes = str(total_minutes%60)
    return hours, minutes, period

def convert_Time_To_Minutes(time):    
    print(time)
    hours, minutes = map(int, time.split(':'))
    minutes = 60*hours + minutes
    return minutes

hours, minutes, period = add_time('11:43 AM', '10:20')
print(f'{hours.zfill(2)}:{minutes.zfill(2)} {period}')