print("Time Converter")

def time_converter(seconds):
    print("Time Calculator")
print("")
seconds = int(input("Please enter number of seconds: "))

if seconds >= 60 and seconds <3600:
    
    minutes = seconds // 60
    minuteRemainder = seconds % 60
    print(f"{minutes}mins:{minuteRemainder}secs")
elif seconds >= 3600 and seconds < 86400:
    hours = seconds // 3600
    hourRemainder = seconds % 3600 // 60
    seconds2 = seconds % 3600 % 60

    print(f"{hours}hrs:{hourRemainder}mins:{seconds2}secs")

elif seconds >= 86400:
    days = seconds // 86400
    hours1 = seconds // 3600 % 24
    mins1 = seconds % 3600 // 60
    seconds1 = seconds % 3600 % 60
    print(f"{days}D {hours1}H {mins1}m {seconds1}secs")
