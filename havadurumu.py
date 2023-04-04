from boai import *

# Ankara şehri için hava durumunu sorgula
weather = Weather('Ankara')
result = weather.get_weather()

print(result)
