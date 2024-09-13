# start

total_minutes: int = int(input('how long is the movie?:'))
hours = total_minutes // 60
remaning_minutes = total_minutes % 60

print(f"{hours} hours and minutes {remaning_minutes} minutes")
