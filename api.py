import csv
import requests

response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()

rates = data[0]['rates']

csv_file = open('exchange_rates.csv', 'w', newline='', encoding='utf-8') 
csv_writer = csv.writer(csv_file, delimiter=';') 
csv_writer.writerow(['currency', 'code', 'bid', 'ask'])

for rate in rates: csv_writer.writerow([rate['currency'], rate['code'], rate['bid'], rate['ask']])

csv_file.close()