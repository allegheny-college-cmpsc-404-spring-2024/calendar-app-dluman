from flask import Flask, Response, redirect, request, render_template

import datetime
import requests

app: Flask = Flask(__name__)
app.debug = True

@app.route("/", methods = ["GET", "POST"])
def index():
  month = None
  year = None
  try:
    month = request.args.get["month"]
    year = request.args.get["year"]
  except:
    now = datetime.datetime.now()
    month = now.month
    year = now.year
  return render_template(
    "layout.html",
    data = {
      "month": month,
      "year": year
    }
  )

@app.route("/calendar", methods = ["GET","POST"])
def calendar():
    month, year = (
      request.form["month"],
      request.form["year"]
    )
    data = requests.post(
      "http://localhost:5000/api/v1/calendar/display",
      json = {
        "month": month,
        "year": year
      }
    )
    return render_template(
      "components/calendar.html",
      data = data.json()
    )

@app.route("/modals/add-modal", methods = ["GET"])
def add_modal_get():
  month, day, year = (
    request.args.get("month"),
    request.args.get("day") or 1,
    request.args.get("year")
  )
  if int(month) < 10:
    month = "0" + month
  if int(day) < 10:
    day = "0" + day
  return render_template(
    "components/add_modal.html",
    data = {"month": month, "day": day, "year": year}
  )

@app.route("/events/new", methods = ["POST"])
def new_event_post():
  data = requests.post(
    "http://localhost:5000/api/v1/events/add",
    json = request.form
  )
  return Response(status = data.status_code)
