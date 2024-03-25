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
          BEGIN TRANSACTION;
          	INSERT INTO appointment_data(month, day, year) VALUES('1', '2', '3');
          COMMIT;
            INSERT INTO appointment_meta(time, title, description) VALUES('4', '5', '6');
          COMMIT;
        """
      )
      self.conn.commit()
    except Exception as e:
      print(e)
      return False
    return True
