import datetime
import calendar

from .calendar_db import DB

class Calendar:

  def __init__(self, month: int = 12, year: int = 1969):
    self.month = month
    self.year = year
    self.number_of_days = calendar.monthrange(self.year, self.month)[1]
    self.data = DB().get_appointments_data_only(
      month = self.months_of_year(month)["short"],
      year = year
    )

  @staticmethod
  def months_of_year(month: int = 12) -> str:
    response = {"int": month}
    months = {
      1: {"long":"January", "short": "Jan"},
      2: {"long":"February", "short": "Feb"},
      3: {"long":"March", "short": "Mar"},
      4: {"long":"April", "short": "Apr"},
      5: {"long":"May", "short": "May"},
      6: {"long":"June", "short": "Jun"},
      7: {"long":"July", "short": "Jul"},
      8: {"long":"August", "short": "Aug"},
      9: {"long":"September", "short": "Sep"},
      10: {"long":"October", "short": "Oct"},
      11: {"long":"November", "short": "Nov"},
      12: {"long":"December", "short": "Dec"}
    }
    response.update(months[month])
    return response

  @staticmethod
  def parse_date(date: str = "") -> dict:
    parts = date.split("-")
    data = {}
    data["year"] = parts[0]
    data["month_data"] = Calendar.months_of_year(int(parts[1]))
    data["month"] = data["month_data"]["short"]
    data["day"] = parts[2]
    return data

  def __days_of_week(self) -> str:
    days = {
      0: "Monday",
      1: "Tuesday",
      2: "Wednesday",
      3: "Thursday",
      4: "Friday",
      5: "Saturday",
      6: "Sunday"
    }
    return days[self.weekday]

  def __update_with_data(self, day):
    for entry in self.data:
      if day["date"] == entry["day"]:
        day["data"] = entry["id"]
    return day

  def __first_day_of_week(self) -> int:
    day = datetime.datetime(self.year, self.month, 1)
    return day.weekday()

  def __make_date_array(self) -> list:
    days = list()
    first_day = self.__first_day_of_week()
    if first_day > 0:
      days = [{"date":''}] * first_day
    days += [
      {"date": n + 1} for n in range(self.number_of_days)
    ]
    days = list(map(self.__update_with_data,days))
    return days

  def date_display(self) -> dict:
    return {
      "display_month": self.month,
      "display_year": self.year,
      "month_text": f"{self.months_of_year(self.month)['long']} {self.year}",
      "number_of_days": self.number_of_days,
      "days": self.__make_date_array(),
      "days_of_week": ['Su','M','T','W','R','F','Sa']
    }
