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
    cursor = self.conn.cursor()
    query = cursor.execute(
      f"""
        SELECT id, day FROM appointment_data
        WHERE month = '{month}' AND year = '{year}'
      """
    )
    return query.fetchall()

  def get_appointments_with_meta(self, month: str = "Dec", year: int = 2023):
    cursor = self.conn.cursor()
    query = cursor.execute(
      f"""
        SELECT day,time,title,description FROM appointment_data
        LEFT JOIN appointment_meta ON appointment_data.id = appointment_meta.id
        WHERE month = '{month}' AND year = '{year}'
      """
    );
    return query.fetchall()

  def add_appointment(self, data: dict = {}) -> bool:
    cursor = self.conn.cursor()
    try:
      query = cursor.execute(
        f"""
          INSERT INTO appointment_data(month,day,year)
          VALUES('{data["month"]}', '{data["day"]}', '{data["year"]}')
        """
      )
      # TODO: GET THE ID FROM THE FIRST INSERT AND USE IN SECOND QUERY
      query = cursor.execute(
        f"""
          INSERT INTO appointment_meta(time,title,description)
          VALUES('{data["time"]}', '{data["title"]}', '{data["description"]}')
        """
      )
      self.conn.commit()
    except Exception as e:
      print(e)
      return False
    return True
