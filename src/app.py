from werkzeug.middleware.dispatcher import DispatcherMiddleware
from frontend import app as frontend
from api import app as api

application = DispatcherMiddleware(
  app = frontend,
  mounts = {'/api': api}
)
