import calendar
from calendar import monthrange

class MakeMonth(object):
    """ Creates an object representing a calendar month in a given year.
    You can then find out what day of the week any day of the month was/is/will
    be.
    """

    def __init__(self, year, month):
        self.month = month
        self.year = year
        self.weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
                        'Friday', 'Saturday', 'Sunday']
        # the above means 0=Monday, etc.
        self.start_of_mnth, self.end_of_mnth = calendar.monthrange(year, month)

    def day(self, day):
        if day < 1:
            raise ValueError("The month starts on the first. Enter a value "
                            "1 or higher.")
        if day > self.end_of_mnth:
            raise ValueError("That isn't a day in the month. The month has %d "
                "days." % self.end_of_mnth)
        else:
            day_of_week = (self.start_of_mnth + (day - 1)) % 7
            return self.weekdays[day_of_week]

# the use of calendar.monthrange was first suggested during our inclass code
# review.