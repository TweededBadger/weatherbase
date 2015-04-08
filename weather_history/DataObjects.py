
class WeatherObject():
    def __init__(self,temperature = None,dewpoint = None,humidity = None,
                 barometer = None,wind_speed = None,precipitation = None):
        self.precipitation = self.float_or_none(precipitation)
        self.wind_speed = self.float_or_none(wind_speed)
        self.barometer = self.float_or_none(barometer)
        self.humidity = self.float_or_none(humidity)
        self.temperature = self.float_or_none(temperature)
        self.dewpoint = self.float_or_none(dewpoint)

    def __str__(self):
        return_string = ""
        return_string += "Temperature: " + str(self.temperature)
        return_string += "\nwind_speed: " + str(self.wind_speed)
        return_string += "\nbarometer: " + str(self.barometer)
        return_string += "\nhumidity: " + str(self.humidity)
        return_string += "\ndewpoint: " + str(self.dewpoint)
        return_string += "\nprecipitation: " + str(self.precipitation)

        return return_string

    def difference(self,comparison):
        temp_comparison = self.compare_values(self.temperature, comparison.temperature)
        wind_comparison = self.compare_values(self.wind_speed, comparison.wind_speed)
        bar_comparison = self.compare_values(self.barometer, comparison.barometer)
        hum_comparison = self.compare_values(self.humidity, comparison.humidity)
        dewpoint_comparison = self.compare_values(self.dewpoint, comparison.dewpoint)
        precipitation_comparison = self.compare_values(self.precipitation, comparison.precipitation)
        comparison_data = WeatherObject(temperature=temp_comparison,wind_speed=wind_comparison,barometer=bar_comparison,
                                        humidity=hum_comparison,dewpoint=dewpoint_comparison,precipitation=precipitation_comparison)
        return comparison_data

    def float_or_none(self,value):
        return_val = None
        try:
            return_val = float(value)
        except:
            pass
        return return_val

    def compare_values(self,v1,v2):
        return_val = None
        try:
            return_val = v1 - v2
        except:
            pass
        return return_val

