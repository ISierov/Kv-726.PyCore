from flask import Flask, render_template
import pyowm

app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    OWM_API_key = pyowm.OWM('KEY')
    manager = OWM_API_key.weather_manager()

    observe = manager.weather_at_place(name)
    w = observe.weather
    temperature = w.temperature('celsius')
    return render_template('hello.html', name=name, temp=temperature['feels_like'])

if __name__ == '__main__':
    app.run()
