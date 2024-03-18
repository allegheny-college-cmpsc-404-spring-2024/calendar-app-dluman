import sqlite3
import collections

class DB:

  def __init__(self):
    db_path = "data/calendar.db"
    self.conn = sqlite3.connect(db_path)
    self.conn.row_factory = self.__entry_factory

  def __entry_factory(self, cursor: sqlite3.Cursor, row: tuple):
    entry = {}
    for idx, col in enumerate(cursor.description):
      entry[col[0]] = row[idx]
    return entry

  def get_appointments_data_only(self, month: str = "Dec", year: int = 2023):
    return True

  def get_appointments_with_meta(self, month: str = "Dec", year: int = 2023):
    return True

  def add_appointment(self, data: dict = {}) -> bool:
    return True
