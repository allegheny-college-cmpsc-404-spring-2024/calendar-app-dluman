from flask import Flask, redirect, request, render_template
from calendar_display import *

app: Flask = Flask(__name__)

@app.route("/")
def index():
    month, year = (
      int(request.args.get("month")) or 12,
      int(request.args.get("year")) or 1969
    )
    print(month, year)
    return render_template(
      "index.html",
      display_calendar = Calendar.date_display(month, year)
    )

if __name__ == "__main__":
    app.run(port = 5001)
