import calendar

def display_month(year, month):
    #Prints the calendar of a given month and year.
    print(calendar.month(year, month))

def display_year(year):
    #Prints the calendar of the entire year
    print(calendar.calendar(year))

if __name__ == "__main__":
    year = int(input("Enter year: "))
    month = int(input("Enter month (1-12): "))
    display_month(year, month)