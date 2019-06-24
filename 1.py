from datetime import datetime, timedelta
def convert_time_to_string(dt):
    return f"{dt.hour}:{dt.minute:02}"
start_time = datetime.strptime( "2009-11-12", "%Y-%m-%d" )
end_time = start_time + timedelta(days=1)
start_time += timedelta(minutes=1)
text = convert_time_to_string(start_time)
print(start_time)
print(text)
