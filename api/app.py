from flask import Flask, request, Response, abort
from datetime import datetime
from datetime import timezone

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False



@app.route('/')
def function():
	now = datetime.now(tz=timezone.utc)
	nowStr = now.isoformat()

	return('<html><head><title>Rozwiązanie zadania PZC 1.1</title></head><body>'+nowStr+'</body>')






	












