from forex_python.converter import CurrencyRates

c = CurrencyRates()
enter_curr = ''
final_curr = ''
amount = 0


def get_enter_curr():
    try:
        global enter_curr
        enter_curr = input("Zadej počáteční měnu: ")
        c.get_rates(enter_curr)
    except:
        print('Neplatný kód měny')
        get_enter_curr()


def get_amount():
    try:
        global amount
        amount = input(f"Zadej částku v {enter_curr}: ")
        amount = float(amount)
    except:
        print('Neplatné číslo')
        get_amount()


def get_final_curr():
    try:
        global final_curr
        final_curr = input("Zadej cílovou měnu: ")
        c.get_rates(final_curr)
    except:
        print('Neplatný kód měny')
        get_enter_curr()


get_enter_curr()
get_amount()
get_final_curr()

price = c.get_rate(final_curr, enter_curr)
result = round(amount / price, 2)

print(f"Vysledna castka je {result} {final_curr}")