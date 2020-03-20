class Value:
    def __init__(self):
        self.value = None

    def __get__(self, instance, owner):
        return int(self.value)

    def __set__(self, instance, value):
        self.value = value - value * instance.commission


class Account:
    amount = Value()

    def __init__(self, commission):
        self.commission = commission

new_account = Account(0.1)

new_account.amount = 100

print(new_account.amount)
