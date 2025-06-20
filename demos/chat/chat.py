from openai import OpenAI
import requests
import time
import json

USER_AGENT = 'BaseChatApp_Weather'


def city_to_gps(city: str) -> tuple[float, float] | None:
    time.sleep(1)
    r = requests.get(
        'https://nominatim.openstreetmap.org/search.php',
        params={
            'city': city,
            'format': 'jsonv2',
        },
        headers={'User-Agent': USER_AGENT}
    )
    res = r.json()

    if not res:
        return None

    try:
        lat = float(res[0]['lat'])
        lon = float(res[0]['lon'])
        return lat, lon
    except (KeyError, IndexError, ValueError):
        return None


def weather(lat: float, lon: float) -> str:
    time.sleep(1)
    r = requests.get(
        'https://api.open-meteo.com/v1/forecast',
        params={
            'latitude': lat,
            'longitude': lon,
            'daily': 'temperature_2m_max',
            'timezone': 'auto'
        },
        headers={'User-Agent': USER_AGENT}
    )
    res = r.json()

    try:
        temp = res['daily']['temperature_2m_max'][0]
        return f"{temp} °C"
    except (KeyError, IndexError):
        return "Weather data unavailable"


api_key: str = open('demo.key').read().strip()
client = OpenAI(api_key=api_key)

tools = [{
    "type": "function",
    "name": "get_weather",
    "description": "Get current temperature for a given location.",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "City, without country, i.e. London"
            }
        },
        "required": ["location"],
        "additionalProperties": False
    }
}]

log: list[dict[str, str | dict]] = []

print('You can start your chat now')
skip_input = False

while True:
    try:
        if not skip_input:
            input_text: str = input('? ')
            log.append({'role': 'user', 'content': input_text})
    except KeyboardInterrupt:
        break

    response = client.responses.create(
        model="gpt-4.1-nano",
        input=log,
        tools=tools,
    )

    for o in response.output:
        log.append(o)

        if o.type == 'message':
            print(f'\x1b[1;33m{o.content[0].text}\x1b[m')
            skip_input = False

        elif o.type == 'function_call':
            args = json.loads(o.arguments)

            if o.name == 'get_weather':
                skip_input = True
                gps = city_to_gps(args['location'])
                if gps is None:
                    log.append({
                        "type": "function_call_output",
                        "call_id": o.call_id,
                        "output": "Unknown location"
                    })
                    print(f"\x1b[1;31mUnknown location: {args['location']}\x1b[m")
                    continue

                lat, lon = gps
                result = weather(lat, lon)
                log.append({
                    "type": "function_call_output",
                    "call_id": o.call_id,
                    "output": result
                })
                print(f'\x1b[1;36mWeather: {result}\x1b[m')
                continue

            raise Exception(f'Unknown function: {o.name}')

print('End of conversation.')
