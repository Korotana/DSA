clock_and_angles = [input() for i in range(int(input()))]

def get_smaller_angle(hour, minute):

    # k = abs((minute * (6)) - ((hour*30) + ((minute)/12)*(6)))
    if minute != 60:
        degrees = abs((minute * (6)) - (((hour*5) * 6) + (minute/2)))
    else:
        degrees = abs((minute * (6)) - (((hour*5) * 6) + (30)))
    if degrees >= 180:
        print(360 - degrees)
    else:
        print(degrees)



for hands in clock_and_angles:
    get_smaller_angle(float(hands[0]), float(hands[2:]))

#https://mycode.prepbytes.com/problems/fundamentals/CLCKANGLE