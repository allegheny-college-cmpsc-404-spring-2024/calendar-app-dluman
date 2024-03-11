import datetime
import calendar

class Calendar:

  @staticmethod
  def months_of_year(month_int: int = 12) -> str:
    months = {
      1: "January",
      2: "February",
      3: "March",
      4: "April",
      5: "May",
      6: "June",
      7: "July",
      8: "August",
      9: "September",
      10: "October",
      11: "November",
      12: "December"
    }
    return months[month_int]

  @staticmethod
  def days_of_week(weekday: int = 0) -> str:
    days = {
      0: "Monday",
      1: "Tuesday",
      2: "Wednesday",
      3: "Thursday",
      4: "Friday",
      5: "Saturday",
      6: "Sunday"
    }
    return days[weekday]

  @staticmethod
  def first_day_of_week(month: int = 12, year: int = 1969) -> int:
    day = datetime.datetime(year, month, 1)
    return day.weekday()

  @staticmethod
  def date_display(month: int = 12, year: int = 1969) -> dict:
    number_of_days = calendar.monthrange(year, month)[1]
    first_day = Calendar.first_day_of_week(month = month, year = year)
    return {
      "month_text": Calendar.months_of_year(month_int = month),
      "days": number_of_days,
      "start": first_day,
      "days_of_week": ['M','T','W','R','F','Sa','Su']
    }
