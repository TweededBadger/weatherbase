
class WeatherObject():
    def __init__(self,temperature,dewpoint,humidity,barometer,wind_speed,precipitation):
        self.precipitation = precipitation
        self.wind_speed = wind_speed
        self.barometer = barometer
        self.humidity = humidity
        self.temperature = temperature
        self.dewpoint = dewpoint

    def __str__(self):
        return_string = ""
        return_string += "Temperature: " + str(self.temperature)
        return_string += "\nwind_speed: " + str(self.wind_speed)
        return_string += "\nbarometer: " + str(self.barometer)
        return_string += "\nhumidity: " + str(self.humidity)
        return_string += "\ndewpoint: " + str(self.dewpoint)
        return_string += "\nprecipitation: " + str(self.precipitation)

        return return_string

