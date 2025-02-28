import requests


def get_usd_exchange_rate():
    url = 'https://api.nbp.pl/api/exchangerates/rates/a/usd/'
    headers = {'Accept': 'application/json'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        usd_rate = data['rates'][0]['mid']
        return usd_rate
    else:
        print(f'Error fetching data: {response.status_code}')
        return None


# Example usage
rate = get_usd_exchange_rate()
if rate:
    print(f'Current USD exchange rate: {rate} PLN')
