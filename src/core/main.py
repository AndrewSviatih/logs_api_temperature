from weather.client import WeatherClient

async def main():
    async with WeatherClient() as weather:
        await weather.get_temperature('St. Petersburg')
        print(weather)
        await weather.post_temperature('St. Petersburg', {'hui': 'pizda'})
