import requests
import certifi


def hit_api(base_url, users_endpoint, input_string=None):
    # Construct the full URL
    url = f"{base_url}{users_endpoint}"
    try:
        payload = {'input': input_string} if input_string is not None else {}
        response = requests.get(url, json=payload, verify=True)
        if response.status_code == 200:
            return response.status_code
        else:
            return response.status_code
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None
certify_path = r'C:\Users\NagaVeerisetti\PycharmProjects\MapAPI\.venv\Lib\site-packages\root_ca.pem'

print(hit_api("https://map-dev-api.azurewebsites.net/api/Access/", "GetUserAccessInfo", "saikrishna@bftg.com"))