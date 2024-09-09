from datetime import datetime
from utils import make_api_request, configure_api_token


def configure_sensors():
    configure_api_token()

    data = {
        'configured_at': datetime.utcnow().isoformat() + 'Z'
    }

    response = make_api_request('sensors/configure', json=data)

    if response.status_code != 202:
        print("Error:", response.status_code, response.text)
        raise response.text

if __name__ == "__main__":
    configure_sensors()
