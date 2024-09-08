from w1thermsensor import W1ThermSensor
from utils import make_api_request
from datetime import datetime


def send_temp_reading(degrees):
    make_api_request('sensors/create-reading', json={
        'degrees_c': degrees,
        'taken_at': datetime.utcnow().isoformat()+'Z',
    })


if __name__ == "__main__":
    sensor = W1ThermSensor()
    degrees_c = sensor.get_temperature()
    send_temp_reading(degrees_c)