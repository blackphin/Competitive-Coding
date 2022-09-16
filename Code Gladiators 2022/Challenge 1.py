from datetime import datetime, timedelta

time_input1 = datetime.strptime(input(), "%H %M")
time_input2 = input()
hour, minute = [int(x) for x in time_input2.split(" ")]
print((time_input1 + timedelta(hours=hour, minutes=minute)).strftime("%H %M"))
