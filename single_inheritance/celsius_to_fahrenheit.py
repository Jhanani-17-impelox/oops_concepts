class Celsius:
    def __init__(self, temperature):
        if temperature < -273.15:
            print("Temperature is less than 0C")
        self.temperature = temperature
    
    def to_fahrenheit(self):
        fahrenheit = (self.temperature * 1.8) + 32
        return fahrenheit

class WeatherReport(Celsius):
    def __init__(self, temperature, location):
        super().__init__(temperature)
        self.location = location
        self.fahrenheit = self.to_fahrenheit()  # Store the converted Fahrenheit value
    
    def report(self):
        print(f"Location: {self.location}")
        print(f"Temperature in Celsius: {self.temperature}")
        print(f"Temperature in Fahrenheit: {self.fahrenheit}")
        
w = WeatherReport(45, "Dubai")
w.report()
