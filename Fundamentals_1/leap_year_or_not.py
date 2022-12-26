
years = [input() for i in range(int(input()))]

def check_leap_year(year):

    if year[-1] == "0" and year[-2] == "0":
        if int(year) % 100 == 0 and int(year) % 400 == 0:
            print("yes")
        else:
            print("no")
    else:
        if int(year) % 4 == 0:
            print("yes")
        else:
            print("no")

for case in range(len(years)):
    check_leap_year(years[case])

