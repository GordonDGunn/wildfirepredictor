from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import pandas as pd
from mainwindowR1 import Ui_MainWindow
import csv
from datetime import datetime
import json
import os
import sys
import requests
from urllib.parse import urlencode
import joblib
from datetime import date

#OPENWEATHERMAP_API_KEY = os.environ.get('OPENWEATHERMAP_API_KEY')
OPENWEATHERMAP_API_KEY = '98795ad55f09f1b49999633f67d0583c'

"""
Get an API key from https://openweathermap.org/ to use with this
application.

"""


def from_ts_to_time_of_day(ts):
    dt = datetime.fromtimestamp(ts)
    return dt.strftime("%I%p").lstrip("0")


class WorkerSignals(QObject):
    '''
    Defines the signals available from a running worker thread.
    '''
    finished = pyqtSignal()
    error = pyqtSignal(str)
    result = pyqtSignal(dict, dict)

class WeatherWorker(QRunnable):
    '''
    Worker thread for weather updates.
    '''
    signals = WorkerSignals()
    is_interrupted = False

    def __init__(self, location):
        super(WeatherWorker, self).__init__()
        self.location = location

    @pyqtSlot()
    def run(self):
        try:
            params = dict(
                q=self.location,
                appid=OPENWEATHERMAP_API_KEY
            )

            url = 'http://api.openweathermap.org/data/2.5/weather?%s&units=metric' % urlencode(params)
            r = requests.get(url)

            global weather
            global locationGlobal
            locationGlobal = self.location

            weather = json.loads(r.text)
            print(weather)

            #df = pd.json_normalize(weather['main'])
            df = pd.json_normalize(weather)
            df.to_csv("samplecsv.csv")

            # Check if we had a failure (the forecast will fail in the same way).
            if weather['cod'] != 200:
                raise Exception(weather['message'])

            url = 'http://api.openweathermap.org/data/2.5/forecast?%s&units=metric' % urlencode(params)
            r = requests.get(url)
            forecast = json.loads(r.text)

            self.signals.result.emit(weather, forecast)

        except Exception as e:
            self.signals.error.emit(str(e))

        self.signals.finished.emit()



class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.pushButton.pressed.connect(self.update_weather)
        self.predict_button.pressed.connect(self.predict_fire)
        self.threadpool = QThreadPool()

        self.show()
    def predict_fire(self):
        loaded_rf = joblib.load("my_random_forest.joblib")

        # this is an LA risky day from 2019 that should produce a [1] for fire risk if uncommented
        #x = pd.read_csv('FireRisk_2019.csv')

        #going to try another method of writing a csv file with manual entry of column headers and weather data

        today = date.today()
        # Textual month, day and year
        d2 = today.strftime("%B %d, %Y")
        print("d2 =", d2)

        if locationGlobal == 'Burbank':
            city = 1
        elif locationGlobal == 'San Diego':
            city = 2
        elif locationGlobal == 'Santa Barbara':
            city = 3
        elif locationGlobal == 'Riverside':
            city = 4
        else:
            city = 0

        header = ['Year', 'Month', 'Day', 'TempMax', 'TempAvg', 'TempMin', 'DewPointMax', 'DewpointAvg', 'DewpointMin',
                  'HumidityMax', 'HumidityAvg', 'HumidityMin', 'WindspeedMax', 'WindSpeedAvg', 'WindspeedMin',
                  'PressureMax', 'PressureAvg', 'PressureMin', 'TotalPrecipitation', 'City']
        data = [today.year, today.month, today.day, weather['main']['temp_max']*9/5+32,
                ((weather['main']['temp_max']*9/5+32)+(weather['main']['temp_min']*9/5+32))/2,
                weather['main']['temp_min']*9/5+32, 50, 40, 40, weather['main']['humidity']+20,
                weather['main']['humidity'], weather['main']['humidity']-20, weather['wind']['speed']+5,
                weather['wind']['speed'], 0, (weather['main']['pressure']+.1)/33.8649,
                weather['main']['pressure']/33.8649, (weather['main']['pressure']-.1)/33.8649, 0, city]

        with open('PredictionFromWeather.csv', 'w', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)

            #write the header
            writer.writerow(header)

            #write the data
            writer.writerow(data)

        x = pd.read_csv('PredictionFromWeather.csv')
        y = loaded_rf.predict(x)

        print(y)
        self.prediction_result.setText(str(y))
        print(locationGlobal)

    def alert(self, message):
        alert = QMessageBox.warning(self, "Warning", message)

    def update_weather(self):
        worker = WeatherWorker(self.lineEdit.text())
        worker.signals.result.connect(self.weather_result)
        worker.signals.error.connect(self.alert)
        self.threadpool.start(worker)

    def weather_result(self, weather, forecasts):
        self.latitudeLabel.setText("%.2f °" % weather['coord']['lat'])
        self.longitudeLabel.setText("%.2f °" % weather['coord']['lon'])

        self.windLabel.setText("%.2f m/s" % weather['wind']['speed'])

        self.temperatureLabel.setText("%.1f °C" % weather['main']['temp'])
        self.pressureLabel.setText("%d" % weather['main']['pressure'])
        self.humidityLabel.setText("%d" % weather['main']['humidity'])

        self.sunriseLabel.setText(from_ts_to_time_of_day(weather['sys']['sunrise']))

        self.weatherLabel.setText("%s (%s)" % (
            weather['weather'][0]['main'],
            weather['weather'][0]['description']
        )
                                  )


        self.set_weather_icon(self.weatherIcon, weather['weather'])

        for n, forecast in enumerate(forecasts['list'][:5], 1):
            getattr(self, 'forecastTime%d' % n).setText(from_ts_to_time_of_day(forecast['dt']))
            self.set_weather_icon(getattr(self, 'forecastIcon%d' % n), forecast['weather'])
            getattr(self, 'forecastTemp%d' % n).setText("%.1f °C" % forecast['main']['temp'])

    def set_weather_icon(self, label, weather):
        label.setPixmap(
            QPixmap(os.path.join('images', "%s.png" %
                                 weather[0]['icon']
                                 )
                    )

        )


if __name__ == '__main__':

    app = QApplication([])
    window = MainWindow()
    app.exec_()