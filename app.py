import requests


response = requests.get('https://api.frankfurter.app/currencies')

print("Please choose from available currencies: ")

if response.status_code == 200:

    data_latest = response.json()

    for currency_code, currency_name in data_latest.items():
        print(f"{currency_code} = {currency_name}")

    from_currency = str(input("From: "))
    to_currency = str(input("To: "))
    amt = float(input("hm?: "))

    response2 = requests.get(f'https://api.frankfurter.app/latest?amount={amt}&from={from_currency}&to={to_currency}')

    conversion = response2.json()

    rates_list = list(conversion["rates"].values())

    print(f'Answer: {rates_list[0]}')
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")