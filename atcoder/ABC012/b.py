N = int(input())


def converter(time):
    return str(time) if time > 9 else "0"+str(time)


hours = N // 3600
minutes = (N - hours*3600) // 60
seconds = N - (hours * 3600 + minutes * 60)
hours_str = converter(hours)
minutes_str = converter(minutes)
seconds_str = converter(seconds)
print(hours_str+":"+minutes_str+":"+seconds_str)
