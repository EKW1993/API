import csv
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        currency = request.form.get('currency')
        amount = float(request.form.get('amount'))

        rates = []
        with open('kursy_walut.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                rates.append(row)

        for rate in rates:
            if rate['code'] == currency:
                converted_amount = amount * float(rate['bid'])
                return f"Koszt kupna {amount} {currency} wynosi {converted_amount:.2f} PLN"

    return render_template('index.html')

if __name__ == '__main__':
    app.run()