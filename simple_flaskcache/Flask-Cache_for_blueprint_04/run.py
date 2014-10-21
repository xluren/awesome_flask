from app import app
print app.url_map
app.run(host="0.0.0.0",port=5555)
