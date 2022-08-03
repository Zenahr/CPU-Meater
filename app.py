from flask import Flask, render_template
import psutil
import flaskwebgui

app = Flask(__name__)
gui = flaskwebgui.FlaskUI(app)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/api/cpu')
def api_cpu():
    return str(psutil.cpu_percent(interval=0.1))

@app.route('/api/ram')
def api_ram():
    return str(psutil.virtual_memory().percent)

if __name__ == '__main__':
    gui.run()