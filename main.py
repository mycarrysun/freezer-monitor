from w1thermsensor import W1ThermSensor
from utils import make_api_request
from datetime import datetime


def send_temp_reading(degrees):
    response = make_api_request('sensors/readings', json={
        'degrees_c': degrees,
        'taken_at': datetime.utcnow().isoformat()+'Z',
    })
    if response.status_code != 201:
        print(response.content)
        raise Exception(f'Unsuccessful response: {response.status_code}')


if __name__ == "__main__":
    sensor = W1ThermSensor()
    degrees_c = sensor.get_temperature()
    send_temp_reading(degrees_c)