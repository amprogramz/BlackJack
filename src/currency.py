class currency:
    def __init__(self, chips):
        self._chips = chips

    def __reduce__(self, quantity):
        if quantity <= self._chips:
            self._chips -= quantity

    def __add__(self, quantity):
        self._chips += quantity

    def get_chips(self):
        return self._chips


cur = currency(100)
print(cur.get_chips())
cur.__reduce__(5)
print(cur.get_chips())
cur.__add__(10)
print(cur.get_chips())
