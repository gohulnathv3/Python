import CurrencyConverter
c = CurrencyConverter()
amount = int(input("Enter the amount: "))
from_currency = input("From currency: ").upper()
to_currency = input("To currency: ").upper()
print(from_currency, " To ", to_currency)
result = c.convert(from_currency, to_currency, amount)
print(result)
