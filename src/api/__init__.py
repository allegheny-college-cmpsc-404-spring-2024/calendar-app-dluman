from flask import Flask, Response, redirect, request, render_template

import json
import datetime

from .post import *
from .calendar_display import *
from .calendar_db import DB

app: Flask = Flask(__name__)
app.debug = True

@app.route("/v1/calendar/display", methods = ["POST"])
def api_calendar_display_post():
  data = post.data(request)
  try:
    month, year = (
      data["month"],
      data["year"]
    )
  except KeyError:
    return Response(status=500)
  calendar = Calendar(
    int(month),
    int(year)
  )
  return Response(
    json.dumps(calendar.date_display()),
    status=200,
    mimetype = "application/json",
    content_type = "application/json"
  )


@app.route("/v1/calendar/list", methods = ["POST"])
def api_appt_list_post():
  data = post.data(request)
  month, year = (
    Calendar.months_of_year(data["month"])["short"],
    data["year"]
  )
  result = DB().get_appointments_with_meta(month = month, year = year)
  return Response(
    json.dumps(result),
    status=200,
    mimetype = "application/json",
    content_type = "application/json"
  )

@app.route("/v1/events/add", methods = ["POST"])
def api_evt_add_post():
  event = {} 
  data = post.data(request)
  for field in data:
    if field == "date":
      event.update(Calendar.parse_date(data[field]))
    event[field] = data[field]
  status = DB().add_appointment(event)
  if status:
    return Response(status = 200)
  return Response(status = 500)
