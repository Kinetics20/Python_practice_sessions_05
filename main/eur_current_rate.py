import requests


def get_euro_exchange_rate():
    url = 'https://api.nbp.pl/api/exchangerates/rates/a/eur/'
    headers = {'Accept': 'application/json'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        euro_rate = data['rates'][0]['mid']
        return euro_rate
    else:
        print(f'Error fetching data: {response.status_code}')
        return None


# Example usage
rate = get_euro_exchange_rate()
if rate:
    print(f'Current EUR exchange rate: {rate} PLN')
